# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from pandas._libs import json

from regres.regr import pred


def lol(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        json_otv = json.loads(body_unicode)
        mass = []
        for val in dict.values(json_otv):
            mass.append(val)
        kek = {"value": pred(mass)}
        return HttpResponse(json.dumps(kek), content_type='application/json')


def buba(request):
    return render(request, "lol.html")
