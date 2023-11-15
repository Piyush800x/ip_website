from django.shortcuts import render, HttpResponse
import ipinfo
# Create your views here.


def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, "index.html", ipinfos(request))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(', ')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ipinfos(request):
    access_token = '4e4f25d4143dc9'
    handler = ipinfo.getHandler(access_token)
    ip_addr = get_client_ip(request)
    details = handler.getDetails("49.37.54.206")
    search(request)
    return details.all


def search(request):
    ip = request.GET
    print(ip)
    pass
