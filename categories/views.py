from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# Class based template to handle index page request
class HomeView(TemplateView):
    template_name = 'categories/index.html'

    def get(self, request, *args, **kwargs):
        """
            returns index.html
        """
        return render(request, template_name=self.template_name)
