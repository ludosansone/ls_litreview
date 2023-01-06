from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.signin, name='signin'),
    path('signup', auth_views.signup, name='signup'),
    path('signout', auth_views.signout, name='signout'),
    path('home', main_views.home, name='home'),
    path('subscribs', main_views.subscribs, name='subscribs'),
    path('contributions', main_views.contributions, name='contributions'),
    path('new-ticket', main_views.new_ticket, name='new-ticket'),
    path('edit-ticket/<int:id>/', main_views.edit_ticket, name='edit-ticket'),
    path('new-review/<int:ticket_id>/', main_views.new_review, name='new-review'),
    path('edit-review/<int:id>/', main_views.edit_review, name='edit-review'),
    path('details-ticket/<int:id>/', main_views.details_ticket, name='details-ticket'),
    path('details-review/<int:id>/', main_views.details_review, name='details-review'),
    path('delete-ticket/<int:id>/', main_views.delete_ticket, name='delete-ticket'),
    path('delete-review/<int:id>/', main_views.delete_review, name='delete-review'),
    path('new-ticket-and-review', main_views.new_ticket_and_review, name='new-ticket-and-review'),
    path('stop-follow/<int:id>/', main_views.stop_follow, name='stop-follow'),
]
