# Generated by Django 2.0.5 on 2018-05-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_persontoregister_ssn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persontoregister',
            name='SSN',
        ),
        migrations.AddField(
            model_name='persontoregister',
            name='SSN1',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='persontoregister',
            name='SSN2',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='persontoregister',
            name='SSN3',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='persontoregister',
            name='birth_month',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='persontoregister',
            name='birth_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='persontoregister',
            name='birthday',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
