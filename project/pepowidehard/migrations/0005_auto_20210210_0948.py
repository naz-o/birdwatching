# Generated by Django 3.1.6 on 2021-02-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepowidehard', '0004_auto_20210210_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangodb',
            name='bild',
            field=models.ImageField(default='posts/frx.png', upload_to='posts/'),
        ),
    ]
