from django.shortcuts import render
from django.http import JsonResponse

class Job:
    def __init__(self,desig,org,salary):
        self.desig = desig
        self.org = org
        self.salary = salary

    def display(self):
        print 'Designation :'+self.desig +' Oganisation :'+self.org+' Expereince Needed :'+self.salary

from bs4 import BeautifulSoup
import urllib2
import json

# Create your views here.
def list(request,skill,city):
    url = "https://www.naukri.com/"+skill+"-jobs-in-"+city
    sauce = urllib2.urlopen(url).read()
    soup = BeautifulSoup(sauce,'lxml')
    data = soup.find_all('li',class_="desig")
    data1 = soup.find_all('span',class_="org")
    data2 = soup.find_all('span',class_="exp")

    j = []
    for i in range(len(data)):
        job = Job(data[i].text,data1[i].text,data2[i].text)
        j.append(job)
        print job.display()
    json_string = json.dumps([ob.__dict__ for ob in j])
    print json_string
    ##l = json.dumps(json_string)
    return JsonResponse(json_string,safe=False)