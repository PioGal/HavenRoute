# Generated by Django 4.1 on 2022-08-25 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HavenRouteApp', '0003_port_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruise',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HavenRouteApp.route'),
        ),
        migrations.AddField(
            model_name='route',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
