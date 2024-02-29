# Generated by Django 5.0.2 on 2024-02-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='historyOfArrears',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='maxCurrentArrears',
        ),
        migrations.AddField(
            model_name='companydata',
            name='preferredGender',
            field=models.ManyToManyField(null=True, to='tablemanagement.gender'),
        ),
        migrations.AddField(
            model_name='companydata',
            name='websiteLink',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
