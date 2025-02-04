"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]

'''
Now we have to tell Django when to serve this view. It’s done inside the urls.py file:

urls.py

from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]

If you compare the snippet above with your urls.py file, you will notice I added the following new line: url(r'^$', views.home, name='home') and imported the views module from our app boards using from boards import views.

As I mentioned before, we will explore those concepts in great detail later on.

But for now, Django works with regex to match the requested URL. For our home view, I’m using the ^$ regex, which will match an empty path, which is the homepage (this url: http://127.0.0.1:8000). If I wanted to match the URL http://127.0.0.1:8000/homepage/, my url would be: url(r'^homepage/$', views.home, name='home').

Let’s see what happen:

python manage.py runserver
'''
