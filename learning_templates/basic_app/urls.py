from django.urls import path,include
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('other',views.other,name='other'),
    path('relative_url_template',views.relative_url_template,name='relative_url_template'),
]
