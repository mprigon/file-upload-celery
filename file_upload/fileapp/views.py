from functools import partial
from pathlib import Path

from django.db import transaction

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .serializers import FileSerializer, FileCreateSerializer
from .models import File

from file_upload.tasks import load_file


class FileAPICreate(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileCreateSerializer

    def post(self, request, *args, **kwargs):
        print('post in FileAPICreate started')
        serializer_class = self.serializer_class
        print('post received request.data: ', request.data, type(request.data))
        print('post received serializer_class: ', serializer_class, type(serializer_class))
        serializer = self.serializer_class(data=request.data)
        print('in post serializer.is_valid: ', serializer.is_valid())
        if serializer.is_valid():
            file = serializer.save()
            print('file object created by calling save() in post')
            print('id: ', file.id, 'type: ', type(file))
            print('object from DB', File.objects.get(id=file.id))
            print('from post in FileAPICreate: file loaded, starting celery task')
            """Здесь можно прочитать по id, а из celery - не удается, проблема известная"""
            # transaction.on_commit(partial(load_file.delay, file_id=file.id))
            transaction.on_commit(lambda: load_file.delay(file.id))
            print('from post in FileAPICreate: check-point just after celery started')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileAPIList(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
