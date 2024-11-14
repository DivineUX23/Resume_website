# management/commands/populate_tools.py
from django.core.management.base import BaseCommand
from main.models import Tool

class Command(BaseCommand):
    help = 'Populate the database with default tools'

    def handle(self, *args, **kwargs):
        for index, tool_data in enumerate(SAMPLE_TOOLS):
            Tool.objects.get_or_create(
                name=tool_data['name'],
                defaults={
                    'category': tool_data['category'],
                    'description': tool_data['description'],
                    'order': index
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated tools'))



# Example tools data
SAMPLE_TOOLS = [
    # Backend Frameworks & Tools
    {
        'name': 'Django',
        'category': 'backend',
        'description': 'High-level Python web framework'
    },
    {
        'name': 'FastAPI',
        'category': 'backend',
        'description': 'Modern, fast web framework for building APIs with Python'
    },
    {
        'name': 'LangChain',
        'category': 'ai',
        'description': 'Artificial intelligence framework for Large Language model intergration'
    },
    {
        'name': 'RabbitMQ',
        'category': 'backend',
        'description': 'Distributed task queue'
    },
    {
        'name': 'Redis',
        'category': 'database',
        'description': 'In-memory data structure store'
    },
    
    # Databases
    {
        'name': 'MySQL',
        'category': 'database',
        'description': 'SQL database'
    },
    {
        'name': 'PostgreSQL',
        'category': 'database',
        'description': 'Advanced open source database'
    },
    {
        'name': 'MongoDB',
        'category': 'database',
        'description': 'NoSQL database'
    },
    
    # DevOps & Deployment
    {
        'name': 'Docker',
        'category': 'devops',
        'description': 'Containerization platform'
    },
    {
        'name': 'GitHub Actions',
        'category': 'devops',
        'description': 'CI/CD platform'
    },
    {
        'name': 'Cpanel',
        'category': 'devops',
        'description': 'Cloud platform services'
    },
    
    # Testing
    {
        'name': 'Pytest',
        'category': 'testing',
        'description': 'Testing framework'
    },
    
    # API Tools
    {
        'name': 'Postman',
        'category': 'other',
        'description': 'API development environment'
    },
    {
        'name': 'Swagger',
        'category': 'other',
        'description': 'API documentation'
    },
    
    # Version Control
    {
        'name': 'Git',
        'category': 'other',
        'description': 'Version control system'
    },
]