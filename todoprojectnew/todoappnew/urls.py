from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvlv/',views.listview.as_view(),name='cbvlv'),
    path('detailv/<int:pk>/',views.detailview.as_view(),name='detailv'),
    path('updatev/<int:pk>/',views.updateview.as_view(),name='updatev'),
    path('deletev/<int:pk>/',views.deleteview.as_view(),name='deletev')

]