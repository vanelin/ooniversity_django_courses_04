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
            print form.cleaned_data
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b**2-4*a*c  # discriminant
            if d < 0:
                result = "Дискриминант: %d \nДискриминант меньше нуля, квадратное уравнение не имеет действительных решений." % (
                    d)
            elif d == 0:
                x = (-b+math.sqrt(d))/2.0*a
                result = "Дискриминант: %d \nДискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % (
                    d, round(x, 1))
            else:
                x1 = float((-b+math.sqrt(d))/2*a)
                x2 = float((-b-math.sqrt(d))/2*a)
                result = "Дискриминант: %d \nКвадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (
                    d, round(x1, 1), round(x2, 1))
            return render(request, 'results.html', locals())
        else:
            return render(request, 'results.html', locals())
    else:
        form = QuadraticForm()
        return render(request, 'results.html', {'form': form})
