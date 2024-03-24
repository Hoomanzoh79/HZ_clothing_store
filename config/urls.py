"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import (signup, login, logout, email, password_change, password_reset,password_reset_done, email_verification_sent,confirm_email,password_reset_from_key,password_reset_from_key_done)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('profile/', include('accounts.urls')),
    path('', include('cloths.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('orders.urls')),
    path('payment/', include('payment.urls')),
    path('search/', include('search.urls')),
    # All Auth
    path("account/login/", login, name="account_login"),
    path("account/logout/", logout, name="account_logout"),
    path("account/signup/", signup, name="account_signup"),
    path("account/email/", email, name="account_email"),
    path("account/password/reset/", password_reset, name="account_reset_password"),
    path("account/password/reset/done/", password_reset_done, name="account_reset_password_done"),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
    path("account/password/change/", password_change, name="account_change_password"),
    path("account/confirm-email/",email_verification_sent,name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$",confirm_email,name="account_confirm_email"),
    # Rosetta (i18n)
    path('rosetta/', include('rosetta.urls')),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
