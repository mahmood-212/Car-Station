# Generated by Django 4.0.1 on 2022-05-16 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customercar', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_hand_price', models.FloatField(blank=True, null=True)),
                ('tax_price', models.FloatField(blank=True, null=True)),
                ('total_cost', models.FloatField(blank=True, null=True)),
                ('total_after_tax', models.FloatField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branchs', to='company.companybranch')),
                ('carpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carparts', to='customercar.carpart')),
                ('customercar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customercars', to='customercar.customercar')),
            ],
        ),
    ]
