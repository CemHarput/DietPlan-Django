# Generated by Django 4.2.14 on 2024-08-07 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_time', models.TimeField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='Plan.plan')),
            ],
        ),
    ]
