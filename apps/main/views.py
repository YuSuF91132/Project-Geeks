from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (Info, Navigation, MainProjects, About, Specializations, 
                    OurProjects,OurServices, Service, Contacts, Footer)

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_id'] = Info.objects.latest('id')
        context['navigation_id'] = Navigation.objects.latest('id')
        context['main_projects_all'] = MainProjects.objects.latest('id')
        context['about_id'] = About.objects.latest('id')
        context['specialization_all'] = Specializations.objects.all()
        context['our_projects_all'] = OurProjects.objects.all()
        context['our_services_id'] = OurServices.objects.latest('id')
        context['service_all'] = Service.objects.all()
        context['contacts_id'] = Contacts.objects.latest('id')
        context['footer_id'] = Footer.objects.latest('id')
        return context
