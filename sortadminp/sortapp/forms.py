from django import  forms

class UserForm(forms.Form):
    flag = forms.BooleanField()

class ViewForm(forms.Form):
    analisys_name = forms.CharField(label="Введите наименование производственной номенклатуры")

