# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 08:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pychall', '0005_student_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_date',
            field=models.DateField(default=datetime.date(2017, 4, 19)),
        ),
    ]
