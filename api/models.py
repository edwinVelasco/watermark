# from django.db import models

# Create your models here.
from djongo import models


class Document(models.Model):
    # auto update when data is inserted
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # auto update when data is altered
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    title = models.CharField(max_length=45, null=True)
    slug = models.SlugField(max_length=100)
    doc_type = models.CharField(max_length=25)
    period = models.CharField(max_length=5)
    student = models.CharField(max_length=8)
    dir_file = models.SlugField(max_length=100, null=True, default=None)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ('-create_at',)
        db_table = 'api_v1_documents'

    def __str__(self):
        return self.title


class Token(models.Model):
    create_at = models.DateField(auto_now_add=True, auto_now=False)
    token = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
        ordering = ('-create_at',)
        db_table = 'api_v1_token'

    def __str__(self):
        return self.token


class LogsDocuments(models.Model):
    ACTION_FLAG_CHOICES = ((1, 'Addition'), (2, 'Change'),
                           (3, u'Deletion'),)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    action_flag = models.PositiveSmallIntegerField(choices=ACTION_FLAG_CHOICES)
    change_message = models.TextField(blank=False)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs de documentos'
        ordering = ('-create_at',)
        db_table = 'api_v1_logs'

    def __str__(self):
        return f'{self.ACTION_FLAG_CHOICES[self.action_flag]}, ' \
            f'{self.create_at}'
