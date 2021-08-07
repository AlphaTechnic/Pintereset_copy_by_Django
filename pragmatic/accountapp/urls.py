"""
128.0.0.1:8000/account/hello_world 를 일일이 타이핑하기에는 번거롭다.
 -> app_name과 url name을 부여하게 되면, 위의 표현을
accountapp:hello_world
이렇게 간단하게 표현이 가능하게 된다.
"""

from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]