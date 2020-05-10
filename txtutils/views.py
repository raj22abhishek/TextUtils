#I have created this files

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'Abhishek','place':'BLR'}
    return render(request,'index.html',params)
def analyse(request):
    analyse_txt = request.POST.get('text','No Comment')
    offOn = request.POST.get('punc','OFF')
    upper = request.POST.get('upper', 'OFF')
    newLine = request.POST.get('newLine','OFF')
    params = {'analyse_txt': analyse_txt, 'offOn': offOn}
    data = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if(offOn == 'on'):
        for char in analyse_txt:
            if char not in punctuations:
                data +=char
        params = {'purpose':'Remove Punc','analyse_txt': data, 'offOn': offOn}
        return render(request,'analyse.html',params)
    elif(upper == 'on'):
        x = analyse_txt.upper()
        params = {'purpose':'Captilazed','analyse_txt': x, 'offOn': offOn}
        return render(request,'analyse.html',params)
    elif (newLine == 'on'):
        x = analyse_txt.upper()
        data = ""
        for char in analyse_txt:
            if char == "\n":
                data += " "
            else:
                data += char
        params = {'purpose': 'New Line Removar', 'analyse_txt': data, 'offOn': offOn}
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("ERROR")