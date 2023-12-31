# Generated by Django 4.0.2 on 2022-04-12 11:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.categoriespost')),
            ],
        ),
        migrations.CreateModel(
            name='SectionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.categoriespost')),
                ('courses', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.coursespost')),
            ],
        ),
        migrations.CreateModel(
            name='StepsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.categoriespost')),
                ('section', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.sectionpost')),
            ],
        ),
        migrations.CreateModel(
            name='ParcoursPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.categoriespost')),
            ],
        ),
        migrations.CreateModel(
            name='LevelPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.categoriespost')),
                ('parcours', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.parcourspost')),
            ],
        ),
        migrations.AddField(
            model_name='coursespost',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.levelpost'),
        ),
    ]
