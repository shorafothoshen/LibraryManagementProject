# Generated by Django 4.2.11 on 2024-05-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_delete_reviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/media/image/'),
        ),
    ]
