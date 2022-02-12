# Обновлённый views.py
from curses.ascii import RS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Cat
from .serializers import CatSerializer


class APICAT(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# через вью-функцию
# @api_view(['GET', 'POST'])
#def cat_list(request):
#    if request.method == 'POST':
#        serializer = CatSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    cats = Cat.objects.all()
#    serializer = CatSerializer(cats, many=True)
#    return Response(serializer.data)
