from django.urls import path
from backend.api import views

urlpatterns = [
    path("items/",views.ListItemView.as_view(),name="list-items"),
    path("items/<int:pk>/", views.RetrieveItemView.as_view(), name="detail-item"),

]
