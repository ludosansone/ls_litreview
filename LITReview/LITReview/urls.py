from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.signin, name='signin'),
    path('signup', main_views.signup, name='signup'),
    path('home', main_views.home, name='home'),
    path('subscribs', main_views.subscribs, name='subscribs'),
    path('contributions', main_views.contributions, name='contributions'),
    path('new-ticket', main_views.new_ticket, name='new-ticket'),
    path('edit-ticket', main_views.edit_ticket, name='edit-ticket'),
    path('new-review', main_views.new_review, name='new-review'),
    path('edit-review', main_views.edit_review, name='edit-review'),
]
