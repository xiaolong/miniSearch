from django.shortcuts import render_to_response
import MySQLdb


def home_view(request):
	return render_to_response('index.html')

