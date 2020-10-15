# Generated by Django 3.1.2 on 2020-10-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_delete_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default='Unknown', max_length=50, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Tag'),
        ),
    ]