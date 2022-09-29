from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView

from portfolio.models import Category, Client, Education, PriceTable, Project, Skills, Style, UserDetails, WhatIdo, WorkExperience
# Create your views here.
class Portfolio(TemplateView):
    template_name = "portfolio/index.html"
    #model = UserDetails
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_data"] = UserDetails.objects.all()[0]
        context["skills"] = Skills.objects.all()
        context["idos"] = WhatIdo.objects.all()
        context["style"] = Style.objects.all()[0]
        context["educations"] = Education.objects.all()
        context["works"] = WorkExperience.objects.all()
        context["clients"] = Client.objects.all()
        context["prices"] = PriceTable.objects.all()
        context["categories"] = Category.objects.all()
        context["projects"] = Project.objects.all()
        #stringit = str(context["skills"][0].type)
        #print(type(context["skills"][0].type))
        return context
    
    #context_object_name = "user_data"