from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from collection.models import Thing

def homepage (request):
    search = request.GET.get('search', '')
    
    if search:
        things = Thing.objects.filter(name__icontains=search).order_by('name')
        
    else:
        things = Thing.objects.all().order_by('name')
        
    context = {
        'things': things,
        'search': search,
    }
    
    return TemplateResponse(request, 'index.html', context)
    
def detail_view (request, slug):
    thing = get_object_or_404(Thing, slug=slug)
    
    context = {
        'thing': thing,
    }
    
    return TemplateResponse(request, 'detail.html', context)
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    