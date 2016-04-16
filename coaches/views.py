# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Coach

def detail(request, coach_id):
        coach = Coach.objects.get(id=coach_id)
        return render(request, 'coaches/detail.html', {'coaches': coach})