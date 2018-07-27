from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse, HttpResponse


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank You!"})

    if form.errors:
        errors = form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    return render(request, 'contact/view.html', context)
