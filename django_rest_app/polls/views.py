from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers  import JSONParser
# its will skip the csrf token validation
from django.views.decorators.csrf import csrf_exempt

from polls.models import Question,PracticeModel
from polls.serializers import QuestionSerializer,PracticeModelSerializer 
# Create your views here.

@csrf_exempt
def poll(request):
	if request.method == 'GET':
		questions = Question.objects.all()
		serializer = QuestionSerializer(questions,many =True)
		return JsonResponse(serializer.data,safe = False)
	elif request.method == 'POST':
		json_parser =JSONParser()
		data = json_parser.parse(request)
		serializer = QuestionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status = 201)
		return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def poll_details(request,pk):
	try:
		instance = Question.objects.get(id = pk)
	except Question.DoesNotExist as e:
		return JsonResponse({'error':'Question objects is DoseNotExist'},status = 404)

	if request.method == 'GET':
		serializer = QuestionSerializer(instance = instance)
		return JsonResponse(serializer.data,status = 200)

	if request.method == 'PUT':
		json_parser = JSONParser()
		data = json_parser	.parse(request)
		serializer = QuestionSerializer(instance,data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status = 200)
		return JsonResponse(serializer.errors ,status = 400)

	if request.method == 'DELETE':
		instance.delete()
		return JsonResponse({'messgae':'Objects is delete'},status = 204)

@csrf_exempt
def create_practice_model_instance(request):
	
	if request.method == 'GET':
		practice_model_instance = PracticeModel.objects.all()
		serializer = PracticeModelSerializer(practice_model_instance,many = True)
		return JsonResponse(serializer.data ,safe = False) 
	
	if request.method == 'POST':
		json_parser = JSONParser()
		data = json_parser.parse(request)
		serializer = PracticeModelSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		else:
			return JsonResponse(serializer.errors)