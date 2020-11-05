# ordermanagement-mod5

in order to have more info about django reset password views see this page : 'https://docs.djangoproject.com/en/3.0/topics/auth/default/#all-authentication-views'
to send a reset password first we need some views and urls that we wrote them in accounts/urls.py as auth_views .
then we need some smtp settings in settings.py .for more info about smtp configs search for 'gmail smtp configuration'.
then if you need to customize the rest password template you should create an html file(in here password_reset.html).
then you need to add that html in 'urls.py' in the 'reset_password' path.this change could be apply on every auth_views.
at the end add reset password link to login.html file.
