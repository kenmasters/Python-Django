# Generated by Django 2.1.2 on 2018-10-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdb_app', '0003_auto_20181023_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]