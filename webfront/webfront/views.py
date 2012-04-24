from django.shortcuts import render_to_response
#import MySQLdb

from django.http import HttpResponse

def home_view(request):
	return render_to_response('index.html')
	
def search(request):
	k=request.GET['userInput']
	from searchData.models import ResultUrls
	results=ResultUrls(k)  #data is accessed here
	return render_to_response('results.html',{'Qresults':results.urls})

