from django.contrib import admin
from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='FLOW API')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('flow.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^docs/', schema_view),
]
