from django.urls import path, include
from rest_framework import routers

from employee import views

router = routers.DefaultRouter()
router.register('',views.EmployeeViewset)

urlpatterns = [
	path('employee/',include(router.urls))
	# its not correct right now
	# path('crud_api/',views.EmployeeViewset.as_view({'get':'list'}),name = 'crud_api')
]