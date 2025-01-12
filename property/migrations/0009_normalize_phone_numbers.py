from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    # Временно фильтруем только одну запись для отладки
    flats = Flat.objects.filter(owners_phonenumber='+70000000000')  # Удалите фильтр после тестирования

    for flat in flats:
        try:
            # Парсим номер
            parsed_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
            if phonenumbers.is_valid_number(parsed_number):
                # Если номер валиден, форматируем в E164
                formatted_phone = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.E164
                )
            else:
                # Если номер невалиден
                formatted_phone = None
        except phonenumbers.NumberParseException:
            # Если номер не удалось разобрать
            formatted_phone = None

        # Обновляем только поле owner_pure_phone
        Flat.objects.filter(id=flat.id).update(owner_pure_phone=formatted_phone)



class Migration(migrations.Migration):

    dependencies = [
        # Укажите зависимости (последнюю миграцию вашего приложения)
        ('property', '0008_auto_20250112_2045'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
