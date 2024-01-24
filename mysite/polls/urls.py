from django.urls import path
from polls import views


app_name = "polls"

# urlpatterns = [
#     path('', views.index, name='index'),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path('results/<int:question_id>/', views.results, name='results'),
#     path('votes/<int:question_id>/', views.votes, name='votes'),
#     # path('details', views.details, name='details'),

# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.votes, name="votes"),
]
