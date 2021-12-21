from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from taskApp.models import Task
from taskApp.serializers import TaskSerializers

# Create your views here.


@csrf_exempt

def taskApi(request, id=0):

    # Metodo get Leer
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializers = TaskSerializers(tasks, many=True)
        return JsonResponse(tasks_serializers.data, safe=False)

    # Metodo Post - Add.
    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        tasks_serializers=TaskSerializers(data=task_data)
        if tasks_serializers.is_valid():
            tasks_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

        #Metodo Put - Update.
    elif request.method=='PUT':
        task_data=JSONParser().parse(request)
        tasks=Task.objects.get(TaskId=task_data['TaskId'])
        tasks_serializers=TaskSerializers(tasks,data=task_data)
        if tasks_serializers.is_valid():
            tasks_serializers.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

        #Metodo Delete.
    elif request.method == 'DELETE':
        task = Task.objects.get(TaskId=id)
        task.delete()
        return JsonResponse("Delete successfully.", safe=False)