from django.http import HttpResponse

def book_list(request):
    return HttpResponse("BOOK LIST VIEW IS WORKING")

