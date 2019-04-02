# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from pandas._libs import json
from rest_framework.decorators import api_view
from regres.regr import pred


@api_view(['POST'])
def lol(request):
    body_unicode = request.body.decode('utf-8')
    json_otv = json.loads(body_unicode)
    mass = [json_otv["SQUARE"],json_otv["RM"],json_otv["NOX"]]

    kek = {"value": pred(mass)}
    return HttpResponse(json.dumps(kek), content_type='application/json')


def buba(request):
    return render(request, "lol.html")
