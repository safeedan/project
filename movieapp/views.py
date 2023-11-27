from django.shortcuts import render
from django . http import HttpResponse
from . models import Movie
from django.shortcuts import redirect
from . forms import MovieForm



def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)
def details(request,Movie_id):
     #return HttpResponse("this is movie no %Movie_id")
     movie = Movie.objects.get(id=Movie_id)
     return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        des = request.POST.get('des',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,des=des,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,"add.html")
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm (request.POST or None, request. FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")