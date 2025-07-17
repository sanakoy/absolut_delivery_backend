from rest_framework import viewsets
from ..models import PackageType
from ..serializers.handbook_serializers import PackageTypeSerializer
from rest_framework.permissions import IsAuthenticated


class PackageTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Эндпоинт для получения списка всех типов упаковки
    Возвращает id и name каждого типа
    """
    permission_classes = [IsAuthenticated]
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeSerializer
