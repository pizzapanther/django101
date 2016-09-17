from django.template.response import TemplateResponse

def homepage (request):
    context = {
        'n': 6
    }
    
    return TemplateResponse(request, 'index.html', context)
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    