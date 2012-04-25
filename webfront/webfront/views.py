from django.shortcuts import render_to_response
#import MySQLdb

from django.http import HttpResponse

def home_view(request):
	return render_to_response('index.html')
	
def search(request):
	userInput=request.GET['userInput']
	keys=userInput.split()
	k=keys[0]
	from searchData.models import ResultUrls
	results=ResultUrls(k)  #data is accessed here	
	return render_to_response('results.html',{'Qresults':results.urls, 'bounce_key': userInput})

