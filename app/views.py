from django.shortcuts import render, HttpResponse
import ipinfo
from pymongo.mongo_client import MongoClient
from my_portfolio.settings import DB_NAME
from datetime import date, datetime

# Create your views here.
client = MongoClient(DB_NAME)
db = client['ip-data']
collection = db['user-data']


def base(request):
    return render(request, "base.html")


def home(request):
    if request.method == "POST":
        ip = request.POST['ip-addr']
    if request.method == "GET":
        ip = get_client_ip(request)
    info = ipinfos(request, ip)
    if request.user.is_authenticated:
        create_data(info)
    return render(request, "index.html", info)


def about(request):
    return render(request, "about.html")


def history(request):
    return render(request, "history.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(', ')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ipinfos(request, ip_addr):
    access_token = '4e4f25d4143dc9'
    handler = ipinfo.getHandler(access_token)
    # ip_addr = get_client_ip(request)
    details = handler.getDetails(ip_addr)
    return details.all


def create_data(info):
    now = datetime.now()
    doc = {
        "ip": info.get("ip"),
        "city": info.get("city"),
        "region": info.get("region"),
        "loc": info.get("loc"),
        "isp": info.get("org"),
        "postal": info.get("postal"),
        "timezone": info.get("timezone"),
        "date&time": f'{date.today()} - {now.strftime("%H:%M:%S")}'
    }
    collection.insert_one(doc)
    print("Done")
