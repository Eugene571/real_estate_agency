# Generated by Django 4.2.19 on 2025-02-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_fix_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
