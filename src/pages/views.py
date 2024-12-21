from django.shortcuts import render


def doctorpage(request):
    return  render(request,'pages\doctorpage.html')

def studentpage(request):
    return  render(request,'pages\studentpage.html')