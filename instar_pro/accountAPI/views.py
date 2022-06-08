import email
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def auth(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        obj = Account.objects.create(data)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            try: 
                Account.objects.get(name=serializer['name'])
            except Account.MultipleObjectsReturned:
                return JsonResponse(status=400)
                
        


@csrf_exempt
def account(request, pk):

    obj = Account.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = Account.objects.get(email=search_email)

        if data['password'] == obj.password:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)