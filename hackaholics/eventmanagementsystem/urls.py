from django.urls import path

from . import views 

urlpatterns=[path('',views.home,name="index"),
path("organizer",views.organizer,name="organizer"),
path("participant",views.participant,name="participant"),
path("login",views.login,name="login"),
path("signup",views.signup,name="signup"),
path("signupcredentials",views.signupdetails,name="signupcredentials"),
path("logincredentials",views.logincredentials,name="logincredentials"),
path("eventcreate",views.eventcreate,name="eventcreate"),
path("newevent",views.newevent,name="newevent"),
path("registerevent",views.registerevent,name="register_event"),
path("event_activities",views.eventactivities,name="event_activities"),
path("view_sessions",views.session,name="view_session"),
path("view_location",views.location,name="view_location")
]
