from django.shortcuts import render
from django.http import HttpResponse

from .models import DataEntry
from .utils import paginate

# Main Page of Data Submission Portal
def submission_portal(request):
    search_query = request.GET.get('search', '')
    data = DataEntry.objects.all()
    data = paginate(data=data, request=request)
    text_count = DataEntry.objects.filter(category='text').count()
    image_url_count = DataEntry.objects.filter(category='image_url').count()
    context = {
        'data': data,
        'text_count': text_count,
        'image_url_count': image_url_count,
        'search_query': search_query
    }
    return render(request, 'submission_portal/submission_page.html', context=context)

# Read https://www.w3schools.com/django/django_queryset_filter.php

# Search Bar Handler
def form_search(request):
    search_query = request.GET.get('search', '')
    data = DataEntry.objects.filter(content__contains=search_query)
    data = paginate(data=data, request=request)
    context = {
        'data': data,
        'search_query': search_query
    }
    if request.htmx:
        template = 'submission_portal/components/pagination.html'
    else:
        template = 'submission_portal/submission_page.html'
    return render(request, template, context=context)

# Form Category Handler
def form_filter_category(request):
    category = request.GET.get('category')
    if category == 'all':
        data = DataEntry.objects.all()
    else:
        data = DataEntry.objects.filter(category=category)
    data = paginate(data=data, request=request)
    context = {
        'data': data,
        'category_query': category
    }
    if request.htmx:
        template = 'submission_portal/components/pagination.html'
    else:
        template = 'submission_portal/submission_page.html'
    return render(request, template, context=context)

# Marking/Unmarking Is_Reviewed Handler
def handle_reviewed(request):
    entry_id = request.GET.get('entry_id')
    entry = DataEntry.objects.filter(id=entry_id).first()
    entry.is_reviewed = not entry.is_reviewed
    entry.save()
    context = {
        'entry': entry
    }
    return render(request, 'submission_portal/components/is_reviewed.html', context=context)

# Form for adding new data
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
    return render(request, 'submission_portal/components/submission_form.html')
