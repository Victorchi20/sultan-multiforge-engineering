from django.db import models
from django.utils.text import slugify


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('structural', 'Structural & Architectural Designs'),
        ('construction', 'Building Construction (Residential)'),
        ('commercial', 'Building Construction (Commercial)'),
        ('management', 'Site / Project Management'),
        ('boq', 'BOQ Estimation & Quantity Surveying'),
        ('decoration', 'Wall Decoration (Screening & Painting)'),
        ('interior', 'Interior & Exterior Designs'),
        ('equipment', 'Construction Equipment Rentals'),
        ('other', 'Other / Not Sure'),
    ]

    BUDGET_CHOICES = [
        ('Below ₦1 Million', 'Below ₦1 Million'),
        ('₦1M – ₦5M', '₦1M – ₦5M'),
        ('₦5M – ₦20M', '₦5M – ₦20M'),
        ('₦20M – ₦100M', '₦20M – ₦100M'),
        ('Above ₦100M', 'Above ₦100M'),
        ('Not Yet Determined', 'Not Yet Determined'),
    ]

    full_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    location = models.CharField(max_length=200, blank=True, null=True)
    budget = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=BUDGET_CHOICES
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"


class SiteSettings(models.Model):
    company_name = models.CharField(
        max_length=200,
        default="Sultan Multiforge Engineering Ltd"
    )
    company_tagline = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    footer_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('residential', 'Residential Construction'),
        ('commercial', 'Commercial Construction'),
        ('structural', 'Structural Design'),
        ('interior', 'Interior / Exterior Design'),
        ('renovation', 'Renovation / Finishing'),
        ('management', 'Project Management'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('planned', 'Planned'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    short_description = models.CharField(max_length=255)
    description = models.TextField()
    overview = models.TextField(blank=True, null=True)

    client_name = models.CharField(max_length=200, blank=True, null=True)
    project_location = models.CharField(max_length=255, blank=True, null=True)
    contract_value = models.CharField(max_length=100, blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    floors = models.CharField(max_length=100, blank=True, null=True)
    total_area = models.CharField(max_length=100, blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='completed'
    )

    image = models.ImageField(upload_to='projects/')

    scope = models.TextField(blank=True, null=True)
    technologies = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)

    challenge_1_title = models.CharField(max_length=255, blank=True, null=True)
    challenge_1_desc = models.TextField(blank=True, null=True)
    solution_1_title = models.CharField(max_length=255, blank=True, null=True)
    solution_1_desc = models.TextField(blank=True, null=True)

    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def client(self):
        return self.client_name

    @property
    def location(self):
        return self.project_location

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def approved_comments(self):
        return self.comments.filter(is_approved=True).order_by('-created_at')


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.project.title} - Gallery Image"


class ProjectComment(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()

    # Admin-only reply
    admin_reply = models.TextField(blank=True, null=True)

    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.project.title}"


class ProjectLike(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'ip_address')

    def __str__(self):
        return f"{self.project.title} - {self.ip_address}"