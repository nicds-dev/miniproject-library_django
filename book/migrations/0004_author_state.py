# Generated by Django 4.2.2 on 2023-06-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_author_created_date_book_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='state',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
    ]
