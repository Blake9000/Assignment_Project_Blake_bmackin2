from django.contrib.auth.views import LogoutView
from django.urls import path, include
from dashboard_view import views
from dashboard_view.views import AdminServers, AdminLogSource, AdminMonitoringProbes, \
    AdminServiceTypes, AdminService, server_add, monitoring_probe_add, DashboardAPI, overviewChart, site_login, \
    ReportsView, export_csv, export_json
from dashboard_view.views import AdminView, generic_delete


urlpatterns = [
    path('login/', views.site_login, name='login'),
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

    path("api/",DashboardAPI.as_view(), name="api"),

    path('api/chart/',overviewChart, name='api-chart'),

    path('weather/', views.weather, name='api-weather'),

    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),

    path("reports/", ReportsView.as_view(), name="reports"),

    path('export/export.csv', export_csv, name='export-csv'),

    path('export/export.json',export_json, name='export-json'),

]
