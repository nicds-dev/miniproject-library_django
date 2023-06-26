# Generated by Django 4.2.2 on 2023-06-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_author_options_alter_author_description_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_date',
            field=models.DateField(auto_now=True, verbose_name='Created date'),
        ),
        migrations.AddField(
            model_name='book',
            name='created_date',
            field=models.DateField(auto_now=True, verbose_name='Created date'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ManyToManyField(to='book.author'),
        ),
    ]
