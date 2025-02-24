from django.shortcuts import render
from .models import credentials,events

# Create your views here.
def home(req):
    return render(req,"home.html")

def organizer(req):
    return render(req,"login-signup.html")
def participant(req):
    return render(req,"pardashboard.html",{"events":events.objects.all()})

def login(req):
    return render(req,"login.html")
def signup(req):
    return render(req,"signup.html")

def signupdetails(req):
    print(req.POST["name"])
    print(req.POST["email"])
    print(req.POST["password"])
    user=credentials(name=req.POST["name"],email=req.POST["email"],password=req.POST["password"])
    user.save()
    return render(req,"accountcreated.html")
def logincredentials(req):
    print(req.POST["email"])
    print(req.POST["password"])
    users=credentials.objects.all()
    for cred in users:
        if cred.email==req.POST["email"] and cred.password==req.POST["password"]:
            return render(req,"orgdashboard.html",{"events":events.objects.all(),"useremail":req.POST["email"]})

    return render(req,"loginfail.html")
    
def eventcreate(req):
    return render(req,"eventcreate.html")

def newevent(req):

    
    eve=events(organizeremail=req.POST["organizer_email"],name=req.POST["event_name"],description=req.POST["event_description"],datetime=req.POST["event_datetime"],location=req.POST["event_location"],eventtype=req.POST["event_type"],category=req.POST["event_category"],utubelink=req.POST["youtube_link"])
    eve.save()
    return render(req,"eventsuccessful.html")



def registerevent(req):
    return 
def eventactivities(req):
    return 

def session(req):
    return 

def location(req):
    return 


