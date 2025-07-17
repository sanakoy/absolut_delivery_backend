from rest_framework.exceptions import APIException

class DeliveryNotFound(APIException):
    """Исключение для случая, когда доставка не найдена"""
    detail = "Ничего не найдено"
    status_code = 404
    default_detail = 'Доставка не найдена'
    default_code = 'delivery_not_found'

class InvalidDeliveryData(APIException):
    """Исключение для случая, когда данные доставки некорректны"""
    status_code = 400
    default_detail = 'Некорректные данные доставки'
    default_code = 'invalid_delivery_data'