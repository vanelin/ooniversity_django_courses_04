# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):

    a = forms.IntegerField(
        label='коэффициент a', required=True, widget=forms.TextInput)
    b = forms.IntegerField(
        label='коэффициент b', required=True, widget=forms.TextInput)
    c = forms.IntegerField(
        label='коэффициент c', required=True, widget=forms.TextInput)

    def clean_a(self):
        cleaned_data = super(QuadraticForm, self).clean()
        data = self.cleaned_data['a']
        if data is 0:
            msg = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"
            self.add_error('a', msg)
        return data

    # def clean_a(self):
    #     data = self.cleaned_data['a']
    #     if data == 0:
    #         raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
    #     return data
