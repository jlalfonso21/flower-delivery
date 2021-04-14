# Generated by Django 3.1.7 on 2021-04-08 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('l10n_cuba', '0005_populate_table_codigo_postal'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='store',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active?'),
        ),
        migrations.AddField(
            model_name='store',
            name='mun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='l10n_cuba.municipio', verbose_name='Municipality'),
        ),
        migrations.AddField(
            model_name='store',
            name='phone',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='store',
            name='primary_color',
            field=models.CharField(max_length=10, null=True, verbose_name='Primary Color'),
        ),
        migrations.AddField(
            model_name='store',
            name='secondary_color',
            field=models.CharField(max_length=10, null=True, verbose_name='Secondary Color'),
        ),
        migrations.AddField(
            model_name='store',
            name='slogan',
            field=models.TextField(max_length=255, null=True, verbose_name='Slogan'),
        ),
        migrations.AddField(
            model_name='store',
            name='website',
            field=models.URLField(null=True, verbose_name='Website'),
        ),
    ]
