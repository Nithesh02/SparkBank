from .forms import CustomerForm, TransitionForm
from django.shortcuts import redirect, render,get_object_or_404
import requests

# Create your views here.
from .models import *
from django.contrib import messages

def home_view(request):
    context={}
    return render(request,"bank/index.html",context)

def new_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been submitted successfully!')

    return render(request, "bank/new_customer.html")
    
def view_customers(request):
    customers = Customer.objects.all()
    context={'customers' : customers}
    return render(request,"bank/view_customers.html",context)

def customer_details(request, pk):
    customer = Customer.objects.get(id = pk)
    customers = Customer.objects.all()
    context={'customer':customer, 'customers':customers}
    
    if request.method == "POST":
        amount = request.POST.get('amount')
        receiver_name = request.POST.get('receiver_name')
        sender_name = customer.name
        customer_details = Transfer(sender_name=sender_name, amount=amount, receiver_name=receiver_name)
        customer_details.save()
        customer.delete()

        sender_balance = customer.current_balance - int(amount)
        sender_number = customer.number
        sender_email = customer.email
        update_sender = Customer(name=sender_name, number=sender_number, email=sender_email, current_balance=sender_balance)
        update_sender.save()
         
        receiver = Customer.objects.get(name=receiver_name)
        receiver_email = receiver.email
        receiver_number = receiver.number
        receiver_balance = receiver.current_balance + int(amount)
        receiver.delete()
        update_receiver = Customer(name=receiver_name, number=receiver_number, email=receiver_email, current_balance=receiver_balance)
        update_receiver.save()

        return redirect('/')
        
    return render(request,"bank/customer_details.html",context)
    