from django.urls import path
from .views import (signup, users, signin, AuthenticateUSer,
                    signout, UserViewSet
                    )


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('users', users),
    path('currentuser', AuthenticateUSer.as_view()),
    path('signout', signout),
    
    
    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    }))

]
