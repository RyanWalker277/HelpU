# Generated by Django 4.0.2 on 2022-03-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_banks_hospitals_malls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banks',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='libraries',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='malls',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='places',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='restraunts',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='toilets',
            name='Image',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
    ]
