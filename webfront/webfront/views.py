from django.shortcuts import render_to_response
import MySQLdb

from django.http import HttpResponse

def home_view(request):
	return render_to_response('index.html')
	
def search(request):
	#return render_to_response('results.html',{'word': request.GET['userInput']})
	db=MySQLdb.connect(user='root',db='test', passwd='cxl', host='localhost')
	cursor=db.cursor()
	cursor.execute('select name from girls')
	names=[row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('results.html',{'Qresults':names})

