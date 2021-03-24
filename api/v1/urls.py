from django.urls import path, include

app_name = 'api_v1'

urlpatterns = [
    path('cource/', include('api.v1.cources.urls')),
    path('event/', include('api.v1.events.urls')),
    path('mark/', include('api.v1.marks.urls')),
    path('user/', include('api.v1.users.urls')),
]