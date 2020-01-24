from django.shortcuts import render
from django.http import HttpResponse
from . forms import CustomerForm
from . models import Customer

# Create your views here.
def index(request):
    return render(request, "user/index.html")

def valid_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        username = request.POST.get('username', '')
        customer = Customer.objects.filter(login__contains=username)

        if not customer:
            return render(request, "user/index.html")
        else:
            return HttpResponse('Hello ', customer)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
