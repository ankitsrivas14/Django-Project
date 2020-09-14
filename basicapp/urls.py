from django.conf.urls import url
from basicapp import views
urlpatterns = [
    url('formpage',views.form_name_view,name='form_name'),
    url('',views.index,name='index'),

]
