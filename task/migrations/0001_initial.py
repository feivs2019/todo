# Generated by Django 2.1.2 on 2019-09-08 09:16

from django.db import migrations, models
import django.utils.timezone
import django_mysql.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task', models.CharField(default='no title', max_length=128)),
                ('author', django_mysql.models.ListCharField(models.CharField(max_length=128), max_length=516, size=4)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
