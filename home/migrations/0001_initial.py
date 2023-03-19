# Generated by Django 4.1.3 on 2022-11-20 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(max_length=200)),
                ('home_image', models.URLField(blank=True, null=True)),
                ('home_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SportsNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_title', models.CharField(max_length=200)),
                ('sports_image', models.URLField(blank=True, null=True)),
                ('sports_url', models.TextField()),
            ],
        ),
    ]