# Generated by Django 5.0.2 on 2024-04-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='propic',
            field=models.ImageField(default='img/avatar.jpg', null=True, upload_to='users'),
        ),
    ]
