from core.models import Modulo, CritEvaluacion, ResAprendizaje
from programacion_didactica.models import InstEvaluacion, PondRA, PondCriterio

# UD 6.6

class actividadORM ():

    def get_modulos_all():
        return Modulo.objects.all()

    def get_ie_3():
        return InstEvaluacion.objects.all()[:3]

    def get_crit_min():
        return CritEvaluacion.objects.filter(minimo=True)

    def get_ra_not_RA6():
        return ResAprendizaje.objects.exclude(codigo__contains='RA6')

    def get_ie_I1_defensa():
        return InstEvaluacion.objects.filter(codigo='I1', nombre__contains='defensa')
        
    def get_mod_id_lt_2_cod_des():
        return Modulo.objects.filter(id__lt=2).order_by('-codigo')

    def get_mod_id_gt_2():
        return Modulo.objects.filter(id__gt=2)

    def get_mod_des_nom_des():
        return Modulo.objects.filter(nombre__contains='desarrollo').order_by('nombre')

    def get_ra_not_RA1():
        return ResAprendizaje.objects.exclude(codigo__contains='%1')

    def get_ra_cli_RA3():
        objetoQuery = ResAprendizaje.objects.filter(modulo__nombre__contains='cliente', codigo__endswith='3').first()
        return objetoQuery

    def get_ce_RA06_not_cli():
        return CritEvaluacion.objects.filter(resultado_aprendizaje__codigo__contains='6').exclude(resultado_aprendizaje__modulo__nombre='cliente')

    def get_pon_ra_gt_5():
        return PondRA.objects.filter(porcentaje__gte=5)

    def get_ce_5_10_RA1():
        return PondCriterio.objects.filter(criterio_evaluacion__porcentaje__range=(5,10), criterio_evaluacion__resultado_aprendizaje__codigo__endswith='1',criterio_evaluacion__resultado_aprendizaje__modulo__codigo='6')
         # ME DA PROBLEMAS CON LA SANGRIA Y NO SE PORQUE

    def create_ie12():
        return InstEvaluacion.objects.create(codigo = 'I12', nombre = 'Nuevo Instrumento 12', descripcion = 'Nuevo Instrumento 12')

    # 15 no la tengo

    def update_last_ud():
        auxiliar = Unidad.objects.last()
        auxiliar.nombre = auxiliar.nombre+'ultima'
        auxiliar.save()

    # 17 - 20 no las tengo

