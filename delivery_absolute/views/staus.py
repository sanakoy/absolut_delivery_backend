from rest_framework import viewsets
from ..models import Status
from ..serializers.handbook_serializers import StatusSerializer
from rest_framework.permissions import IsAuthenticated


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Эндпоинт для получения списка всех статусов доставки
    Возвращает id и name каждого статуса
    """
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
