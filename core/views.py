from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import requests
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Event, Review, Category, Bookmark, Organizer, Media, Ticket
import random
from django.db.models import Sum
from django.template.defaultfilters import slugify  
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import environ
from .forms import EventForm
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Create your views here.
def index(request):
    events = Event.objects.all()
    

    context = {'events':events}
    return render(request, 'main.html', context)

def browse(request):
    events = Event.objects.all()

    context = {'events':events}
    return render(request, 'browse.html', context)

def details(request, slug):
    event = Event.objects.get(slug=slug)
    organizer = Organizer.objects.all()
    media = event.media_set.all()
    review = event.review_set.all()
    ticket = Ticket.objects.filter(event=event)
    if request.method == 'POST':
        comment = Review.objects.create(
            name = request.POST.get('name'),
            comment = request.POST.get('comment'),
            event = event
        )
        comment.save()
        return redirect('details', slug=event.slug)

    context = {'event':event, 'media':media, 'review':review, 'ticket':ticket, 'organizer':organizer}
    return render(request, 'event.html', context)

def admin_details(request, slug):
    event = Event.objects.get(slug=slug)
    tickets = event.ticket_set.all()
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
         

    context = {'event':event, 'tickets':tickets, 'form':form}
    return render(request, 'adminview.html', context)

def delete_event(request, slug):
    event = Event.objects.get(slug=slug)


    if request.method == 'POST':
        event.delete()
        return redirect('index')
    
    context = {'event':event}
    return render(request, 'delete.html', context)
def profile(request, slug):
    profilex = Organizer.objects.get(slug=slug)
    events = Event.objects.filter(creator=profilex)
    tickets = Ticket.objects.filter(event__creator=profilex)
    sum_totalx  = events.count()
    sum_total =  sum(events.values_list('ticket_price', flat=True))

    if request.method == 'POST':
        account_number = request.POST.get('phone')
        account_name = request.POST.get('phone')
        bank = request.POST.get('phone')
        
        org = Organizer.objects.create(
            user = request.user,
            phone = request.POST.get('phone'),
            account_number = request.POST.get('aza_num'),
            account_name = request.POST.get('aza_name'),
            bank = request.POST.get('bank'),
            poster = request.FILES.get('image'),
            slug = slugify(request.POST['user']),
        )
        
        org.save()
        rave = Rave(os.getenv("FLW_PUBLIC_KEY"), os.getenv("FLW_SECRET_KEY"))
        details = {
          "account_number": account_number,
          "account_bank": bank
        }
        response = rave.Transfer.accountResolve(details)
        context = {'response':response}
        return redirect('profile', context)

    context = {'profilex':profilex, 'events':events, 'tickets':tickets, 'sum_total':sum_total, 'sum_totalx':sum_totalx}
    return render(request, 'profile.html', context)

