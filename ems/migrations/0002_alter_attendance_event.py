# Generated by Django 4.2.7 on 2024-01-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ems.event'),
        ),
    ]
