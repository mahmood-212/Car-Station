# Generated by Django 4.0.4 on 2022-05-19 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumed', '0004_alter_income_user_alter_outcome_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='requiremtsbranch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requiremtsbranches', to='consumed.requiremtsbranch'),
        ),
    ]
