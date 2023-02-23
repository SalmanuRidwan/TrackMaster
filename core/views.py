# works with both python 2 and 3
from __future__ import print_function
import africastalking
import environ
env = environ.Env()
environ.Env.read_env()
from django.shortcuts import render


username = env('AT_USERNAME')
api_key = env('API_KEY')

africastalking.initialize(username, api_key)

voice = africastalking.Voice

def make_conference(request):
    callFrom = "+254711082570"

    if request.method == "GET":
        return render(request, "conference.html")
    
    # if request.POST == "POST":
    callFrom = "+254711082570"
    callTo = '+2349035947006'

    try:
        # Make the call
        voice.call(callFrom, callTo)
    except Exception as e:
        print ("Encountered an error while making the call:%s" %str(e))

    return render(request, 'conference.html')