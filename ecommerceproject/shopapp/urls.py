from . import views
from django.urls import path


app_name ='shopapp'


urlpatterns = [
    path('', views.AllProductCat, name='AllProductCat'),
    path('<slug:c_slug>/', views.AllProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Prodetails, name='ProdCatDetail')

]