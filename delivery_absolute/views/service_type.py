from rest_framework import viewsets
from ..models import ServiceType
from ..serializers.handbook_serializers import ServiceTypeSerializer
from rest_framework.permissions import IsAuthenticated


class ServiceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Эндпоинт для получения списка всех типов услуг
    Возвращает id и name каждого типа
    """
    permission_classes = [IsAuthenticated]
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
