from rest_framework import serializers
from delivery_absolute.models import Delivery, PackageType, ServiceType, Status, TransportModel
from delivery_absolute.serializers.handbook_serializers import PackageTypeSerializer, ServiceTypeSerializer, StatusSerializer, TransportModelSerializer

class DeliveryCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания доставки
    """
    # связь с типом упаковки
    package_type = serializers.PrimaryKeyRelatedField(
        queryset=PackageType.objects.all(),
        required=False
    )
    # связь с моделью транспорта
    transport_model = serializers.PrimaryKeyRelatedField(
        queryset=TransportModel.objects.all(),
        required=False
    )   
    # связь с типом услуги
    service_type = serializers.PrimaryKeyRelatedField(
        queryset=ServiceType.objects.all(),
        required=False
    )
    # связь со статусом доставки
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        required=False
    )

    class Meta:
        model = Delivery
        fields = [
            'transport_model',
            'package_type',
            'service_type',
            'status',
            'date_sending',
            'date_delivery',
            'distance',
            'file',
            'technical_condition'
        ]
        extra_kwargs = {
            'file': {'required': False},
        }

        def validate(self, data):
            # проверка даты доставки
            if data['date_sending'] and data['date_delivery']:
                if data['date_sending'] > data['date_delivery']:
                    raise serializers.ValidationError(
                        "Дата доставки не может быть раньше даты отправки"
                    )
            return data

    def to_internal_value(self, data):
        # преобразование объекта в id
        if 'package_type' in data and isinstance(data['package_type'], dict):
            data['package_type'] = data['package_type']['id']
        
        if 'transport_model' in data and isinstance(data['transport_model'], dict):
            data['transport_model'] = data['transport_model']['id']
            
        if 'service_type' in data and isinstance(data['service_type'], dict):
            data['service_type'] = data['service_type']['id']
            
        if 'status' in data and isinstance(data['status'], dict):
            data['status'] = data['status']['id']
            
        return super().to_internal_value(data)

class DeliveryListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка доставки
    """
    # связь с моделью транспорта
    transport_model = serializers.StringRelatedField()
    package_type = serializers.StringRelatedField()
    service_type = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    delivery_duration_hours = serializers.SerializerMethodField()
    
    class Meta:
        model = Delivery
        fields = '__all__'
        extra_fields = ['delivery_duration_hours']
    
    def get_delivery_duration_hours(self, obj):
        """Вычисляет разницу между датами в часах"""
        if obj.date_sending and obj.date_delivery:
            delta = obj.date_delivery - obj.date_sending
            return round(delta.total_seconds() / 3600, 2)  # Переводим секунды в часы
        return None

    def to_representation(self, instance):
        """Возвращаем вреия в пути, убираем даты отправки и доставки"""
        representation = super().to_representation(instance)
        
        # Удаляем оригинальные поля дат (опционально)
        representation.pop('date_sending', None)
        representation.pop('date_delivery', None)
        
        return representation
    
    
class DeliveryDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации о доставке по id
    """
    # связь с моделью транспорта
    transport_model = TransportModelSerializer()
    package_type = PackageTypeSerializer()
    service_type = ServiceTypeSerializer()
    status = StatusSerializer()
    delivery_duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Delivery
        fields = [
            'id',
            'transport_model',
            'package_type',
            'service_type',
            'status',
            'date_sending',
            'date_delivery',
            'delivery_duration',
            'distance',
            'file',
            'technical_condition',
            'created_at',
            'updated_at'
        ]
    
    def get_delivery_duration(self, obj):
        """Вычисляет разницу между датами в часах"""
        if obj.date_sending and obj.date_delivery:
            delta = obj.date_delivery - obj.date_sending
            return round(delta.total_seconds() / 3600, 2)
        return None