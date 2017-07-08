# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-08 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=500)),
                ('header', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('school_program', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=250)),
                ('current_school', models.CharField(choices=[('uoft', 'University of Toronto'), ('harvard', 'Harvard'), ('MIT', 'MIT'), ('waterloo', 'Univertsity of Waterloo')], default='uoft', max_length=100)),
                ('school_program', models.CharField(choices=[('computer_science', 'Computer Science'), ('commerce', 'Commerce'), ('medicine_lifesci', 'Medicine/Lifesci/Healthsci'), ('math_statistics', 'Math/Statistics/Physics')], default='computer_science', max_length=100)),
                ('school_of_interest', models.CharField(choices=[('uoft', 'University of Toronto'), ('harvard', 'Harvard'), ('MIT', 'MIT'), ('waterloo', 'Univertsity of Waterloo')], default='uoft', max_length=100)),
                ('industry_of_interest', models.CharField(choices=[('software', 'software'), ('entrepreneur', 'entrepreneur'), ('data_science', 'data science'), ('research', 'research'), ('finance', 'finance'), ('medicine', 'medicine')], default='software', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('parsedprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='link_rec.ParsedProfile')),
                ('job1', models.CharField(max_length=500)),
                ('job2', models.CharField(max_length=500)),
                ('job3', models.CharField(max_length=500)),
                ('job4', models.CharField(max_length=500)),
                ('job5', models.CharField(max_length=500)),
                ('job6', models.CharField(max_length=500)),
                ('job7', models.CharField(max_length=500)),
                ('job8', models.CharField(max_length=500)),
                ('job9', models.CharField(max_length=500)),
            ],
            bases=('link_rec.parsedprofile',),
        ),
        migrations.AddField(
            model_name='parsedprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('jobtitle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='link_rec.JobTitle')),
                ('loc1', models.CharField(max_length=500)),
                ('loc2', models.CharField(max_length=500)),
                ('loc3', models.CharField(max_length=500)),
                ('loc4', models.CharField(max_length=500)),
                ('loc5', models.CharField(max_length=500)),
                ('loc6', models.CharField(max_length=500)),
                ('loc7', models.CharField(max_length=500)),
                ('loc8', models.CharField(max_length=500)),
                ('loc9', models.CharField(max_length=500)),
            ],
            bases=('link_rec.jobtitle',),
        ),
    ]
