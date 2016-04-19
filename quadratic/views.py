#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b**2-4*a*c  # discriminant
            discriminant = "Дискриминант: %s" % (d)
            if d < 0:
                result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b+math.sqrt(d))/2.0*a
                result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % (round(x, 1))
            else:
                x1 = float((-b+math.sqrt(d))/2*a)
                x2 = float((-b-math.sqrt(d))/2*a)
                result = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (round(x1, 1), round(x2, 1))
            return render(request, 'quadratic/results.html', locals())
        else:
            return render(request, 'quadratic/results.html', locals())
    form = QuadraticForm()
    return render(request, 'quadratic/results.html', {'form': form})
