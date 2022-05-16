# Generated by Django 4.0.1 on 2022-05-16 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_car_name', models.CharField(blank=True, max_length=255, null=True)),
                ('owner_car_phone', models.IntegerField(blank=True, null=True)),
                ('car_company', models.CharField(blank=True, max_length=255, null=True)),
                ('owner_identity', models.IntegerField(blank=True, null=True)),
                ('car_plate', models.CharField(blank=True, max_length=255, null=True)),
                ('car_color', models.CharField(blank=True, max_length=255, null=True)),
                ('date_entery', models.DateTimeField(auto_now=True)),
                ('car_under_process', models.BooleanField(blank=True, default=True, null=True)),
                ('car_ready', models.BooleanField(blank=True, default=False, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='company.companybranch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emplyees', to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CarPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(blank=True, max_length=255, null=True)),
                ('part_price', models.IntegerField(blank=True, null=True)),
                ('part_invoice', models.ImageField(blank=True, null=True, upload_to='')),
                ('customer_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customercar', to='customercar.customercar')),
            ],
        ),
    ]