from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

# Create your views here.

def dashboard_login_view(request):
    template = loader.get_template('dashboard_view/dashboard_view_login.html')
    output = template.render()
    return HttpResponse(output)


class SettingsView(TemplateView):
    template_name = 'dashboard_view/settings.html'