from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Assignment
from .serializers import *


@api_view(['GET'])
def get_assigments(request):
    ass = Assignment.objects.all()
    serDat = WorkSerializers(ass, many=True).data
    serDat = list(serDat)
    serDat.sort(key=lambda item: item["subject"])
    dat = {}
    dat_ = {"None":[]}
    # return Response(serDat)
    for data in serDat:
        if data["date"] == None:
            dat_["None"].append(data)
            continue
        try:
            dat[data["date"]].append(data)
        except Exception:
            dat[data["date"]] = [data]

    dat = dict(sorted(dat.items()))

    return Response([len(serDat) == 0, (dat_ if len(dat_["None"]) > 0 else {}) | dat])