# Generated by Django 2.0.5 on 2018-05-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default='false')),
                ('todotext', models.CharField(max_length=50)),
            ],
        ),
    ]