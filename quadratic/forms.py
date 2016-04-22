# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """ форма ввода коэффиц квадратного уравнения """
    a = forms.IntegerField(
        label="коэффициент a", required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))
    b = forms.IntegerField(
        label="коэффициент b", required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))
    c = forms.IntegerField(
        label="коэффициент c", required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))

    def clean_a(self):
        data = self.cleaned_data['a']
        if int(data) == 0:
           raise forms.ValidationError(u"коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return data

    # def clean_a(self):
    #     data = self.cleaned_data['a']
    #     if data == 0:
    #         msg = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"
    #         self.add_error('a', msg)
    #     return data
