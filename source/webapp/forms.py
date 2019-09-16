from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    status = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES, required=False)
    detailed_description = forms.CharField(max_length=2000,label='Детальное описание', required=False, widget = widgets.Textarea)
    done_date = forms.DateField(label='Дата выполнения', widget=widgets.SelectDateWidget)
