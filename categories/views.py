from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from . models import Category
from .serializer import serialize_categories
import json
# Create your views here.


# Class based template to handle index page request
class HomeView(TemplateView):
    template_name = 'categories/index.html'
    def get(self, request, *args, **kwargs):
        """
            returns index.html
        """
        # Querying categories
        categories = Category.objects.filter(parent=None)
        # Checking if default root categories exist or not
        if categories.exists() == False:
            # Adding root categories if they dont exist
            Category.objects.get_or_create(name="A", level=0)
            Category.objects.get_or_create(name="B", level=0)

            categories = Category.objects.filter(parent=None)

        return render(request, template_name=self.template_name, context={'categories' : categories})


    def post(self, request, *args, **kwargs):
        """ Post request view to handle adding new categories and returns them as json """
        cat_id = request.POST.get("category_id")
        print(cat_id)
        # Getting the current parent category
        parent = Category.objects.get(id=cat_id)
        categories = None
        if parent:
            # Querying existing sub categories
            categories = Category.objects.filter(parent=parent)

            # If no sub categories found create 2 new sub categories
            if categories.count() == 0:
                cat1 = Category.objects.create(name='1', cat_type='1', parent=parent)
                cat2 = Category.objects.create(name='2', cat_type='2', parent=parent)

                categories = [cat1, cat2]

            # Serializing data to be sent as a response
            data = serialize_categories(categories)

            return JsonResponse(data)

        return JsonResponse({"error" : "no parent specified"})
