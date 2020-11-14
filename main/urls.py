from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new_user', views.new_user),
    path('success', views.success),
    path('destroy_session', views.destroy),
    path('login', views.login),
    path('jobs/new', views.new_job),
    path('jobs/create', views.create_job),
    path('jobs/<int:job_id>', views.job_desc),
    path('jobs/edit/<int:job_id>', views.job_edit),
    path('jobs/edit/<int:job_id>/complete', views.complete_edit),
    path('/edit/<int:job_id/<int:user_id>', views.edit_function),
    path('job/<int:jobid>/delete', views.deletejob),
]