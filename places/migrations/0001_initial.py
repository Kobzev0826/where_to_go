# Generated by Django 3.0 on 2024-08-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('short_description', models.TextField(blank=True, verbose_name='Short description')),
                ('detail_description', models.TextField(blank=True, verbose_name='Detailed description')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
            ],
        ),
    ]
