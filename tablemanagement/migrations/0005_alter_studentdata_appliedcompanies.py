# Generated by Django 5.0.2 on 2024-02-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemanagement', '0004_alter_companydata_ctc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='appliedCompanies',
            field=models.ManyToManyField(null=True, related_name='appliedcompanies1', to='tablemanagement.companydata'),
        ),
    ]
