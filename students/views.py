# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):

    """docstring for StudentListView"""
    model = Student
    paginate_by = 2
    # context_object_name = 'student'

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):

    """docstring for StudentDetailView"""
    model = Student


class StudentCreateView(CreateView):

    """docstring for StudentCreateView"""
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Student registration"
        return context

    def form_valid(self, form):
        application = form.save()
        msg = u"Student %s %s has been successfully added." % (
            application.name, application.surname)
        messages.success(self.request, msg)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):

    """docstring for StudentUpdateView"""
    model = Student
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('students:edit')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Student info update"
        return context

    def get_success_url(self):
        return reverse_lazy('students:edit', args=(self.object.id,))
        # return reverse_lazy('students:edit', kwargs={'pk': self.get_object().id})

    def form_valid(self, form):
        application = form.save()
        messages.success(
            self.request, u"Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):

    """docstring for StudentDeleteView"""
    model = Student
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = u"Student info suppression"
        context['notice'] = u"Студент %s %s будет удален" % (
            self.object.name, self.object.surname)
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Info on {} has been sucessfully deleted.'.format(self.get_object()))
        return super(StudentDeleteView, self).delete(self, request, *args, **kwargs)

'''
def list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'students': student})
    else:
        student = Student.objects.filter(courses=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'students': student})


def detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/detail.html', {'students': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Student %s %s has been successfully added." % (
                application.name, application.surname)
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
            messages.success(
                request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    application = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        application.delete()
        msg = u"Info on %s %s has been sucessfully deleted." % (
            application.name, application.surname)
        messages.success(request, msg)
        return redirect('students:list_view')
    notice = u"The student %s %s will be removed" % (
        application.name, application.surname)
    return render(request, 'students/remove.html', {'notice': notice})
'''