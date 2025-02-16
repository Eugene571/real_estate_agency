# Generated by Django 2.2.24 on 2025-02-04 18:27

from django.db import migrations


def clear_owned_property(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    # Очищаем связи для всех владельцев за один запрос
    Owner._default_manager.update(owned_property=None)


class Migration(migrations.Migration):
    def fill_owners(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')

        for flat in Flat.objects.all().iterator():
            owner, created = Owner.objects.get_or_create(
                owner=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                defaults={
                    'owner_phone_pure': flat.owner_pure_phone
                }
            )
            owner.owned_property.add(flat)
            owner.save()

    dependencies = [
        ('property', '0014_auto_20250204_2118'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
