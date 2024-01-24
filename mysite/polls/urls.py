from django.urls import path
from polls import views


app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:question_id>/", views.detail, name="detail"),
    path('results/<int:question_id>/', views.results, name='results'),
    path('votes/<int:question_id>/', views.votes, name='votes'),
    # path('details', views.details, name='details'),

]
