
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views import home,success,admin_dashboard,edit_user,delete_user,edit_form

urlpatterns = [
    
    path("",home,name="home"),
    path("success",success,name="success"),
    path("admin_dashboard",admin_dashboard,name="admin_dashboard"),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('edit_form',edit_form,name="edit_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
