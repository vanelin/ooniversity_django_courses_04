# -*- coding: utf-8 -*-
import math
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    text_result = {}
    d = x = x1 = x2 = None
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b**2-4*a*c  # discriminant
            if d < 0:
                d = d
            elif d == 0:
                x = (-b+math.sqrt(d))/2*a
            else:
                x1 = (-b+math.sqrt(d))/2*a
                x2 = (-b-math.sqrt(d))/2*a
            text_result = {'discriminant': d, 'x': x, 'x1': x1, 'x2': x2}
    else:
        form = QuadraticForm()
    text_result.update({'form': form})
    return render(request, 'quadratic/results.html', text_result)
