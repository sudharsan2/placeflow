# Generated by Django 5.0.2 on 2024-03-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemanagement', '0007_remove_studentdata_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
