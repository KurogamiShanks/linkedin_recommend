# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-11 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link_rec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllJobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(default=None, max_length=500)),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='link_rec.AllJobTitle')),
            ],
        ),
        migrations.CreateModel(
            name='AllParsedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('header', models.CharField(max_length=500, null=True)),
                ('url', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500, null=True)),
                ('school_program', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='parsedprofile',
            name='uo',
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job5',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job6',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job7',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job8',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='job9',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc4',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc5',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc6',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc7',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc8',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc9',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='parsedprofile',
            name='header',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='parsedprofile',
            name='school',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='parsedprofile',
            name='school_program',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='alljobtitle',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link_rec.AllParsedProfile'),
        ),
    ]
