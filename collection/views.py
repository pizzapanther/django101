from django.template.response import TemplateResponse

from collection.models import Thing

def homepage (request):
    things = Thing.objects.all()
    
    context = {
        'things': things
    }
    
    return TemplateResponse(request, 'index.html', context)
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    