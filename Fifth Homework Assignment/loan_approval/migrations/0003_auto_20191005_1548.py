# Generated by Django 2.2.6 on 2019-10-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approval', '0002_auto_20191005_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapproval',
            name='Property_Area',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')], max_length=10),
        ),
    ]
