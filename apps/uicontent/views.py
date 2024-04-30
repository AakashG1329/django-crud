from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.uicontent.models import Uicontent
from apps.uicontent.serializer import UicontentSerializer
# Create your views here.
class uicontentGetAll(APIView):
    def get_queryset(self):
        return Uicontent.objects.all().order_by('id')
    def get(self,request):
        try:
            queryset = self.get_queryset() 
            serializer = UicontentSerializer(queryset, many=True)
            msg = {'code': status.HTTP_200_OK, 'msg': 'Datas Get Successfully', 'data': serializer.data,}
            return Response(msg, status=status.HTTP_200_OK)
        except Uicontent.DoesNotExist:
            msg={'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Data Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        