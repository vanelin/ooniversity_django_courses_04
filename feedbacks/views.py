# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbackView(CreateView):

    """docstring for FeedbackView"""
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['page_title'] = u"Feedback"
        return context

    def form_valid(self, form):
        application = form.save()
        mail_admins(application.subject, application.message, fail_silently=False)
        msg = u"Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, msg)
        return super(FeedbackView, self).form_valid(form)