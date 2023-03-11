from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def pasts(request):
    pass


def post_detail(request):
    pass
