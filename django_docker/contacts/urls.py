from django.conf.urls import url
from . import views as contact_views

urlpatterns = [
    url(r'^$', contact_views.contact, name="contact_us"),
]
