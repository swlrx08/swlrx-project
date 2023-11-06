from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from Documents.models import Documents
from Projects.models import Projects


def home(request):
    documents = Documents.objects.all()
    projects = Projects.objects.all()
    paginator = Paginator(projects,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'documents': documents,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)



