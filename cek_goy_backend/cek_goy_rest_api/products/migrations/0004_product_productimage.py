# Generated by Django 3.2.8 on 2022-08-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220825_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Product Image'),
        ),
    ]