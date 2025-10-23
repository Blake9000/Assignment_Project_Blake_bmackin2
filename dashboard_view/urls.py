from django.urls import path, include
from dashboard_view import views
from dashboard_view.views import dashboard_login_view, AdminServers, AdminLogSource, AdminMonitoringProbes, \
    AdminServiceTypes, AdminService, ServerAdd
from dashboard_view.views import AdminView

urlpatterns = [
    path('login/',dashboard_login_view, name='login'),
    path('admin/',AdminView.as_view(), name='admin'),

    path('admin/servers',AdminServers.as_view(), name='admin-servers'),

    path('admin/log_sources',AdminLogSource.as_view(), name='log-sources'),

    path('admin/probes',AdminMonitoringProbes.as_view(), name='admin-probes'),

    path('admin/service_types',AdminServiceTypes.as_view(), name='admin-service-types'),

    path('admin/services',AdminService.as_view(), name='admin-services'),

    path('admin/service_types/add',views.service_type_add, name='service-types-add'),

    path('admin/servers/add', ServerAdd.as_view(), name='server-add'),

]
