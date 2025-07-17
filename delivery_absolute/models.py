from django.db import models

from delivery_absolute.enums import TechnicalCondition

# Модель транспорта

class TransportModel(models.Model):
    """
    Справочник моделей транспорта
    """
    name = models.CharField(
        verbose_name='Номер модели',
        max_length=15,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Модель транспорта'
        verbose_name_plural = 'Модели транспорта'
        ordering = ['name']

    def __str__(self):
        return self.name


class PackageType(models.Model):
    """
    Типы упаковки
    """
    name = models.CharField(
        verbose_name='Тип упаковки',
        max_length=100,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Тип упаковки'
        verbose_name_plural = 'Типы упаковки'
        ordering = ['name']

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    """
    Услуга
    """
    name = models.CharField(
        verbose_name='Услуга',
        max_length=100,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return self.name



class Status(models.Model):
    """
    Статус доставки
    """
    name = models.CharField(
        verbose_name='Статус доставки',
        max_length=100,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Статус доставки'
        verbose_name_plural = 'Статусы доставок'
        ordering = ['name']

    def __str__(self):
        return self.name


class Delivery(models.Model):
    """
    Доставка
    """
    transport_model = models.ForeignKey(
        TransportModel,
        verbose_name='Модель транспорта',
        on_delete=models.RESTRICT
    )
    package_type = models.ForeignKey(
        PackageType,
        verbose_name='Тип упаковки',
        on_delete=models.RESTRICT
    )
    service_type = models.ForeignKey(
        ServiceType,
        verbose_name='Услуга',
        on_delete=models.RESTRICT
    )
    status = models.ForeignKey(
        Status,
        verbose_name='Статус доставки',
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    date_sending = models.DateTimeField(
        verbose_name='Дата отправки',
        null=True,
        blank=True
    )
    date_delivery = models.DateTimeField(
        verbose_name='Дата доставки',
        null=True,
        blank=True
    )
    distance = models.FloatField(
        verbose_name='Расстояние',
        null=True,
        blank=True
    )
    file = models.FileField(
        verbose_name='Файл',
        upload_to='delivery/',
        null=True,
        blank=True
    )
    technical_condition = models.CharField(
        verbose_name='Техническое состояние',
        max_length=20,
        choices=TechnicalCondition.choices(),
        default=None,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.transport_model} - {self.package_type} - {self.service_type} - {self.status}'

