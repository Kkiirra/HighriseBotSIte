from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BotModerator, HighrisePlayers
from .serializers import BotModeratorSerializer, HighrisePlayersSerializer
from .csrf import CsrfExemptSessionAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class BotModeratorGet(APIView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request):
        data_from_request = request.data
        api_key = data_from_request.get('api_key', None)

        if api_key is not None:
            try:
                queryset = BotModerator.objects.get(api_key=api_key.strip())
            except ObjectDoesNotExist:
                return Response({'error': 'Неверный API ключ'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = BotModeratorSerializer(queryset)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        else:
            Response({'error': 'API ключ не был предоставлен'},
                     status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        api_key = request.data.get('api_key')
        print(request.data)
        if api_key is None:
            return Response({'error': 'API ключ не был предоставлен'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                moderator = BotModerator.objects.get(api_key=api_key)
            except BotModerator.DoesNotExist:
                return Response({'error': 'Неверный API ключ'},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = BotModeratorSerializer(moderator, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        api_key = request.query_params.get('api_key')
        word = request.query_params.get('word')
        field_name = request.query_params.get('field')

        if not all([api_key, word, field_name]):
            return Response({'error': 'Необходимо предоставить API ключ, слово и имя поля.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            moderator = BotModerator.objects.get(api_key=api_key)
        except BotModerator.DoesNotExist:
            return Response({'error': 'Неверный API ключ'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = BotModeratorSerializer()
        try:
            serializer.remove_word(moderator, word, field_name)
            return Response({'message': 'Слово удалено успешно.'},
                            status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class BotModeratorCreate(APIView):
    pass


class HighrisePlayersAPI(APIView):

    def get(self, request):
        username = request.query_params.get('username', None)
        user_id = request.query_params.get('user_id', None)

        if username is not None and user_id is not None:
            queryset = HighrisePlayers.objects.filter(username=username, user_id=user_id)
        else:
            queryset = HighrisePlayers.objects.all()

        serializer = HighrisePlayersSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = HighrisePlayersSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({'error': 'Пользователь с такими данными уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
