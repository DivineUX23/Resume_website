from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		Conversation
	)

from django.views import generic
import uuid
from datetime import datetime
from . forms import ContactForm, ChatForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		profile = UserProfile.objects.first()

		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		if profile:
			context["user_title"] = profile.title
			context["user_first_name"] = profile.user.first_name.title()
			print(profile.title)
			print(profile.user.first_name.title())

		return context



class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


def assistant(request):
	form = ChatForm
	#context = {"message": messages}
	#return render(request,'main/partials/assistant_message.html', context)
	#------------------------------------------
	#open the db here and save to a file
	#------------------------------------------
	messages.success(request, 'Please note that your conversionation with the AI in this session will be saved for imporving User Experience.')
	return render(request,'main/assistant.html', {'form':form})

"""
class AssistantVIew(generic.FormView):
	template_name = "main/assistant.html"
	form_class = ChatForm
"""

#REQUIRES REVIEW
#class AssistantView(generic.TemplateView):
	#template_name = "main/assistant.html"

	#token expires if tab relaod or tab closes or inactive for 30min.
	#give user token-key.

class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"