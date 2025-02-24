from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .models import DataEntry

# Main Page of Data Submission Portal
def submission_portal(request):
    data = DataEntry.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    text_count = DataEntry.objects.filter(category='text').count()
    image_url_count = DataEntry.objects.filter(category='image_url').count()
    context = {
        'data': data,
        'text_count': text_count,
        'image_url_count': image_url_count
    }
    return render(request, 'submission_portal/submission_page.html', context=context)

# Read https://www.w3schools.com/django/django_queryset_filter.php

# Search Bar Handler
def form_search(request):
    if request.method == 'POST':
        data = DataEntry.objects.filter(content__contains=request.POST.get('search'))
        context = {
            'data': data
        }
        return render(request, 'submission_portal/components/submission_table.html', context=context)

# Form Category Handler
def form_filter_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        if category == 'all':
            data = DataEntry.objects.all()
        else:
            data = DataEntry.objects.filter(category=request.POST.get('category'))
        context = {
            'data': data
        }
        return render(request, 'submission_portal/components/submission_table.html', context=context)

# Marking/Unmarking Is_Reviewed Handler
def handle_reviewed(request):
    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        entry = DataEntry.objects.filter(id=entry_id).first()
        entry.is_reviewed = not entry.is_reviewed
        entry.save()
        data = DataEntry.objects.all()
        context = {
            'data': data
        }
        return render(request, 'submission_portal/components/submission_table.html', context=context)

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
