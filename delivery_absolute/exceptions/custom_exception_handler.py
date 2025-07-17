from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Логируем ошибку
    logger.error(f"Ошибка: {str(exc)}", exc_info=True)
    
    # Стандартная обработка DRF
    response = exception_handler(exc, context)
    
    if response is None:
        # Для необработанных исключений
        if isinstance(exc, ObjectDoesNotExist):
            response_data = {'error': 'Объект не существует'}
            status_code = status.HTTP_404_NOT_FOUND
        elif isinstance(exc, DatabaseError):
            response_data = {'error': 'Ошибка базы данных'}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            response_data = {'error': 'Произошла непредвиденная ошибка'}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        
        response = Response(response_data, status=status_code)
    else:
        # Для уже обработанных DRF исключений
        if isinstance(exc, (ValidationError, PermissionDenied)):
            response.data = {'error': str(exc)}
        elif isinstance(exc, NotFound):
            response.data = {'error': 'Ресурс не найден'}
    
    return response