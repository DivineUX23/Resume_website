# management/commands/populate_about.py
from django.core.management.base import BaseCommand
from main.models import AboutMe

class Command(BaseCommand):
    help = 'Populate the About Me section'

    def handle(self, *args, **kwargs):
        AboutMe.objects.get_or_create(
            headline=ABOUT_ME_DATA['headline'],
            defaults=ABOUT_ME_DATA
        )
        self.stdout.write(self.style.SUCCESS('Successfully populated About Me section'))




ABOUT_ME_DATA = {
    'headline': 'Backend Engineer Specializing in High-Performance Systems & AI Integration',
    'short_bio': 'Transforming business ideas into scalable backend solutions with proven 40%+ performance improvements. Expertise in FastAPI, Django, and AI integration.',
    'detailed_bio': """
    🎯 What I Bring to Your Project

    I transform complex business requirements into high-performance backend solutions that scale. Whether you're a startup looking to build your MVP or an established company seeking to optimize your systems, I deliver results that matter.

    ⚡ Key Capabilities & Impact

    Backend Architecture & Development:
    • Reduced system response times by through optimized API design
    • Built scalable systems handling concurrent users
    • Expertise in FastAPI, Django, Flask, and modern Python development
    • Strong focus on clean, maintainable, and well-documented code

    Database & System Optimization:
    • Advanced experience with MySQL and MongoDB implementations
    • Efficient data modeling and query optimization
    • Message broker integration (RabbitMQ) for distributed systems
    • Proven track record of improving system reliability

    AI Integration & Automation:
    • Seamless integration of AI models into production systems
    • Development of AI-powered features that enhance user experience
    • Implementation of automated testing and deployment pipelines
    • Real-world experience with LangChain and other AI frameworks

    🚀 Recent Success Stories

    Healthcare Platform Development:
    • Built robust backend system capable of supporting 1000+ daily users
    • Implemented AI-driven diagnosis system to aid early sickness detection and suggest remedies
    • Integrated real-time emergency response features

    Asset Management System:
    • Developed system managing corporate assets
    • Reduced manual tracking errors by 30%
    • Implemented automated reporting and analytics
    • Enhanced data accuracy and operational efficiency

    AI Model Deployment:
    • Optimized backend integration for AI models
    • Implemented efficient testing and validation systems

    💼 What You Get

    1. Technical Excellence:
       • Clean, efficient, and maintainable code
       • Scalable architecture from day one
       • Comprehensive documentation
       • Performance optimization

    2. Project Management:
       • Clear communication and regular updates
       • Meeting deadlines consistently
       • Flexible adaptation to project needs

    3. Innovation & Problem Solving:
       • Creative solutions to complex challenges
       • Integration of cutting-edge technologies
       • Future-proof architecture decisions
       • Performance-focused development

    🤝 Perfect Fit For:

    • Startups building their MVP
    • Companies needing system optimization
    • Projects requiring AI integration
    • Healthcare tech initiatives
    • Asset management systems
    • Real-time processing applications

    🎯 Specialized Solutions For:

    • High-performance API development
    • Database optimization
    • AI model integration
    • Scalable architecture design
    • System reliability improvement
    • Automated testing implementation

    📈 Value Proposition

    Working with me means getting:
    • Proven performance improvements
    • Scalable solutions from the start
    • AI-ready infrastructure
    • Clean, maintainable code
    • Regular communication and updates
    • Quick problem resolution

    Ready to build something great? Let's discuss how I can help turn your vision into reality.

    📧 Get in Touch:
    I'm currently available for new projects and would be happy to discuss your specific needs and how I can help achieve your goals.


    
        
    🏆🏆 ABOUT_ME_DATA 🏆🏆

    🌟 Vision & Mission

    I'm on a mission to position Africa at the forefront of global technological innovation. My journey involves crafting robust backend systems that not only solve today's challenges but also lay the groundwork for tomorrow's breakthroughs.

    🔬 Future Focus

    My interests span across transformative technologies:
    • Artificial Intelligence advancement in African contexts
    • Space technology applications
    • Quantum computing possibilities
    • Nuclear fusion energy solutions
    • Product development for emerging markets

    🌈 The Bigger Picture

    I believe in a future where African innovation leads global technological advancement. Every line of code I write, every system I design, and every solution I develop is a step toward creating technologies that will:
    • Enhance life on Earth
    • Bridge global technological divides
    • Prepare humanity for a multi-planetary future
    • Create opportunities for the next generation of African innovators

    💡 Innovation Through Collaboration

    I'm always excited to connect with fellow innovators, especially those who share my vision of using technology to create meaningful impact. Whether it's discussing potential collaborations, exploring new technologies, or sharing insights about the future of tech in Africa, I'm open to meaningful conversations.

    The future of technology is being written right now, and I'm ensuring Africa is not just part of the story – but leading it.

    Let's connect and explore how we can create impact together.
    """,
    'github_url': 'https://github.com/yourusername',  # Replace with your actual GitHub URL
    'linkedin_url': 'https://linkedin.com/in/yourprofile',  # Replace with your actual LinkedIn URL
    'email': 'your.email@example.com'  # Replace with your actual email
}
