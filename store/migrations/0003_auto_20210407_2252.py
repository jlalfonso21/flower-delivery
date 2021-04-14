# Generated by Django 3.1.7 on 2021-04-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210407_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='store',
            name='primary_color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Primary Color'),
        ),
        migrations.AlterField(
            model_name='store',
            name='secondary_color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Secondary Color'),
        ),
        migrations.AlterField(
            model_name='store',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
    ]