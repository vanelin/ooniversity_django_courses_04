#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

from django.shortcuts import render
from django.http import HttpResponse


def valid(arg, flag=False, flag_error = True):
    try:
        int_arg = int(arg)
        err_mess = str
        if int_arg == 0 and flag:
            err_mess = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            flag_error = False
    except ValueError:
        if not str(arg):
            int_arg = ''
            err_mess = 'коэффициент не определен'
            flag_error = False
        elif not str(arg).isdigit():
            int_arg = str(arg)
            err_mess = 'коэффициент не целое число'
            flag_error = False
    return (int_arg, err_mess, flag_error)


def quadratic_results(request):
    if request.GET:
        a = valid(request.GET['a'], flag=True)
        b = valid(request.GET['b'])
        c = valid(request.GET['c'])
        if a[2] and b[2] and c[2]:
            d = b[0]**2-4*a[0]*c[0]  # discriminant

            if d < 0:
                result = "Дискриминант: %d \nДискриминант меньше нуля, квадратное уравнение не имеет действительных решений." % (d)
            elif d == 0:
                x = (-b[0]+math.sqrt(d))/2.0*a[0]
                result = "Дискриминант: %d \nДискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % (d, round(x, 1))
            else:
                x1 = float((-b[0]+math.sqrt(d))/2*a[0])
                x2 = float((-b[0]-math.sqrt(d))/2*a[0])
                result = "Дискриминант: %d \nКвадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (d, round(x1, 1), round(x2, 1))
            return render(request, 'results.html', locals())
        else:
            return render(request, 'results.html', locals())
    else:
        a = ('None', '',)
        b = ('None', '',)
        c = ('None', '',)
        return render(request, 'results.html', locals())

    
    # print func(-1, 2, 35)
    # print func(1, 12, 38)
    # print func(1, 6, 9)


    # dict_param = (request.GET.dict()).items()
    # dict_param = request.GET.dict()