from django.core.paginator import Paginator


# function to be reused in various views to paginate the request
def paginate(data, request, per_page=10):
    paginator = Paginator(data, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj