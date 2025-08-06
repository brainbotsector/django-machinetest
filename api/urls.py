from django.urls import path
from .views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroyView,
    ProjectCreateView,
    UserProjectListView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('clients/<int:id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectListView.as_view(), name='user-projects'),
]