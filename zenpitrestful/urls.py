from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# use api.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('api.urls'))
]
