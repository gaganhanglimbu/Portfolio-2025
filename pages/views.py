from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView
from .models import CustomUser, Speciality, Experience, Education, Skill, Award, Project, Tag, Contact
from django.urls import reverse_lazy
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.all().first()
        context["service"] = Speciality.objects.all()
        experience = Experience.objects.all()
        context["experience"] = experience.order_by('-start_date')
        eduation = Education.objects.all()
        context["education"] = eduation.order_by('-start_date')
        context["skill"] = Skill.objects.all()
        context["award"] = Award.objects.all()
        context['project'] = Project.objects.all()
        return context
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.all().first()
        experience = Experience.objects.all()
        context["experience"] = experience.order_by('-start_date')
        eduation = Education.objects.all()
        context["education"] = eduation.order_by('-start_date')
        context["skill"] = Skill.objects.all()
        context["award"] = Award.objects.all()
        return context

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class ProjectPageView(TemplateView):
    template_name = 'pages/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.all()
        return context
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pages/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_project_object = self.get_object()
        print(current_project_object.pk)
        related_projects = Project.objects.exclude(pk=current_project_object.pk).order_by("?")[:2]
        context["related_projects"] = related_projects
        
        return context
    
    

class ContactPageView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
