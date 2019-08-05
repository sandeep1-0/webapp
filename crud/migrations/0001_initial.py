# Generated by Django 2.1.7 on 2019-07-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=100)),
                ('clg_email', models.EmailField(max_length=254)),
                ('clg_address', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'college',
            },
        ),
    ]