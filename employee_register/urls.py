
from django.urls import path, include
from . import views

urlpatterns = [
    # for insert operation
    path('add-employee/', views.employee_form, name='employee_insert'),
    # for updte operation
    path('<int:id>/', views.employee_form, name='employee_update'),
    #for display operation
    path('', views.employee_list, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
