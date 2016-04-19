#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):

    """docstring for QuadraticForm"""
    a = forms.IntegerField(label='коэффициент a', widget=forms.TextInput({"placeholder": "Enter integer"}))
    b = forms.IntegerField(label='коэффициент b', widget=forms.TextInput({"placeholder": "Enter integer"}))
    c = forms.IntegerField(label='коэффициент c', widget=forms.TextInput({"placeholder": "Enter integer"}))

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        # Always return the cleaned data, whether you have changed it or 
        # not.
        else:
            return data