def create_event(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        eventcreate = Event.objects.create(
            title = request.POST.get('title'),
            venue = request.POST.get('venue'),
            description = request.POST.get('description'),
            tickets_ava = request.POST.get('limit'),
            ticket_price = request.POST.get('price'),
            creator = request.user,
            category = request.POST.get('category'),
            date = request.POST.get('date'),
            slug = slugify(request.POST['title']),  
            poster = request.FILES.get('images')
        )
        
        eventcreate.save()

        for image in images:
            photo = Media.objects.create(
            event = eventcreate,
            photos = image,
            video = request.FILES.get('video'),
            )
            photo.save()

        

        # photo = Media.objects.create(
        #     event = eventcreate,
        #     photos = request.FILES.get('image'),
        #     video = request.FILES.get('floor_plan'),
        # )
        # photo.save()
            
        return redirect('details', slug=eventcreate.slug)

    context = {}
    return render(request, 'org.html', context)

def sendmail(request, slug):
    global eventx
    eventx = Event.objects.get(slug=slug)
    byte = random.randint(1000,1239)
    # global tix_code
    # tix_code = "#" + str(eventx.id) + "-" + str(random.randint(1000,123999999))
    global tix_mail
    tix_mail = request.POST.get('customer[email]')
    # tix_name = request.POST.get('customer[name]')
    # tix_phone = request.POST.get('phone')
    if request.method == 'POST':
        global tix_code
        tix_code = "#" + str(eventx.id) + "-" + str(random.randint(1000,123999999))
        tix_mail = request.POST.get('customer[email]')
        global tix_name
        tix_name = request.POST.get('customer[name]')
        tix_phone = request.POST.get('phone')
        ticket_price = request.POST.get('price'),
        tix = Ticket.objects.create(
            event = eventx,
            tix_code = tix_code,
            tix_mail = request.POST.get('customer[email]'),
            tix_name = request.POST.get('customer[name]'),
            tix_phone = request.POST.get('phone'),
            ticket_price = request.POST.get('price'),
        )
        tix.save()
        return redirect(str(process_payment(tix_name,tix_mail,ticket_price,tix_phone)))

    context = {'event':eventx, 'byte':byte}
    return render(request,'pay.html', context)

def bookmark(request, pk):
    eventx = Event.objects.get(slug=pk)
    
    
    tix = Bookmark.objects.create(
            
            user = request.user,  
        )
    tix.save()
    tix.event.add(eventx)
        
    return redirect('details', slug=eventx.slug)
    
def organizer(request):
    if request.method == 'POST':
        org = Organizer.objects.create(
            user = request.user,
            phone = request.POST.get('phone'),
            account_number = request.POST.get('aza_num'),
            account_name = request.POST.get('aza_name'),
            bank = request.POST.get('bank'),
            poster = request.FILES.get('image'),
            biz_name = request.POST.get('biz_name'),
            bio = request.POST.get('bio'),
            slug = slugify(request.POST['biz_name']),
        )
        org.save()
        return redirect('profile', slug=org.slug)
    return render(request, 'org_create.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
                messages.error(request, "User already exists.")
                return redirect('signup')

        if not request.POST.get('password1'):
            messages.error(request, "Password cannot be blank.")
            return redirect('signup')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "User already exists.")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name, password=password1, email=email)
                return redirect('signin')


    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']

        if not request.POST.get('email'):
            messages.error(request, "Email cannot be blank.")
            return redirect('signin')

        if not request.POST.get('password'):
            messages.error(request, "Password cannot be blank.")
            return redirect('signin')

        user = auth.authenticate(request, username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'login.html')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin') 

def process_payment(tix_name,tix_mail,ticket_price,tix_phone):
     auth_token= env('SECRET_KEY')
     hed = {'Authorization': 'Bearer ' + auth_token}
     data = {
                "tx_ref":''+str((1000 + random.random()*900)),
                "amount":ticket_price,
                "currency":"NGN",
                "redirect_url":"http://localhost:8000/callback",
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":tix_mail,
                    "phonenumber":tix_phone,
                    "name":tix_name
                },
                "customizations":{
                    "title":"Supa Electronics Store",
                    "description":"Best store in town",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
     url = ' https://api.flutterwave.com/v3/payments'
     response = requests.post(url, json=data, headers=hed)
     response=response.json()
     link=response['data']['link']
    #  message = 'Dear' + tix_name + 'your ticket for event has been booked. Your ticket code is ' + tix_code,
    #  receiver = tix_mail
     return link
    

@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    event = str(eventx)
    tix_namez = tix_name
    tix_codex = 'Hello ' + tix_namez + ' your ticket for the show ' + event + ' has been booked, your ticket code is '+ tix_code
    tix_mailx = tix_mail
    send_mail(
            'Ticket booked!!!',
            tix_codex,
            'settings.EMAIL_HOST_USER',
            [tix_mailx],
            fail_silently=False,
        )
    return HttpResponse('Finished')



import os
from rave_python import Rave

def verifyaza(account_name,account_number,bank):
    rave = Rave(os.getenv("FLW_PUBLIC_KEY"), os.getenv("FLW_SECRET_KEY"))
    details = {
      "account_number": account_number,
      "account_bank": bank
    }
    response = rave.Transfer.accountResolve(details)
    context = {'response':response}
    return redirect('profile', context)