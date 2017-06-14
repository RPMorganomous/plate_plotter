from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from plot_app.views import profile

urlpatterns = [
                  url(r'^', include('plot_app.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^accounts/', include('registration.backends.simple.urls')),
                  url(r'^accounts/profile/$', profile, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
