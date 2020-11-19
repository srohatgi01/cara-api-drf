# Generated by Django 3.0.9 on 2020-11-19 13:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('totaltime', models.PositiveIntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(default='', max_length=100)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('zip_code', models.CharField(blank=True, max_length=6)),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('photo_url', models.URLField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zorg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unique_id', models.EmailField(max_length=30, unique=True)),
                ('owner_first_name', models.CharField(max_length=20)),
                ('owner_last_name', models.CharField(max_length=20)),
                ('salon_email_id', models.EmailField(max_length=100)),
                ('owner_email_id', models.EmailField(max_length=100)),
                ('open_year_of_salon', models.CharField(max_length=4)),
                ('website', models.URLField(blank=True, max_length=100)),
                ('base_rating', models.IntegerField(default=2)),
                ('profile_photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/profile_photo/')),
                ('cover_photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/cover_photo/')),
                ('photo_1', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/zorg_images/')),
                ('photo_2', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/zorg_images/')),
                ('photo_3', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/zorg_images/')),
                ('photo_4', models.ImageField(blank=True, max_length=200, null=True, upload_to='zorg/zorg_images/')),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zorg_Branche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('zip_code', models.CharField(blank=True, max_length=6)),
                ('zorg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='v3.Zorg')),
            ],
        ),
        migrations.CreateModel(
            name='UserCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v3.User')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('time', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='v3.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='zorg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='v3.Zorg'),
        ),
        migrations.CreateModel(
            name='AppointmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='v3.Appointment')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='v3.Service')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='v3.Zorg_Branche'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v3.Appointment_Status'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v3.User'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='zorg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v3.Zorg'),
        ),
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('link', models.URLField(max_length=255)),
                ('zorg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v3.Zorg')),
            ],
        ),
    ]
