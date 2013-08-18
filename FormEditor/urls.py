from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns("editor",
	url(r"^$", "FormEditor.views.home", name="home"),  # TODO
	url(r"^editor/form/new$", TemplateView.as_view(template_name="editor.html")),
#	url(r"^editor/", include("editor.urls")),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
)
