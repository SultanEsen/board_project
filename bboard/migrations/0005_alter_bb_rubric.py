# Generated by Django 5.0.6 on 2024-08-03 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(limit_choices_to={'show': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Rubric'),
        ),
    ]
