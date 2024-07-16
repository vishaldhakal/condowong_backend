# Generated by Django 3.1.6 on 2024-07-16 02:58

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('preconstruction', '0008_auto_20240614_0654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preconstruction',
            options={'ordering': ['-last_updated', django.db.models.expressions.Case(django.db.models.expressions.When(status='Sell', then=django.db.models.expressions.Value(1)), django.db.models.expressions.When(status='Rent', then=django.db.models.expressions.Value(2)), default=django.db.models.expressions.Value(4), output_field=models.IntegerField())]},
        ),
        migrations.RemoveField(
            model_name='preconstruction',
            name='co_op_available',
        ),
        migrations.RemoveField(
            model_name='preconstruction',
            name='no_of_units',
        ),
        migrations.RemoveField(
            model_name='preconstruction',
            name='occupancy',
        ),
        migrations.AddField(
            model_name='preconstruction',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='preconstruction',
            name='baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='preconstruction',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='preconstruction',
            name='project_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Villa', 'Villa')], default='Apartment', max_length=500),
        ),
        migrations.AlterField(
            model_name='preconstruction',
            name='status',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell')], default='Sale', max_length=500),
        ),
    ]
