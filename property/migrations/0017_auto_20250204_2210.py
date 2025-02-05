from django.db import migrations


def clear_owned_property(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    for owner in Owner.objects.all():
        owner.owned_property.clear()
        owner.save()

    # Удаляем все записи из таблицы owned_property
    with schema_editor.connection.cursor() as cursor:
        cursor.execute('DELETE FROM property_owner_owned_property;')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20250204_2203'),
    ]

    operations = [
        migrations.RunPython(clear_owned_property)
    ]
