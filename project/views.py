from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Project

def list_projects(request):
	"""
	List the projects that have been submitted. 
	"""

	projects = Project.objects.all()

	context = {
		'projects': projects,
	}
	
	return render(request, "list.html", context)

class ProjectDetail(DetailView):
	model = Project
	template_name = 'project.html'	

