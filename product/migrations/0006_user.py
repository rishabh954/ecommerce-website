# Generated by Django 5.0.2 on 2024-04-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('mobile_no', models.IntegerField()),
                ('city', models.CharField(max_length=30, null=True)),
                ('propic', models.ImageField(default='images/resource/default-user.png', null=True, upload_to='users')),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
