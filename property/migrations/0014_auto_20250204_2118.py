# Generated by Django 2.2.24 on 2025-02-04 18:18

from django.db import migrations


def add_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    # Получаем все объекты Flat и предварительно загружаем связанных владельцев
    flats = Flat.objects.prefetch_related('owner')

    for flat in flats:
        owner, _ = Owner.objects.get_or_create(
            owner=flat.owner,
            defaults={'owners_phonenumber': flat.owners_phonenumber}
        )
        owner.owned_property.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250204_2104'),
    ]

    operations = [
        migrations.RunPython(add_flat_to_owner)
    ]
