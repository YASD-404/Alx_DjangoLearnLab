# Generated by Django 5.1.2 on 2024-11-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authot',
            new_name='author',
        ),
    ]
