from django.conf.urls import url, patterns, include
from .views import CategoryList, DesignerList, ProductList

urlpatterns = patterns('',
                       url(r'api/v1/categories/', CategoryList.as_view(), name='category_api'),
                       url(r'api/v1/designer', DesignerList.as_view(), name='designer_api'),
                       url(r'api/v1/products/', ProductList.as_view(), name="product_api"),
)