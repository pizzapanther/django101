from django.template.response import TemplateResponse

def homepage (request):
    num = int(request.GET.get('num', '6'))
    
    context = {
        'num': num,
        'name': 'Paul edkjhfasjhfjasdhfjsahfjsahdfjh',
    }
    
    return TemplateResponse(request, 'index.html', context)
    
def page_view (request, template_path):
    return TemplateResponse(request, template_path, {})
    