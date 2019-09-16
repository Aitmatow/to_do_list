import datetime

from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Tasks(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=8, null=False, default=('new', 'Новая'),  blank=False, verbose_name='Статус', choices=STATUS_CHOICES)
    detailed_description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Детальное описание')
    done_date = models.DateField(verbose_name='Дата выполнения', default=None, null=True, blank=True)

    def __str__(self):
        return self.description