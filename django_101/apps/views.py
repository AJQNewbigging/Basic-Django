from django.views.generic import View


class BaseView(View):
    http_method_names = ['get']
  
