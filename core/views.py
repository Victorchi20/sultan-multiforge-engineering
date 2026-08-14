from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from django.core.mail import send_mail

from .models import (
    ContactMessage,
    SiteSettings,
    Project,
    ProjectComment,
    ProjectLike,
)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()

    return request.META.get('REMOTE_ADDR')


def home(request):
    site_settings = SiteSettings.objects.first()

    featured_projects = Project.objects.filter(
        is_published=True,
        featured=True
    ).order_by('display_order', '-created_at')[:6]

    context = {
        'site_settings': site_settings,
        'featured_projects': featured_projects,
    }

    return render(request, 'index.html', context)


def about(request):
    site_settings = SiteSettings.objects.first()

    return render(
        request,
        'about.html',
        {'site_settings': site_settings}
    )


def services(request):
    site_settings = SiteSettings.objects.first()

    return render(
        request,
        'services.html',
        {'site_settings': site_settings}
    )


def projects(request):
    site_settings = SiteSettings.objects.first()

    projects = Project.objects.filter(
        is_published=True
    ).annotate(
        likes_count=Count('likes'),
        comments_count=Count('comments')
    ).order_by(
        'display_order',
        '-created_at'
    )

    context = {
        'site_settings': site_settings,
        'projects': projects,
    }

    return render(
        request,
        'projects.html',
        context
    )


def project_detail(request, slug):
    site_settings = SiteSettings.objects.first()

    project = get_object_or_404(
        Project,
        slug=slug,
        is_published=True
    )

    related_projects = Project.objects.filter(
        category=project.category,
        is_published=True
    ).exclude(
        id=project.id
    ).order_by(
        'display_order',
        '-created_at'
    )[:3]

    comments = project.comments.filter(
        is_approved=True
    ).order_by('-created_at')

    user_ip = get_client_ip(request)

    user_has_liked = project.likes.filter(
        ip_address=user_ip
    ).exists()

    context = {
        'site_settings': site_settings,
        'project': project,
        'related_projects': related_projects,
        'comments': comments,
        'likes_count': project.likes.count(),
        'comments_count': comments.count(),
        'user_has_liked': user_has_liked,
    }

    return render(
        request,
        'project_detail.html',
        context
    )


def add_project_comment(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_published=True
    )

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        if not name or not message_text:

            messages.error(
                request,
                'Name and comment are required.'
            )

            return redirect(
                'project_detail',
                slug=slug
            )

        ProjectComment.objects.create(
            project=project,
            name=name,
            email=email,
            message=message_text,
            is_approved=True,
        )

        messages.success(
            request,
            'Your comment has been posted successfully.'
        )

        return redirect(
            'project_detail',
            slug=slug
        )

    return redirect(
        'project_detail',
        slug=slug
    )


def like_project(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_published=True
    )

    if request.method == 'POST':

        ip_address = get_client_ip(request)

        already_liked = ProjectLike.objects.filter(
            project=project,
            ip_address=ip_address
        ).exists()

        if already_liked:

            messages.info(
                request,
                'You have already liked this project.'
            )

        else:

            ProjectLike.objects.create(
                project=project,
                ip_address=ip_address
            )

            messages.success(
                request,
                'You liked this project.'
            )

    return redirect(
        'project_detail',
        slug=slug
    )


def contact(request):
    site_settings = SiteSettings.objects.first()

    # Default empty form data
    form_data = {
        'full_name': '',
        'company': '',
        'email': '',
        'phone': '',
        'service': '',
        'location': '',
        'budget': '',
        'message': '',
    }

    if request.method == 'POST':

        full_name = request.POST.get(
            'full_name',
            ''
        ).strip()

        company = request.POST.get(
            'company',
            ''
        ).strip()

        email = request.POST.get(
            'email',
            ''
        ).strip()

        phone = request.POST.get(
            'phone',
            ''
        ).strip()

        service = request.POST.get(
            'service',
            ''
        ).strip()

        location = request.POST.get(
            'location',
            ''
        ).strip()

        budget = request.POST.get(
            'budget',
            ''
        ).strip()

        message_text = request.POST.get(
            'message',
            ''
        ).strip()

        # Keep submitted data so form can refill
        # if there is a validation error.
        form_data = {
            'full_name': full_name,
            'company': company,
            'email': email,
            'phone': phone,
            'service': service,
            'location': location,
            'budget': budget,
            'message': message_text,
        }

        # Backend validation
        if (
            not full_name
            or not email
            or not phone
            or not service
            or not message_text
        ):

            context = {
                'site_settings': site_settings,
                'error': (
                    'Please fill in all required fields '
                    'before sending your message.'
                ),
                'form_data': form_data,
            }

            return render(
                request,
                'contact.html',
                context
            )

        # ==============================
        # SAVE MESSAGE TO DATABASE
        # ==============================

        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            service=service,
            message=message_text,
        )

        # ==============================
        # SEND EMAIL NOTIFICATION
        # ==============================

        company_name = (
            site_settings.company_name
            if site_settings and site_settings.company_name
            else 'Sultan Multiforge Engineering Ltd'
        )

        email_subject = (
            f'New Contact Enquiry — {company_name}'
        )

        email_body = f"""
You have received a new contact enquiry from your website.

==============================
CONTACT DETAILS
==============================

Full Name:
{full_name}

Company / Organisation:
{company or 'Not provided'}

Email:
{email}

Phone:
{phone}

Service Required:
{service}

Project Location:
{location or 'Not provided'}

Estimated Budget:
{budget or 'Not provided'}

==============================
PROJECT DESCRIPTION
==============================

{message_text}

==============================

This message was submitted through the contact form on your website.
"""

        try:

            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=None,
                recipient_list=[
                    'emmanueleya1998@gmail.com'
                ],
                fail_silently=False,
            )

        except Exception as e:

            print(
                f'Contact email sending failed: {e}'
            )

        # ==============================
        # SUCCESS
        # ==============================

        messages.success(
            request,
            'Your message has been sent successfully.'
        )

        return redirect(
            '/contact/?success=1'
        )

    context = {
        'site_settings': site_settings,
        'form_data': form_data,
    }

    return render(
        request,
        'contact.html',
        context
    )