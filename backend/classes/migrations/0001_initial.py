# Generated by Django 2.2.17 on 2021-01-22 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import home.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_populate_weekdays'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_parent_school_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('days', models.ManyToManyField(related_name='classes', to='home.WeekDay')),
                ('students', models.ManyToManyField(blank=True, related_name='classes', to='users.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to='users.Teacher')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('video', models.FileField(upload_to=home.utils.get_upload_path, verbose_name='Video')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_video', to=settings.AUTH_USER_MODEL)),
                ('uploaded_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='classes.Class')),
            ],
            options={
                'verbose_name': 'Class Video',
                'verbose_name_plural': 'Class Videos',
            },
        ),
        migrations.CreateModel(
            name='ClassVideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('content', models.TextField(verbose_name='Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_video_comments', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='classes.ClassVideo')),
            ],
            options={
                'verbose_name': 'Class Video Comment',
                'verbose_name_plural': 'Class Video Comments',
            },
        ),
    ]