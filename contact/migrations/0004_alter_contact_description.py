# Generated by Django 5.1.7 on 2025-03-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
