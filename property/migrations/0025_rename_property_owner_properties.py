# Generated by Django 4.2.19 on 2025-02-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_alter_complaint_id_alter_flat_id_alter_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='property',
            new_name='properties',
        ),
    ]
