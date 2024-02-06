"""
URL configuration for avaluaproy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# UD6.2.e
from django.conf import settings
from django.conf.urls.static import static

from common import views as common_views
from core import views as core_views
from programacion_didactica import views as pd_views
from login.views import LoginFormView, LogoutView, LogoutRedirectView
#UD8.4
from django.views.generic import TemplateView
from core.api.views import ModuloListViewSet, ModuloDetailViewSet, RAListViewSet, RADetailViewSet, CEListViewSet, CEDetailViewSet
from programacion_didactica.api.views import UnidadListViewSet, UnidadDetailViewSet, IEListViewSet, IEDetailViewSet, PondRAListViewSet, PondRADetailViewSet, PondCEListViewSet, PondCEDetailViewSet, PondCEUDListViewSet, PondCEUDDetailViewSet
from programacion_aula.api.views import AlumnoListViewSet, AlumnoDetailViewSet, CEUDListViewSet, CEUDDetailViewSet, CalUDCEListViewSet, CalUDCEDetailViewSet, CalCEListViewSet, CalCEDetailViewSet, CalRAListViewSet, CalRADetailViewSet, CalTotalListViewSet, CalTotalDetailViewSet
from rest_framework import routers

#UD10.3.a
#####################################
##   API VIEWS     -       CORE    ##
#####################################
router = routers.DefaultRouter()
router.register(r'modulo_list', ModuloListViewSet, basename='modulo_list')
router.register(r'modulo_detail', ModuloDetailViewSet, basename='modulo_detail')
router.register(r'ra_list', RAListViewSet, basename='ra_list')
router.register(r'ra_detail', RADetailViewSet, basename='ra_detail')
router.register(r'ce_list', CEListViewSet, basename='ce_list')
router.register(r'ce_detail', CEDetailViewSet, basename='ce_detail')
###############################################
##   API VIEWS     -       PROG_DIDACTICA    ##
###############################################
router.register(r'ud_list', UnidadListViewSet, basename='ud_list')
router.register(r'ud_detail', UnidadDetailViewSet, basename='ud_detail')
router.register(r'ie_list', IEListViewSet, basename='ie_list')
router.register(r'ie_detail', IEDetailViewSet, basename='ie_detail')
router.register(r'pond_ra_list', PondRAListViewSet, basename='pond_ra_list')
router.register(r'pond_ra_detail', PondRADetailViewSet, basename='pond_ra_detail')
router.register(r'pond_ce_list', PondCEListViewSet, basename='pond_ce_list')
router.register(r'pond_ce_detail', PondCEDetailViewSet, basename='pond_ce_detail')
router.register(r'pond_ce_ud_list', PondCEUDListViewSet, basename='pond_ce_ud_list')
router.register(r'pond_ce_ud_detail', PondCEUDDetailViewSet, basename='pond_ce_ud_detail')
##########################################
##   API VIEWS     -       PROG_AULA    ##
##########################################
router.register(r'alu_list', AlumnoListViewSet, basename='alu_list')
router.register(r'alu_detail', AlumnoDetailViewSet, basename='alu_detail')
router.register(r'ce_ud_list', CEUDListViewSet, basename='ce_ud_list')
router.register(r'ce_ud_detail', CEUDDetailViewSet, basename='ce_ud_detail')
router.register(r'cal_ud_ce_list', CalUDCEListViewSet, basename='cal_ud_ce_list')
router.register(r'cal_ud_ce_detail', CalUDCEDetailViewSet, basename='cal_ud_ce_detail')
router.register(r'cal_ce_list', CalCEListViewSet, basename='cal_ce_list')
router.register(r'cal_ce_detail', CalCEDetailViewSet, basename='cal_ce_detail')
router.register(r'cal_ra_list', CalRAListViewSet, basename='cal_ra_list')
router.register(r'cal_ra_detail', CalRADetailViewSet, basename='cal_ra_detail')
router.register(r'cal_total_list', CalTotalListViewSet, basename='cal_total_list')
router.register(r'cal_total_detail', CalTotalListViewSet, basename='cal_total_detail')

# UD6.7.b
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),
    #UD7.2.b
    path('modulo_list/', core_views.ModuloListView.as_view(), name='modulo_list'),
    path('modulo_detail/<int:pk>/', core_views.ModuloDetailView.as_view(), name='modulo_detail'),
    path('modulo_create/', core_views.ModCreateView.as_view(), name='modulo_create'),
    path('modulo_update/<int:pk>/', core_views.ModUpdateView.as_view(), name='modulo_update'),
    path('modulo_delete/<int:pk>/', core_views.ModDeleteView.as_view(), name='modulo_delete'),
    #UD7.2.b
    path('ra_list/', core_views.RAListView.as_view(), name='ra_list'),
    path('ra_detail/<int:pk>/', core_views.RADetailView.as_view(), name='ra_detail'),
    path('ra_create', core_views.RACreateView.as_view(), name='ra_create'),
    path('ra_update/<int:pk>/', core_views.RAUpdateView.as_view(), name='ra_update'),
    path('ra_delete/<int:pk>/', core_views.RADeleteView.as_view(), name='ra_delete'),
    #UD7.2.b
    path('ce_list/', core_views.CEListView.as_view(), name='ce_list'),
    path('ce_detail/<int:pk>/', core_views.CEDetailView.as_view(), name='ce_detail'),
    path('ce_create', core_views.CECreateView.as_view(), name='ce_create'),
    path('ce_update/<int:pk>/', core_views.CEUpdateView.as_view(), name='ce_update'),
    path('ce_delete/<int:pk>/', core_views.CEDeleteView.as_view(), name='ce_delete'),
    #UD7.2.b
    path('unidad_list/', pd_views.UnidadListView.as_view(), name='unidad_list'),
    path('unidad_detail/<int:pk>/', pd_views.UnidadDetailView.as_view(), name='unidad_detail'),
    path('unidad_create', pd_views.UDCreateView.as_view(), name='unidad_create'),
    path('unidad_update/<int:pk>/', pd_views.UDUpdateView.as_view(), name='unidad_update'),
    path('unidad_delete/<int:pk>/', pd_views.UDDeleteView.as_view(), name='unidad_delete'),
    #UD7.2.b
    path('ie_list/', pd_views.InstEvListView.as_view(), name='ie_list'),
    path('ie_detail/<int:pk>/', pd_views.InstEvDetailView.as_view(), name='ie_detail'),
    path('ie_create', pd_views.InstEvaluacionCreateView.as_view(), name='ie_create'),
    path('ie_update/<int:pk>/', pd_views.InstEvaluacionUpdateView.as_view(), name='ie_update'),
    path('ie_delete/<int:pk>/', pd_views.InstEvaluacionDeleteView.as_view(), name='ie_delete'),
    #UD7.2.b
    path('pond_ra_list/', pd_views.PondRAListView.as_view(), name='pond_ra_list'),
    path('pond_ra_detail/<int:pk>/', pd_views.PondRADetailView.as_view(), name='pond_ra_detail'),
    path('pond_ra_create', pd_views.PonderacionRACreateView.as_view(), name='pond_ra_create'),
    path('pond_ra_update/<int:pk>/', pd_views.PonderacionRAUpdateView.as_view(), name='pond_ra_update'),
    path('pond_ra_delete/<int:pk>/', pd_views.PonderacionRADeleteView.as_view(), name='pond_ra_delete'),
    #UD7.2.b
    path('pond_ce_list/', pd_views.PondCritListView.as_view(), name='pond_ce_list'),
    path('pond_ce_detail/<int:pk>/', pd_views.PondCritDetailView.as_view(), name='pond_ce_detail'),
    path('pond_ce_create', pd_views.PondCriterioCreateView.as_view(), name='pond_ce_create'),
    path('pond_ce_update/<int:pk>/', pd_views.PondCriterioUpdateView.as_view(), name='pond_ce_update'),
    path('pond_ce_delete/<int:pk>/', pd_views.PondCriterioDeleteView.as_view(), name='pond_ce_delete'),
    #UD7.2.b
    path('pond_ce_ud_list/', pd_views.PondCritUDListView.as_view(), name='pond_ce_ud_list'),
    path('pond_ce_ud_detail/<int:pk>/', pd_views.PondCritUDDetailView.as_view(), name='pond_ce_ud_detail'),
    path('pond_ce_ud_create', pd_views.PondCriterioUDCreateView.as_view(), name='pond_ce_ud_create'),
    path('pond_ce_ud_update/<int:pk>/', pd_views.PondCriterioUDUpdateView.as_view(), name='pond_ce_ud_update'),
    path('pond_ce_ud_delete/<int:pk>/', pd_views.PondCriterioUDDeleteView.as_view(), name='pond_ce_ud_delete'),
    #UD8.2.b Autenticacion por medio de mi LoginForm
    path('login/', LoginFormView.as_view(), name='login'),
    #UD8.2.c
    #path('logout/', LogoutView.as_view(), name='logout')
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
    #UD8.4 Autenticacion por medio de Allauth
    path('accounts/', include('allauth.urls')),
]

# UD6.2.e
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    