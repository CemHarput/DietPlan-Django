# Generated by Django 4.2.14 on 2024-08-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
