from django.urls import path, include
from dashboard_view import views
from dashboard_view.views import dashboard_login_view, AdminServers, AdminLogSource, AdminMonitoringProbes, \
    AdminServiceTypes, AdminService, server_add, monitoring_probe_add
from dashboard_view.views import AdminView, generic_delete

urlpatterns = [
    path('login/',dashboard_login_view, name='login'),
    path('admin/',AdminView.as_view(), name='admin'),

    path('admin/servers',AdminServers.as_view(), name='admin-servers'),

    path('admin/log_sources',AdminLogSource.as_view(), name='log-sources'),

    path('admin/probes',AdminMonitoringProbes.as_view(), name='admin-probes'),

    path('admin/service_types',AdminServiceTypes.as_view(), name='admin-service-types'),

    path('admin/services',AdminService.as_view(), name='admin-services'),

    path('admin/service_types/add',views.service_type_add, name='service-types-add'),

    path('admin/servers/add', views.server_add, name='server-add'),

    path('admin/probes/add',views.monitoring_probe_add, name='monitoring-probe-add'),

    path('admin/services/add', views.service_add, name='service-add'),

    path('admin/log_sources/add', views.log_source_add, name='log-sources-add'),

    path("delete/<str:app>/<str:model>/<int:pk>/",generic_delete, name="generic-delete"),

]
