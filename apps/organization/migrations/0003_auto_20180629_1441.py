# Generated by Django 2.0.2 on 2018-06-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_teacher_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=25, verbose_name='年龄'),
        ),
    ]
