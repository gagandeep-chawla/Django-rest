from django.urls import path,include
from polls import views

urlpatterns = [
	# polls requset
	path('polls/',views.poll,name= 'polls'),
	path('polls/<int:pk>',views.poll_details,name = 'poll_details'),
	# practice_model request
	path('practice_model_create/',views.create_practice_model_instance,
		name = 'create_practice_model_instance')
]