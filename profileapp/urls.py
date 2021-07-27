from django.urls import path

from profileapp.views import ProfileCreateView
app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<ink:pk>', ProfileCreateView.as_view(), name='update'),

]