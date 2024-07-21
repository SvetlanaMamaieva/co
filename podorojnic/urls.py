from django.urls import path
from  . import views
app_name = 'podorojnic'
urlpatterns = [
    path('', views.index, name='index'),

    path('directions', views.directions, name='directions'),
    path('directions/<int:direction_id>', views.direction, name='direction'),
    path('new_direction', views.new_direction, name='new_direction'),

    path('new_entry/<int:direction_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),

    path('best_co', views.best_co, name='best_co'),

    path('simple_form', views.simple_from_view, name='simple_form'),



]