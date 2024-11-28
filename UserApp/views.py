import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json

def Home (request):
    return render(
        request,
        'main.html',
    )
