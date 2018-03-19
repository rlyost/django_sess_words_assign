from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'sess_word/index.html')

def process(request):
    if request.method == "POST": 
        request.session['context'] = {"word": request.POST['word'], "word_color": request.POST['word_color'], "word_size": request.POST['word_size'], "time": strftime("%Y-%m-%d %H:%M %p", gmtime())}
    return redirect("/", request.session['context'])

def clear(request):
    del request.session['context']
    return redirect('/')