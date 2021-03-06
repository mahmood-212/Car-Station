# Generated by Django 4.0.4 on 2022-05-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_user_companybranch_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'الشركة', 'verbose_name_plural': 'الشركات'},
        ),
        migrations.AlterModelOptions(
            name='companybranch',
            options={'verbose_name': 'الفرع', 'verbose_name_plural': 'الفروع'},
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='branch_address',
            field=models.URLField(blank=True, null=True, verbose_name='عنوان الفرع'),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='branch_city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='branch_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الفرع'),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='branch_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الفرع'),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='branch_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم هاتف الفرع'),
        ),
        migrations.AlterField(
            model_name='companybranch',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.company', verbose_name='اسم الشركة '),
        ),
    ]
