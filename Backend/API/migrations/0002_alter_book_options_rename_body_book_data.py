# Generated by Django 4.1.3 on 2023-05-27 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id', 'data']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='body',
            new_name='data',
        ),
    ]
