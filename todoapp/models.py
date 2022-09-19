from django.db import models


class Article(models.Model):
    CHOICES = (('new', 'Новая'), ('in process', 'В процессе'), ('ready', 'Сделано'))

    description = models.CharField(verbose_name='Описание', max_length=200, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', choices=CHOICES, max_length=15, default='new', null=False,
                              blank=False)
    deadline = models.DateField(verbose_name='Дата выполнения', default='')

    def __str__(self):
        return f'{self.description} - {self.status}'
