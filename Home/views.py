from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from ContactMe.forms import ContactFormModule
from Documents.models import Documents
from Projects.models import Projects


def home(request):
    documents = Documents.objects.all()
    projects = Projects.objects.all()
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        contact_form = ContactFormModule(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactFormModule()

    context = {
        'documents': documents,
        'page_obj': page_obj,
        'contact_form': contact_form,
    }
    return render(request, 'index.html', context)
