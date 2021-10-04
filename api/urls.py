from django.urls.conf import include, path

urlpatterns = [
	path('todo/', include('api.todo.urls')),
	path('subtask/', include('api.subtask.urls')),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
