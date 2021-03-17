from django.urls import path, include

app_name = 'api_v1'

urlpatterns = [
    path('cources/', include('api.v1.cources.urls')),
    path('events/', include('api.v1.events.urls')),
    path('marks/', include('api.v1.marks.urls')),
    path('users/', include('api.v1.users.urls')),
]