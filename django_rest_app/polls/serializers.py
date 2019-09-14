from rest_framework import serializers
from polls.models import Question,PracticeModel

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = [
			'title',
			'status',
			'created_by'
		]

class PracticeModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = PracticeModel
		exclude = ('id',)

	def create(self,validate_data):
		question_instances = validate_data.pop('question')
		practice_model_instance = PracticeModel.objects.create(**validate_data)
		for question in question_instances:
			practice_model_instance.question.add(question)
		return practice_model_instance