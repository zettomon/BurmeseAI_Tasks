from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .models import DataEntry

def submission_portal(request):
    data = DataEntry.objects.all()
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'submission_portal/index.html', {'data': data})

def form_add(request):
    if request.method == 'POST':
        DataEntry.objects.create(
            content = request.POST.get('content'),
            category = request.POST.get('category'),
            is_reviewed = request.POST.get('is_reviewed')
        )
        response = HttpResponse()
        response['HX-Redirect'] = '/submission_portal'
        return response
    return render(request, 'submission_portal/components/form.html')