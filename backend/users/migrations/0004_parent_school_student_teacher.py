# Generated by Django 2.2.17 on 2021-01-19 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import home.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210118_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='Phone number')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=home.utils.get_upload_path, verbose_name='Profile picture')),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('student_code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Student Code')),
                ('teacher_code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Teacher Code')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Color')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='Phone number')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=home.utils.get_upload_path, verbose_name='Profile picture')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='users.School', verbose_name='School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='Phone number')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=home.utils.get_upload_path, verbose_name='Profile picture')),
                ('student_id', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Student ID')),
                ('grade', models.CharField(blank=True, choices=[('kindergarten', 'Kindergarten'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eight', 'Eigth'), ('freshman', 'Freshman'), ('sophomore', 'Sophomore'), ('junior', 'Junior'), ('senior', 'Senior')], max_length=50, null=True, verbose_name='Grade')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.School', verbose_name='School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='Phone number')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=home.utils.get_upload_path, verbose_name='Profile picture')),
                ('students', models.ManyToManyField(related_name='parents', to='users.Student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
