from rest_framework import viewsets
from ..models import TransportModel
from ..serializers.handbook_serializers import TransportModelSerializer
from rest_framework.permissions import IsAuthenticated


class TransportModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Эндпоинт для получения списка всех моделей транспорта
    Возвращает id и name каждой модели
    """
    permission_classes = [IsAuthenticated]
    queryset = TransportModel.objects.all()
    serializer_class = TransportModelSerializer
