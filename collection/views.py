from django.template.response import TemplateResponse

def homepage (request):
    return TemplateResponse(request, 'index.html', {})
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    