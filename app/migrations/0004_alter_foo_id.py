# Generated by Django 4.1 on 2022-08-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_foo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
