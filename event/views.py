from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from .models import Category, Judge, Club, Dog, Dog_Event
from django.db.models import Q




def post_list(request):
    posts = Dog_Event.objects.order_by('category__name')
    return render(request, 'event/post_list.html', {'posts': posts})

def post_list_all_categories(request):
    posts = Dog_Event.objects.order_by('category__name')
    return render(request, 'event/property-grid.html', {'posts': posts})


def post_list_category(request,category):
    posts = Dog_Event.objects.filter(category__pk=category)
    return render(request, 'event/post_list_category.html', {'posts': posts})

def post_list_judge(request,judge):
    posts = Dog_Event.objects.filter(judge__pk=judge)
    return render(request, 'event/post_list_judge.html', {'posts': posts})

def post_list_club(request,club):
    posts = Dog_Event.objects.filter(club__pk=club)
    return render(request, 'event/post_list_club.html', {'posts': posts})

def post_list_dog(request,dog):
    posts = Dog_Event.objects.filter(dog__pk=dog)
    return render(request, 'event/post_list_dog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Dog_Event, pk=pk)
    return render(request, 'event/property-single.html', {'post': post})

def get_queryset(self):
    query = self.request.GET.get('q')
    if query:
        return Dog_Event.objects.filter(pk=query)
    else:
        return Dog_Event.objects.all()


def search(request):
    search =  request.GET.get('search')
    posts = Dog_Event.objects.filter(Q(name__contains=search)|Q(description__contains=search)|Q(category__name__contains=search)|Q(club__name__contains=search)|Q(dog__name__contains=search)|Q(judge__name__contains=search)|Q(judge__country__contains=search)).order_by('category')
    return render(request, 'event/property-grid.html', {'posts': posts})




