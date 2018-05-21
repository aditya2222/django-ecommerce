from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.


class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_queryset(self):
        # GET returns a key value pai and get lets us fetch  the value using the key returned by GET
        # shirt after the q acts as the alternative parameter in case the q does not exist or is none
        query = self.request.GET.get('q',None)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        else:
            return Product.objects.none()
        """ 
        __icontains = field contains this
        __iexact = field is exactly this
        both are not case sensitive
        """
