from django.db import models

# Create your models here.


#class Index(models.Model):
#	keyword=models.CharField(max_length=255)
#	url=models.CharField(max_length=255)

#class Ranks(models.Model):
#	url=models.CharField(max_length=255)
#	rank=models.FloatField()

class ResultUrls(models.Model):
	#url=models.CharField(max_length=255)
	#description=models.CharField(max_length=255)
	def __init__(self,KEY):
		import MySQLdb
		db=MySQLdb.connect(user='root',db='mini', passwd='cxl', host='localhost')
		cursor=db.cursor()
		cursor.execute('select url,title from mini_index natural join mini_ranks where keyword="'+ KEY+'" order by rank desc')
		urls=[]
		for row in cursor.fetchall():
			urls.append({'url':row[0], 'title':row[1]})
		db.close()
		self.urls=urls
		
	
