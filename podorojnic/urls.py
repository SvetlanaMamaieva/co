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

    path('countries', views.countries, name='countries'),
    path('new_country/', views.new_country, name='new_country'),
    path('countries/<int:country_id>', views.country, name='country'),
    path('new_info/<int:country_id>', views.new_info, name='new_info')


]