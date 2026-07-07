from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer

TASK_LIST_CACHE_KEY = 'task_list'
TASK_LIST_CACHE_TIMEOUT = 60  # секунды


class TaskListAPIView(APIView):
    """GET — список задач, POST — создание задачи."""

    def get(self, request):
        cached = cache.get(TASK_LIST_CACHE_KEY)
        if cached is not None:
            return Response(cached, status=status.HTTP_200_OK)

        tasks = Task.objects.only(
            'id', 'title', 'priority', 'is_completed',
        ).order_by('-created_at')

        serializer = TaskListSerializer(tasks, many=True)
        cache.set(TASK_LIST_CACHE_KEY, serializer.data, TASK_LIST_CACHE_TIMEOUT)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(TASK_LIST_CACHE_KEY)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    """GET / PUT / PATCH / DELETE для одной задачи."""

    def _get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self._get_object(pk)
        if task is None:
            return Response(
                {"detail": "Задача не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self._get_object(pk)
        if task is None:
            return Response(
                {"detail": "Задача не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(TASK_LIST_CACHE_KEY)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        task = self._get_object(pk)
        if task is None:
            return Response(
                {"detail": "Задача не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete(TASK_LIST_CACHE_KEY)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self._get_object(pk)
        if task is None:
            return Response(
                {"detail": "Задача не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
        task.delete()
        cache.delete(TASK_LIST_CACHE_KEY)
        return Response(status=status.HTTP_204_NO_CONTENT)
