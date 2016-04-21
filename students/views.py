# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'students': student})
    else:
        student = Student.objects.filter(courses=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'students': student})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'students': student})


def students_add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u'Student %s %s has been successfully added.' % (
                application.name, application.surname)
            messages.success(request, msg)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    return render(request, 'students/add.html', context)


def students_edit(request, student_id):
    application = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            msg = u'Info on the student has been sucessfully changed.'
            messages.success(request, msg)
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})


def students_remove(request, student_id):
    application = Student.objects.get(id=student_id)
    if request.method == 'POST':
        application.delete()
        msg = u'Info on %s %s has been sucessfully deleted.' % (
            application.name, application.surname)
        messages.success(request, msg)
        return redirect('students:list_view')
    notice = u'The student %s %s will be removed' % (
        application.name, application.surname)
    return render(request, 'students/remove.html', {'notice': notice})
