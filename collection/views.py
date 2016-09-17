from django.template.response import TemplateResponse

from collection.models import Thing

def homepage (request):
    search = request.GET.get('search', '')
    
    if search:
        things = Thing.objects.filter(name__icontains=search).order_by('name')
        
    else:
        things = Thing.objects.all().order_by('name')
        
    context = {
        'things': things
    }
    
    return TemplateResponse(request, 'index.html', context)
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    