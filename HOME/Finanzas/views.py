from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from Finanzas.models import Variable, VariableMeasure
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


from rest_framework import permissions
from Finanzas.serializers import UserSerializer, GroupSerializer, VariableSerializer, VariableMeasureSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class VariableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows process variables to be viewed or edited.
    """
    queryset = Variable.objects.all()
    print(queryset)
    serializer_class = VariableSerializer
    permission_classes = [permissions.IsAuthenticated]

class VarMeasureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows process variables to be viewed or edited.
    """
    queryset = VariableMeasure.objects.all()
    serializer_class = VariableMeasureSerializer
    # permission_classes = [permissions.IsAuthenticated]
@api_view(['GET'])
def BankView(request):

    if request.method == 'GET':

        print('insideBank class')
        return Response({'a':1})