from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View


class BaseView(View):
    http_method_names = ['get']
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login'))

        return HttpResponse("hello, world!")

class UserAuthView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            print "hello?"
            return HttpResponseRedirect(reverse('login'))

        print "going back to base view!"
        return HttpResponseRedirect(reverse('base_view'))
    
