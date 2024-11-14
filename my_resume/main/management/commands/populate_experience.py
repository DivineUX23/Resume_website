# management/commands/populate_experience.py
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from main.models import Company, WorkExperience, Tool

class Command(BaseCommand):
    help = 'Populate the database with work experience'

    def handle(self, *args, **kwargs):
        for exp_data in ACTUAL_EXPERIENCES:
            # Create or get company
            company_data = exp_data.pop('company')
            company, _ = Company.objects.get_or_create(
                name=company_data['name'],
                defaults=company_data
            )

            # Create technologies
            technologies = exp_data.pop('technologies_used')
            tech_objects = []
            for tech_name in technologies:
                tech, _ = Tool.objects.get_or_create(
                    name=tech_name,
                    defaults={'category': 'backend'}  # Set appropriate category
                )
                tech_objects.append(tech)

            # Create work experience
            exp_data['company'] = company
            exp_data['start_date'] = parse_date(exp_data['start_date'])
            if 'end_date' in exp_data:
                exp_data['end_date'] = parse_date(exp_data['end_date'])

            experience, created = WorkExperience.objects.get_or_create(
                company=company,
                title=exp_data['title'],
                defaults=exp_data
            )

            # Add technologies to experience
            experience.technologies_used.set(tech_objects)

        self.stdout.write(self.style.SUCCESS('Successfully populated work experience'))


# Sample data for your specific experiences
ACTUAL_EXPERIENCES = [
    {
        'company': {
            'name': 'NCMMS',
            'location': 'Remote',
            'website': '',  # Add website if available
        },
        'title': 'Backend Developer',
        'employment_type': 'full_time',
        'start_date': '2024-07-01',
        'is_current': True,
        'description': """
        Currently working as a Backend Developer focusing on API development and testing optimization.
        """,
        'key_achievements': """
        Enhanced testing efficiency by developing API and function tests using FastAPI, reducing debugging time by over 30%
        Implemented automated testing with mock MySQL and MongoDB databases
        Optimized data management by designing and integrating MongoDB database
        Enhanced overall system performance through database optimization
        """,
        'technologies_used': ['FastAPI', 'MongoDB', 'MySQL', 'Python', 'API Testing']
    },
    {
        'company': {
            'name': 'HealthMate',
            'location': 'Benin City, Edo State, Nigeria',
            'website': '',  # Add website if available
        },
        'title': 'Backend Developer',
        'employment_type': 'full_time',
        'start_date': '2024-01-01',
        'end_date': '2024-05-31',
        'description': """
        Worked on developing a healthcare platform focused on connecting users with medical practitioners.
        """,
        'key_achievements': """
        Collaborated with 10+ developers and designers on healthcare accessibility platform
        Architected scalable backend using FastAPI and Langchain, resulting in 35% increase in user engagement
        Implemented self-diagnosis feature using LangChain
        Gained expertise in healthcare tech and agile development processes
        """,
        'technologies_used': ['FastAPI', 'LangChain', 'Python', 'Agile']
    },
    {
        'company': {
            'name': 'Nigerian National Petroleum Corporation Exploration Production Limited (NNPC)',
            'location': 'Benin City, Edo State, Nigeria',
            'website': 'https://nnpcgroup.com/',
        },
        'title': 'Backend Developer Intern',
        'employment_type': 'internship',
        'start_date': '2023-06-01',
        'end_date': '2023-10-31',
        'description': """
        Developed and implemented asset management system as a Backend Developer Intern.
        """,
        'key_achievements': """
        Developed scalable FastAPI backend and MySQL database for managing assets
        Improved data accuracy and operational efficiency
        """,
        'technologies_used': ['FastAPI', 'MySQL', 'Python', 'Asset Management']
    },
    {
        'company': {
            'name': 'Polymarq',
            'location': 'Remote',
            'website': '',  # Add website if available
        },
        'title': 'DevOps Intern',
        'employment_type': 'internship',
        'start_date': '2023-07-01',
        'end_date': '2023-09-30',
        'description': """
        Worked as a DevOps Intern focusing on AI model deployment and system optimization.
        """,
        'key_achievements': """
        Enhanced AI deployment efficiency through Dockerization
        Deployed AI models on PaperSpace platform
        Improved backend integration and system performance
        """,
        'technologies_used': ['Docker', 'PaperSpace', 'DevOps', 'AI Deployment', 'Backend Integration']
    },
]