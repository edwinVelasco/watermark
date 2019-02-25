# Create your views here.
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from api.util.mixins import ValidateToken
from .models import Document
from .serializer import DocumentSerializer


class TestToken(ValidateToken, APIView):
    def get(self, request):
        return Response({'msg': 'Prueba de token GET OK', 'code': 200},
                        status=200)

    def post(self, request):
        return Response({'msg': 'Prueba de token POST OK', 'code': 200},
                        status=200)

    def put(self, request):
        return Response({'msg': 'Prueba de token PUT OK', 'code': 200},
                        status=200)


# Example views
class Docs(APIView):
    def get(self, request):
        docs = Document.objects.get(id=request.data)
        docs_json = DocumentSerializer(docs, many=False)
        return Response(docs_json.data)

    def post(self, request):
        docs_json = DocumentSerializer(data=request.data)
        if docs_json.is_valid():
            docs_json.save()
            return Response(docs_json.data, status=201)
        return Response(docs_json.errors, status=400)


class DetailDocs(APIView):
    def get_object(self, pk):
        try:
            return Document.objects.get(id=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        docs = self.get_object(pk)
        docs_json = DocumentSerializer(docs) #UnMarshall
        return Response(docs_json.data)

    def put(self, request, pk):
        docs = self.get_object(pk)
        docs_json = DocumentSerializer(docs, data=request.data)
        if docs_json.is_valid():
            docs_json.save()
            return Response(docs_json.data)
        return Response(docs_json.errors, status=400)

    def delete(self, request, pk):
        docs = self.get_object(pk)
        docs.delete()
        return Response(status=204)
