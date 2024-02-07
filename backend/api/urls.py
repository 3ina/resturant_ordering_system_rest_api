from django.urls import path
from backend.api import views

urlpatterns = [
    path("order/",views.CreateListOrder.as_view()
         ,name="list-orders"),
    path("order/<int:pk>/",views.OrderDetail.as_view()
         ,name="detail-order"),
    path("order/<int:pk>/createPayment",views.CreatePayment.as_view()
         ,name="detail-order"),
    path("order/<int:pk>/createOrderItem",views.CreateOrderItem.as_view()
         ,name="create-list-orderItem"),
    path("items/",views.ListItemView.as_view()
         ,name="list-items"),
    path("items/<int:pk>/", views.RetrieveItemView.as_view()
         , name="detail-item"),
    path("category/",views.ListCategoryView.as_view()
         ,name="list-categories"),
    path("category/<int:pk>/", views.RetrieveCategoryView.as_view()
         , name="detail-category"),
    path("admin/items/",views.CreateListItemView.as_view()
         ,name='admin-create-item'),
    path("admin/items/<int:pk>/",views.RetrieveUpdateDeleteItem.as_view()
         ,name='admin-detail-item'),
    path("admin/category/",views.CreateListCategoryView.as_view()
         ,name='admin-create-category'),
    path("admin/category/<int:pk>/",views.RetrieveUpdateDeleteCategory.as_view()
         ,name='admin-detail-category'),
]
