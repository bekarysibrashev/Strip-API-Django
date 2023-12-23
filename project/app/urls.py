from django.urls import path
from .views import *

urlpatterns = [
    path('', AllItem.as_view(), name='all'),
    path('item/<int:id>/', ItemInfo.as_view(), name='item'),
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy'),
    path('success/<int:item_id>/', Success.as_view(), name='success'),
    path('cancel/<int:item_id>/', Cancel.as_view(), name='cancel'),
    # path('add/<int:id>/', AddView.as_view(), name='add')
]