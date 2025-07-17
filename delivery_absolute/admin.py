from django.contrib import admin

from delivery_absolute.models import TransportModel, PackageType, ServiceType, Status, Delivery

# Регистрация моделей в админке

@admin.register(TransportModel)
class TransportModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    
@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('transport_model', 'package_type', 'service_type', 'status', 'created_at', 'updated_at', 'date_sending', 'date_delivery', 'distance', 'file', 'technical_condition')
    search_fields = ('transport_model', 'package_type', 'service_type', 'status', 'created_at', 'updated_at', 'date_sending', 'date_delivery', 'distance', 'file', 'technical_condition')

