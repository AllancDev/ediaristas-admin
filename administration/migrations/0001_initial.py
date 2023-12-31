# Generated by Django 4.2.5 on 2023-09-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('minimum_value', models.FloatField()),
                ('number_of_hours', models.IntegerField()),
                ('commission_percentage', models.FloatField()),
                ('hours_room', models.IntegerField()),
                ('room_value', models.FloatField()),
                ('hours_hall', models.IntegerField()),
                ('hall_value', models.FloatField()),
                ('hours_bathroom', models.IntegerField()),
                ('bathroom_value', models.FloatField()),
                ('hours_kitchen', models.IntegerField()),
                ('kitchen_value', models.FloatField()),
                ('hours_others', models.IntegerField()),
                ('others_value', models.FloatField()),
                ('icon', models.CharField(choices=[('twf-cleaning-1', 'twf-cleaning-1'), ('twf-cleaning-2', 'twf-cleaning-2'), ('twf-cleaning-3', 'twf-cleaning-3')], max_length=14)),
                ('position', models.IntegerField()),
            ],
        ),
    ]
