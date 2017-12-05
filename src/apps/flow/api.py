import logging

from django_fsm import TransitionNotAllowed
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from src.constants import API_RESPONSE
from .models import Order
from .serializer import FlowSerializer

logger = logging.getLogger(__name__)


def exception_handler(function, *args, **kwargs):
    def method_handler(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except TransitionNotAllowed:
            logger.error('Transition Not allowed')
            API_RESPONSE['message'] = 'Transition Not Allowed'
            API_RESPONSE['success'] = False
            return Response(API_RESPONSE, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            logger.error('Order Not Found')
            API_RESPONSE['message'] = 'Order Not Found'
            API_RESPONSE['success'] = False
            return Response(API_RESPONSE, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(repr(e))
            API_RESPONSE['message'] = repr(e)
            API_RESPONSE['success'] = False
            return Response(API_RESPONSE, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return method_handler


class FlowBaseView(CreateAPIView):
    model = Order
    serializer_class = FlowSerializer

    def process_data(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        order_obj = self.model.objects.get(awb=serializer.data.get('awb'))
        return order_obj


class CreateView(FlowBaseView):
    """
    Creating/uploading an order in the workflow system

    Payload:
    ```
    {
         "awb": "air waybill number",
    }
    ```
    Response:
    ```
    {
        "data": {},
        "success": True,
        "message": "Successful"
    }
    ```
    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        requested_data = request.data
        serializer = self.get_serializer(data=requested_data)
        serializer.is_valid(raise_exception=True)
        order_obj = self.model(awb=serializer.data.get('awb'))
        order_obj.save()
        logger.info('Created Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class PickView(FlowBaseView):
    """
        Picking an Order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```

    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.pick()
        order_obj.save()
        logger.info('Picked Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class ReceiveView(FlowBaseView):
    """
        Receiving an order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```

    """

    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.receive()
        order_obj.save()
        logger.info('Received Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class ShelveView(FlowBaseView):
    """
        Shelving an order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```

    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.shelve()
        order_obj.save()
        logger.info('Shelved Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class ReadyToDispatchView(FlowBaseView):
    """
        Ready to dispatch an order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```

    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.ready_to_dispatch()
        order_obj.save()
        logger.info('Ready to dispatched Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class DispatchView(FlowBaseView):
    """
        Dispatching an order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```
    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.dispatch()
        order_obj.save()
        logger.info('Dispatched Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)


class DeliverView(FlowBaseView):
    """
        Delivering an order

        Payload:
        ```
        {
             "awb": "air waybill number",
        }
        ```
        Response:
        ```
        {
            "data": {},
            "success": True,
            "message": "Successful"
        }
        ```

    """

    @exception_handler
    def post(self, request, *args, **kwargs):
        order_obj = self.process_data(request.data)
        response = order_obj.deliver()
        order_obj.save()
        logger.info('Delivered Successfully awb: {}'.format(order_obj.awb))
        return Response(API_RESPONSE, status=status.HTTP_200_OK)
