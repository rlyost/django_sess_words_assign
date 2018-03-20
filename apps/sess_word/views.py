from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'sess_word/index.html')

def process(request):
    if 'context' not in request.session:
        request.session['context'] = ''
    if request.method == "POST":
        word = request.POST['word']
        color = request.POST['word_color']
        size = request.POST.get('word_size','small')
        time = strftime("%H:%M %p %B-%d, %Y", gmtime())
        request.session['context'] += "<br><p class='" +color+ ' ' +size+ "'>"+word+ "</p><p class='add'>  - added at " +time+"</p>"
    return redirect("/", request.session['context'])

def clear(request):
    request.session['context'] = ''
    return redirect('/')