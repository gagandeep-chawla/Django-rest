from rest_framework import serializers
from django.contrib.auth.models import USER

class EmployeeSerializer(serializers.HyperLinkedModelSerializer):
	class Meta:
		model = User
		fields = ('first_name',
			'last_name',
			'email',
			'url'
		)
