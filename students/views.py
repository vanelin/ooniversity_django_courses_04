# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from students.models import Student
from students.forms import StudentModelForm



def list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'students': student})
    else:
        student = Student.objects.filter(courses=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'students': student})


def detail(request, student_id):
    student = get_object_or_404(Student,id=student_id)
    return render(request, 'students/detail.html', {'students': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Student %s %s has been successfully added." % (application.name, application.surname)
            messages.success(request, msg)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    application = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    new_student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        new_student.delete()
        new_message = u"Info on %s %s has been sucessfully deleted." % (new_student.name, new_student.surname)
        messages.success(request, new_message)
        return redirect("students:list_view")
    return render(request, "students/remove.html", {'name': new_student.name, 'surname': new_student.surname})


def remove(request, student_id):
    application = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        application.delete()
        msg = u"Info on %s %s has been sucessfully deleted." % (application.name, application.surname)
        messages.success(request, msg)
        return redirect('students:list_view')
    notice = u"The student %s %s will be removed" % (application.name, application.surname)
    return render(request, 'students/remove.html', {'notice': notice})
