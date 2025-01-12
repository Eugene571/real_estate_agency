from django.db import migrations


def transfer_owners_to_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner_name = flat.owner
        owner_phone = flat.owners_phonenumber
        normalized_phone = flat.owner_pure_phone

        # Создаем или получаем существующего собственника
        owner, created = Owner.objects.get_or_create(
            name=owner_name,
            phone_number=owner_phone,
            defaults={'normalized_phone': normalized_phone}
        )

        # Логирование
        if created:
            print(f"Создан новый собственник: {owner_name}")
        else:
            print(f"Существующий собственник обновлен: {owner_name}")


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250112_2045'),  # Укажите предыдущую миграцию
    ]

    operations = [
        migrations.RunPython(transfer_owners_to_model),
    ]
