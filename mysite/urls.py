from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static, settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^accounts/login/$', views.login, name='login'),
	url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
	url(r'', include('blog.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


