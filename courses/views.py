# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = Lesson.objects.filter(course = course_id)
    return render(request, 'courses/detail.html',{'course':course, 'lesson':lesson})


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Course %s has been successfully added." % (application.name)
            messages.success(request, msg)
            return redirect('pybursa:index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    application = get_object_or_404(Course, id=student_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, u"The changes have been saved.")
    else:
        form = CourseModelForm(instance=application)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    application = get_object_or_404(Course, id=student_id)
    if request.method == 'POST':
        application.delete()
        msg = u"Course %s has been deleted." % (application.name)
        messages.success(request, msg)
        return redirect('students:list_view')
    notice = u"The student %s %s will be removed" % (application.name, application.surname)
    return render(request, 'courses/remove.html', {'notice': notice})