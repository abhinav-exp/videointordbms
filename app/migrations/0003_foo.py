# Generated by Django 4.1 on 2022-08-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_videomodel_delete_numpy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', models.TextField(blank=True, db_column='data')),
            ],
        ),
    ]
