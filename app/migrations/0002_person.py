# Generated by Django 2.2.4 on 2019-08-29 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
