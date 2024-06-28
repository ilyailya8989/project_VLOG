from django.urls import path

from v_app import views

urlpatterns = [
 path('info_category', views.info_category, name='info_category'),
 path('info_post_about_cat/<int:cat_id>/', views.info_post_about_cat, name='info_post_about_cat'),
 path('add_category', views.add_category, name='add_category'),
 path('del_category/<int:cat_id>', views.del_category, name='del_category'),


 path('info_category/avtor/<int:author_id>', views.info_post_about_avtor, name='info_post_about_avtor'),
 path('add_avtor', views.add_avtor, name='add_avtor'),
 path('del_avtor/<int:author_id>', views.del_author, name='del_avtor')




]
