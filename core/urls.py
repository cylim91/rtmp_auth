from django.urls                    import URLPattern, include, path
from rest_framework                 import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

import core.views as core_view

router = routers.DefaultRouter()

app_name = 'core'

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-token/',        TokenObtainPairView.as_view(),      name='token_obtain_pair'),
    # path('api-token-verify/', TokenVerifyView.as_view(),          name='api-token-verify'),
    # path('login_user/'      , core_view.LoginUserView.as_view(),  name='login_user'),
    # path('login_admin/'     , core_view.LoginAdminView.as_view(), name='login_admin'),
    # path('get_user_profile/', core_view.GetUserProfile.as_view(), name='get_user_profile'),

    # path('verify_user/',      core_view.VerifyUser.as_view(),     name='verify_user'),
    # path('verify_token/',     core_view.VerifyToken.as_view(),    name='verify_token'),
    path('stream_auth/', core_view.StreamAuth.as_view(), name='stream_auth'),
]