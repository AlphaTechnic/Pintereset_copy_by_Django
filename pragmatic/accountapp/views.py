from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    # return HttpResponse("안녕하세요")

    # 아래와 같은 가독성을 위해 accountapp/templates/accountapp과 같은 폴더 구조를 만들었다.
    return render(request, 'accountapp/hello_world.html')
