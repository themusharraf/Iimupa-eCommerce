# Generated by Django 4.2 on 2023-04-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('dec', models.CharField(max_length=222)),
                ('category', models.CharField(max_length=222)),
            ],
        ),
    ]
