
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('job/', include('job.urls')),
    path('admin/', admin.site.urls),
]
