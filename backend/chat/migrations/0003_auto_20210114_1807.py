# Generated by Django 2.2.17 on 2021-01-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210114_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='contacts',
            field=models.ManyToManyField(related_name='_contact_contacts_+', to='chat.Contact', verbose_name='Contacts'),
        ),
    ]
