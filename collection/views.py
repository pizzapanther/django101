from django.template.response import TemplateResponse

def homepage (request):
    return TemplateResponse(request, 'index.html', {})
    