# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    

    return render(request, 'index.html', {"date": date, "projects":projects})