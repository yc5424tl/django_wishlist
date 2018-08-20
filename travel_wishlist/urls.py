from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.places_visited, name='places_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
]

# Regular expression to match the exact path visited.
# ^ matches the start of a word, $ matches the end.
# Without these, r'visited' would match routes like
# visitedplaces and allplacesvisited and any other path with 'visited' in.
