from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('modules.user.urls')),
    path("api/v1/", include("modules.home.urls")),
    path("api/v1/", include("modules.questions.urls")),
    path("api/v1/", include("modules.reqs_to_company.urls")),
    path("api/v1/", include("modules.votes.urls")),
    path("api/v1/", include("modules.events.urls")),
    path("api/v1/", include("modules.documents.urls")),
    path("api/v1/", include("modules.news.urls")),
    path("api/v1/", include("modules.user.user_urls")),
    path("api/v1/", include("modules.company.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
