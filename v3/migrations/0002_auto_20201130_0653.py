# Generated by Django 3.0.9 on 2020-11-30 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
