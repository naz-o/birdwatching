# Generated by Django 3.1.6 on 2021-02-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepowidehard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='djangodb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=5)),
                ('humidity', models.CharField(max_length=5)),
                ('datum', models.DateTimeField(verbose_name='date published')),
                ('bild', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Basictest',
        ),
    ]
