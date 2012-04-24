from django.shortcuts import render_to_response
import MySQLdb

from django.http import HttpResponse

def home_view(request):
	return render_to_response('index.html')
	
def search(request):
	k=request.GET['userInput']
	db=MySQLdb.connect(user='root',db='mini', passwd='cxl', host='localhost')
	cursor=db.cursor()
	cursor.execute('select url from mini_index natural join mini_ranks where keyword="'+ k+'" order by rank desc')
	names=[row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('results.html',{'Qresults':names})
	

