# Generated by Django 3.2.18 on 2023-04-03 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Имя',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Телефон',
        ),
    ]