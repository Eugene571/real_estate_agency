from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField(
        'Текст объявления',
        blank=True)
    price = models.IntegerField(
        'Цена квартиры',
        db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField(
        'Наличие балкона',
        null=True,
        db_index=True)
    active = models.BooleanField(
        'Активно-ли объявление',
        db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField(
        verbose_name='Новостройка',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Кто лайкнул',
        related_name='liked_flats',
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


@receiver(pre_save, sender=Flat)
def set_new_building(sender, instance, **kwargs):
    if instance.construction_year and instance.construction_year > 2014:
        instance.new_building = True
    else:
        instance.new_building = False


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался',
        related_name='complaints')
    flat = models.ForeignKey(
        'property.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую жаловались',
        related_name='complaints')
    message = models.TextField(
        'Текст жалобы',
        help_text='Опишите вашу жалобу')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')

    def __str__(self):
        return f'Жалоба от {self.user.username} на {self.flat.address}'


class Owner(models.Model):
    fio = models.CharField(
        "ФИО владельца",
        max_length=200,
        db_index=True)
    phonenum = models.CharField(
        "Номер владельца",
        max_length=20,
        db_index=True)
    phonenum_pure = PhoneNumberField(
        "Нормализованный номер владельца",
        blank=True,
        db_index=True)
    properties = models.ManyToManyField(
        Flat,
        blank=True,
        verbose_name='Квартиры в собственности',
        related_name='owners')

    def __str__(self):
        return self.fio
