# Generated by Django 3.2.9 on 2021-12-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_qu1pfb.png', upload_to='images/'),
        ),
    ]