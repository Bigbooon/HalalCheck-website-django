from django.shortcuts import render
from django.db.models import Q

from .models import Comp, Tag


# Create your views here.
def comp_list(request):
    search1_query = request.GET.get('search1', '')

    if search1_query:
        comps = Comp.objects.filter(Q(slug__icontains=search1_query) | Q(halal__icontains=search1_query))
    else:
        comps = Comp.objects.all()

    return render(request, 'compon/index.html', context={'comps': comps})


def comp_tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'compon/tag_detail.html', context={'tag': tag})
