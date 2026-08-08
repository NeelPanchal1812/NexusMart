from django.contrib import admin
from django.urls import path, include

from django.conf import settings          # ✅ ADD
from django.conf.urls.static import static # ✅ ADD

urlpatterns = [
    path('', include('products.urls')),
    path('', include('users.urls')),   # 
    path('orders/', include('orders.urls')),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
    path("analytics/", include("analytics_app.urls")),
    path('chatbot/', include('chatbot.urls')),

]


# ✅ SERVE MEDIA AND STATIC FILES IN DEV MODE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
