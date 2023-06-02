# Generated by Django 4.1.3 on 2023-06-02 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_book_options_rename_id_book_id_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.AutoField(primary_key=True, serialize=False)),
                ('name_author', models.TextField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_genre', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Genre', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='lenguage',
            fields=[
                ('id_lenguage', models.AutoField(primary_key=True, serialize=False)),
                ('name_lenguage', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id_book', 'title_book']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='data',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Description', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_book',
            field=models.TextField(default='ISBN', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='title_book',
            field=models.CharField(default='title', max_length=100),
        ),
    ]
