/* ============================================================
   SULTAN MULTIFORGE ENGINEERING LTD
   projects-data.js  —  All project data lives here.

   HOW TO ADD A NEW PROJECT:
   1. Copy one object below
   2. Give it the next id number
   3. Fill in your details
   4. Put the photo in: assets/images/projects/
   5. Set "image" to just the FILENAME e.g. "project9.png"
   It will automatically appear on the Projects page
   AND get its own full detail page. No other file to touch.
   ============================================================ */

/*
  Auto-detect image base path.
  - index.html is at root → assets/images/projects/
  - pages/*.html are one level deep → ../assets/images/projects/
*/
const IMG_BASE = '/static/images/projects/';
const PAINT_BASE = '/static/images/painting/';

const PROJECTS = [

  {
    id: 1,
    title: "4-Bedroom Residential Building",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Igbo-Eze South, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "In Progress",
    startDate: "2024",
    completionDate: "In Progress",
    contractValue: "On Request",
    floors: "Ground Floor (Single Storey)",
    totalArea: "On Request",
    status: "In Progress",
    image: "project1.png",
    tags: ["Residential", "4 Bedroom", "Bungalow"],
    shortDesc: "A 4-bedroom residential building currently under construction at Igbo-Eze South, Enugu State — wall raising in active progress.",
    overview: [
      "This project is a 4-bedroom residential building currently under active construction at Igbo-Eze South, Enugu State. Engr. Emmanuel Onyedikachi is personally handling the full construction from foundation to roof.",
      "The project involves sandcrete block walling, reinforced concrete columns, and careful setting-out to ensure the building meets the client's specification and all required structural standards.",
      "The site photo shows the wall-raising stage, with the structural frame and blockwork progressing steadily toward lintel level."
    ],
    scope: [
      "Foundation design & construction",
      "Sandcrete block walling",
      "Reinforced concrete columns & lintels",
      "Roof structure & covering",
      "Site management & supervision"
    ],
    technologies: ["Manual Setting-Out", "Structural Design", "Reinforced Concrete"],
    challenges: [
      {
        type: "challenge",
        title: "Site Layout & Accuracy",
        desc: "Ensuring precise setting-out and column alignment across the full building footprint on a raw land site."
      },
      {
        type: "solution",
        title: "Careful Setting-Out & Supervision",
        desc: "Engr. Emmanuel personally supervised the setting-out and column positioning to guarantee structural accuracy before wall-raising began."
      }
    ],
    relatedIds: [2, 4, 7]
  },

  {
    id: 2,
    title: "3-Bedroom Bungalow (Ongoing)",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Nsukka, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "Ongoing",
    startDate: "2024",
    completionDate: "Ongoing",
    contractValue: "On Request",
    floors: "Ground Floor (Bungalow)",
    totalArea: "On Request",
    status: "Ongoing",
    image: "project2.png",
    tags: ["Residential", "3 Bedroom", "Bungalow", "Nsukka"],
    shortDesc: "An ongoing 3-bedroom bungalow construction in Nsukka, Enugu State — blockwork and fencing currently in progress.",
    overview: [
      "This is an ongoing 3-bedroom bungalow project located in Nsukka, Enugu State — the home base of Sultan Multiforge Engineering Ltd. Engr. Emmanuel is managing the full construction personally.",
      "The project involves complete building construction including the perimeter fence, gate columns, and main residential structure. The site photo shows the decorative brick fence and gate column work alongside the main structure in the background.",
      "Progress is active and the building is advancing through the walling and roofing stages under close supervision."
    ],
    scope: [
      "Bungalow structural design",
      "Foundation & substructure",
      "Block walling (main building)",
      "Perimeter fence & gate columns",
      "Site supervision & management"
    ],
    technologies: ["Reinforced Concrete", "Sandcrete Block", "Brick Fencing"],
    challenges: [
      {
        type: "challenge",
        title: "Decorative Brick Fence Integration",
        desc: "The client requested a decorative patterned brick fence that required careful block selection and laying sequence."
      },
      {
        type: "solution",
        title: "Skilled Brickwork Supervision",
        desc: "Engr. Emmanuel supervised the bricklaying pattern closely, ensuring consistent alignment and the decorative effect the client wanted."
      }
    ],
    relatedIds: [1, 4, 7]
  },

  {
    id: 3,
    title: "Residential Duplex",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Anambra State",
    year: "2024",
    client: "Private Client",
    duration: "In Progress",
    startDate: "2023",
    completionDate: "In Progress",
    contractValue: "On Request",
    floors: "G + 1 (Duplex)",
    totalArea: "On Request",
    status: "In Progress",
    image: "project3.png",
    tags: ["Duplex", "Residential", "G+1", "Anambra"],
    shortDesc: "A residential duplex project in Anambra State — G+1 structure with red roof, reaching near-completion stage.",
    overview: [
      "This residential duplex project is located in Anambra State and represents one of Sultan Multiforge's cross-state construction commissions. The building is a G+1 duplex — two floors — with a distinctive red hip roof.",
      "The structure is near completion in the photo, with the full superstructure, roof covering, window frames, and external plastering all done. Final internal finishes and painting are the remaining stages.",
      "Engr. Emmanuel handled the full structural and architectural design, supervised the construction from foundation through to the roof, and is overseeing the finishing stages."
    ],
    scope: [
      "Structural & architectural design",
      "Foundation to superstructure construction",
      "G+1 reinforced concrete frame",
      "Roof structure & red standing seam covering",
      "External plastering & window installation",
      "Project management & site supervision"
    ],
    technologies: ["RC Frame", "Structural Design", "Architectural Design"],
    challenges: [
      {
        type: "challenge",
        title: "Cross-State Project Management",
        desc: "Managing a project in Anambra State while based in Enugu required careful scheduling and dedicated site visits."
      },
      {
        type: "solution",
        title: "Scheduled Site Presence",
        desc: "Engr. Emmanuel maintained a regular site visit schedule and communicated consistently with the client to keep the project on track."
      }
    ],
    relatedIds: [5, 6, 1]
  },

  {
    id: 4,
    title: "3-Bedroom Bungalow with Hip Roof",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Igbo-Eze North, Enugu State",
    year: "2023",
    client: "Private Client",
    duration: "Completed",
    startDate: "2023",
    completionDate: "2023",
    contractValue: "On Request",
    floors: "Ground Floor (Bungalow)",
    totalArea: "On Request",
    status: "Completed",
    image: "project4.png",
    tags: ["3 Bedroom", "Bungalow", "Hip Roof", "Igbo-Eze North"],
    shortDesc: "A beautiful 3-bedroom bungalow at Igbo-Eze North, Enugu State — featuring a striking red standing-seam hip roof.",
    overview: [
      "This 3-bedroom bungalow project at Igbo-Eze North, Enugu State is one of Sultan Multiforge's standout residential builds. The structure features a dramatic wide hip roof with red standing-seam metal covering, giving the building a strong, elegant presence.",
      "The photo shows the building at the roofing stage — timber roof trusses already erected, the distinctive hip shape clearly defined, and the red roof sheets being fixed. Blockwork is complete and window frames are installed.",
      "Engr. Emmanuel designed, costed, and personally supervised this build from ground clearing to roof completion."
    ],
    scope: [
      "Full architectural & structural design",
      "Foundation & block walling",
      "Timber roof truss design & construction",
      "Standing-seam metal roof installation",
      "Window frames & external finishes",
      "BOQ & cost estimation"
    ],
    technologies: ["Timber Roof Truss", "Standing Seam Roofing", "RC Frame"],
    challenges: [
      {
        type: "challenge",
        title: "Wide Hip Roof Geometry",
        desc: "The wide, low-pitched hip roof required precise truss geometry to achieve the correct overhang and aesthetic without structural weakness."
      },
      {
        type: "solution",
        title: "Custom Truss Design & Supervision",
        desc: "Engr. Emmanuel designed each truss configuration individually and supervised the carpentry team on-site to ensure accurate construction."
      }
    ],
    relatedIds: [1, 2, 7]
  },

  {
    id: 5,
    title: "4-Bedroom Residential Duplex",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Enugu, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "Completed",
    startDate: "2023",
    completionDate: "2024",
    contractValue: "On Request",
    floors: "G + 1 (Duplex)",
    totalArea: "On Request",
    status: "Completed",
    image: "project5.png",
    tags: ["Duplex", "4 Bedroom", "G+1", "Enugu"],
    shortDesc: "Completion of a 4-bedroom residential duplex in Enugu — roofing stage with black stone-coated tiles being installed.",
    overview: [
      "This is the completion phase of a 4-bedroom residential duplex in Enugu, Enugu State. The project is a G+1 duplex structure and the site photo captures the roofing stage — timber trusses fully erected and black stone-coated roof tiles being laid by the roofing team.",
      "The building features a gabled and hipped hybrid roof design, bamboo scaffolding on the exterior for plastering works, and the full two-storey RC frame structure clearly visible.",
      "Engr. Emmanuel supervised this project through all stages and personally managed the roofing completion to ensure weathertight installation."
    ],
    scope: [
      "G+1 duplex construction",
      "RC frame & block walling",
      "Timber roof truss construction",
      "Stone-coated roof tile installation",
      "Scaffolding & plastering works",
      "Full site supervision"
    ],
    technologies: ["RC Frame", "Stone-Coated Roofing", "Timber Trusses"],
    challenges: [
      {
        type: "challenge",
        title: "Roof Geometry Complexity",
        desc: "The hybrid gable-hip roof design had multiple junction points requiring careful carpentry coordination."
      },
      {
        type: "solution",
        title: "On-Site Roof Supervision",
        desc: "Engr. Emmanuel was present during all critical roof junction stages to direct the carpenters and ensure the design was built accurately."
      }
    ],
    relatedIds: [6, 3, 4]
  },

  {
    id: 6,
    title: "3-Bedroom Residential Duplex",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Emene, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "In Progress",
    startDate: "2023",
    completionDate: "In Progress",
    contractValue: "On Request",
    floors: "G + 1 (Duplex)",
    totalArea: "On Request",
    status: "In Progress",
    image: "project6.png",
    tags: ["Duplex", "3 Bedroom", "G+1", "Emene"],
    shortDesc: "A 3-bedroom residential duplex at Emene, Enugu State — roofing complete with black stone-coated tiles, finishing works ongoing.",
    overview: [
      "This 3-bedroom residential duplex project is located at Emene, Enugu State. The building is a G+1 (ground floor + first floor) duplex and the site photo shows the structure with the black stone-coated roof now complete.",
      "Bamboo scaffolding is still in place on the exterior, indicating that external plastering, rendering, and finishing works are currently ongoing. The gate and perimeter wall are also under construction.",
      "Engr. Emmanuel is managing this project personally, with the construction now moving from the structural and roofing phase into the finishing and decoration phase."
    ],
    scope: [
      "G+1 duplex structural construction",
      "Block walling & RC frame",
      "Roof truss & stone-coated tile installation",
      "Perimeter fence & gate",
      "External rendering & plastering",
      "Interior finishing (in progress)"
    ],
    technologies: ["RC Frame", "Stone-Coated Roofing", "Sandcrete Block"],
    challenges: [
      {
        type: "challenge",
        title: "Working on Two Levels with Scaffolding",
        desc: "Coordinating external plastering on a G+1 structure while roofing was still ongoing required careful sequencing."
      },
      {
        type: "solution",
        title: "Phased Work Scheduling",
        desc: "Engr. Emmanuel scheduled roofing and plastering works in phases to keep different trades active simultaneously without interference."
      }
    ],
    relatedIds: [5, 3, 1]
  },

  {
    id: 7,
    title: "6 Units of 2-Bedroom Apartments (G+2)",
    category: "Residential Construction",
    categoryFilter: "construction",
    location: "Nsukka, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "Ongoing",
    startDate: "2024",
    completionDate: "Ongoing",
    contractValue: "On Request",
    floors: "G + 2 (3 floors, 6 units)",
    totalArea: "On Request",
    status: "Ongoing",
    image: "project7.png",
    tags: ["Apartment", "G+2", "6 Units", "Nsukka"],
    shortDesc: "An ongoing G+2 block of 6 units of 2-bedroom apartments in Nsukka — Engr. Emmanuel personally on-site reviewing drawings.",
    overview: [
      "This is one of Sultan Multiforge's most significant active projects — a G+2 multi-unit residential development comprising 6 units of 2-bedroom apartments, located in Nsukka, Enugu State.",
      "The site photo shows Engr. Emmanuel Onyedikachi personally on-site, reviewing drawings at the foundation and block-laying stage — exactly the kind of hands-on personal involvement that defines Sultan Multiforge.",
      "This project involves full structural design for a three-storey apartment block, reinforced concrete columns, ground beam, and suspended slab design — a technically more demanding project than a typical bungalow build."
    ],
    scope: [
      "Full structural design (G+2 apartment block)",
      "Foundation & reinforced concrete ground beams",
      "RC columns, slabs & staircase design",
      "Block walling (all 3 floors)",
      "BOQ & cost planning",
      "Personal on-site supervision by Engr. Emmanuel"
    ],
    technologies: ["RC Frame", "Structural Design", "Multi-storey Construction", "BOQ"],
    challenges: [
      {
        type: "challenge",
        title: "Multi-Unit Layout Coordination",
        desc: "Designing 6 identical apartment units in a G+2 block requires precise structural coordination across all three floors."
      },
      {
        type: "solution",
        title: "Detailed Structural Drawing & On-Site Presence",
        desc: "Engr. Emmanuel produced detailed structural drawings for every floor and reviews them personally on-site at each stage to ensure accuracy."
      }
    ],
    relatedIds: [1, 2, 4]
  },

  {
    id: 8,
    title: "Swimming Pool Construction",
    category: "Specialist Construction",
    categoryFilter: "construction",
    location: "Igbo-Eze North, Enugu State",
    year: "2024",
    client: "Private Client",
    duration: "In Progress",
    startDate: "2024",
    completionDate: "In Progress",
    contractValue: "On Request",
    floors: "Below Ground (Pool)",
    totalArea: "On Request",
    status: "In Progress",
    image: "project8.png",
    tags: ["Swimming Pool", "Specialist", "Reinforced Concrete"],
    shortDesc: "A swimming pool construction project at Igbo-Eze North, Enugu State — excavation, concrete walls, and reinforcement in active progress.",
    overview: [
      "This swimming pool construction project at Igbo-Eze North, Enugu State demonstrates the breadth of Sultan Multiforge's engineering capabilities beyond standard building construction.",
      "The site photo shows the pool in its construction phase — the excavation is complete, reinforced concrete retaining walls have been cast on three sides, and the reinforcement cage for the pool shell is being assembled. The construction is taking place in the basement level of a larger building project.",
      "Engr. Emmanuel is managing this specialist work personally, overseeing the waterproofing design, structural shell, and drainage details required for a properly engineered swimming pool."
    ],
    scope: [
      "Pool excavation & setting-out",
      "Reinforced concrete pool shell design",
      "Waterproofing system design",
      "Drainage & pipework coordination",
      "Structural integration with main building",
      "Site supervision & management"
    ],
    technologies: ["Reinforced Concrete", "Waterproofing", "Pool Shell Design"],
    challenges: [
      {
        type: "challenge",
        title: "Waterproofing & Structural Integrity",
        desc: "A swimming pool requires both structural strength and complete waterproofing — two demands that must be met simultaneously."
      },
      {
        type: "solution",
        title: "Integral Waterproofing + Dense RC Mix",
        desc: "Engr. Emmanuel specified an integral crystalline waterproofing admixture in the concrete mix combined with a dense RC wall design to achieve both requirements."
      }
    ],
    relatedIds: [1, 7, 4]
  }

];
