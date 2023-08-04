from django.urls import path
from . import views

urlpatterns = [

    path('',views.employeeFormView, name='formshow'),
    path('data_show/',views.employeeshowdata, name='datashow'),
    path('data_update/<int:id>',views.employeeDataUpdate, name='dataupdate'),
    path('data_del/<int:id>',views.employeeDataDel, name='datadelete'),
]
