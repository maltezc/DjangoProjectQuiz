# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 06:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_auto_20180115_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='message',
            new_name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_html',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='question_html',
            field=models.TextField(default=''),
        ),
        migrations.RemoveField(
            model_name='question',
            name='message_html',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('user', 'question', 'answer')]),
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]
