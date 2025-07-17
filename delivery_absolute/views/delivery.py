from rest_framework import viewsets, status
from rest_framework.response import Response

from delivery_absolute.exceptions.custom_exceptions import DeliveryNotFound
from ..models import Delivery
from rest_framework.decorators import api_view, permission_classes
from ..serializers.delivery_serializer import DeliveryCreateSerializer, DeliveryListSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from ..serializers.delivery_serializer import DeliveryDetailSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с доставками
    """
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        # получение сериализатора в зависимости от действия
        return DeliveryCreateSerializer if self.action in ['create', 'update', 'partial_update'] else DeliveryListSerializer

    def get_queryset(self):
        # получение queryset в зависимости от query параметров
        queryset = Delivery.objects.select_related(
                'transport_model',
                'package_type',
                'service_type',
                'status'
            ).all().order_by('-created_at')

        # фильтрация queryset в зависимости от query параметров
        service_type = self.request.query_params.get('service_type')
        date_delivery = self.request.query_params.get('date_delivery')
        if service_type:
            queryset = queryset.filter(service_type__id=service_type)
        if date_delivery:
            queryset = queryset.filter(date_delivery__lte=date_delivery)

        return queryset

    def create(self, request, *args, **kwargs):
        # создание доставки
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            DeliveryListSerializer(instance=serializer.instance).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, *args, **kwargs):
        # частичное обновление доставки
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
            
        return Response(DeliveryDetailSerializer(instance).data)


    def destroy(self, request, *args, **kwargs):
        # удаление доставки
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Доставка успешно удалена'},
            status=status.HTTP_204_NO_CONTENT
        )


    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        # получение детальной информации о доставке по id
        try:
            delivery = Delivery.objects.get(pk=pk)
            serializer = DeliveryDetailSerializer(delivery)
            return Response(serializer.data)
        except Delivery.DoesNotExist:
            raise DeliveryNotFound()
