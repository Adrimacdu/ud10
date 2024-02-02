from django.db import migrations, models
from core.models import *
from programacion_didactica.models import *

#9.3.b MIGRACIONES PROG_DIDACTICA

def migracion_didactica(apps, schema_editor):

    inst_evaluacion1 = InstEvaluacion.objects.create(codigo= 1, nombre="Examen", descripcion="Examenes para evaluar conocimientos del alumno" )
    inst_evaluacion2 = InstEvaluacion.objects.create(codigo= 2, nombre="Practicas", descripcion="Actividades para poner a prueba los conocimientos adquiridos" )



    ra01 = ResAprendizaje.objects.get(codigo='RA01')
    ra02 = ResAprendizaje.objects.get(codigo='RA02')
    ra03 = ResAprendizaje.objects.get(codigo='RA03')
    ra04 = ResAprendizaje.objects.get(codigo='RA04')
    ra05 = ResAprendizaje.objects.get(codigo='RA05')
    ra06 = ResAprendizaje.objects.get(codigo='RA06')
    ra07 = ResAprendizaje.objects.get(codigo='RA07')
    ra08 = ResAprendizaje.objects.get(codigo='RA08')
    ra09 = ResAprendizaje.objects.get(codigo='RA09')


    pondRA01 = PondRA.objects.create(resultado_aprendizaje=ra01, porcentaje=2.5)
    pondRA02 = PondRA.objects.create(resultado_aprendizaje=ra02, porcentaje=2.5)
    pondRA03 = PondRA.objects.create(resultado_aprendizaje=ra03, porcentaje=10)
    pondRA04 = PondRA.objects.create(resultado_aprendizaje=ra04, porcentaje=20)
    pondRA05 = PondRA.objects.create(resultado_aprendizaje=ra05, porcentaje=15)
    pondRA06 = PondRA.objects.create(resultado_aprendizaje=ra06, porcentaje=15)
    pondRA07 = PondRA.objects.create(resultado_aprendizaje=ra07, porcentaje=25)
    pondRA08 = PondRA.objects.create(resultado_aprendizaje=ra08, porcentaje=5)
    pondRA09 = PondRA.objects.create(resultado_aprendizaje=ra09, porcentaje=5)


    ce_a_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='a')
    ce_b_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='b')
    ce_c_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='c')
    ce_d_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='d')
    ce_e_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='e')
    ce_f_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='f')
    ce_g_RA01 = CritEvaluacion.objects.get(resultado_aprendizaje=ra01, codigo='g')
    

    pond_ce_a_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA01, porcentaje=14.3)
    pond_ce_b_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA01, porcentaje=14.3)
    pond_ce_c_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA01, porcentaje=14.3)
    pond_ce_d_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA01, porcentaje=14.3)
    pond_ce_e_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA01, porcentaje=14.3)
    pond_ce_f_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA01, porcentaje=14.3)
    pond_ce_g_RA01 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA01, porcentaje=14.3)
    

    ce_a_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='a')
    ce_b_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='b')
    ce_c_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='c')
    ce_d_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='d')
    ce_e_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='e')
    ce_f_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='f')
    ce_g_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='g')
    ce_h_RA02 = CritEvaluacion.objects.get(resultado_aprendizaje=ra02, codigo='h')

    pond_ce_a_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA02, porcentaje=12.5)
    pond_ce_b_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA02, porcentaje=12.5)
    pond_ce_c_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA02, porcentaje=12.5)
    pond_ce_d_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA02, porcentaje=12.5)
    pond_ce_e_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA02, porcentaje=12.5)
    pond_ce_f_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA02, porcentaje=12.5)
    pond_ce_g_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA02, porcentaje=12.5)
    pond_ce_h_RA02 = PondCriterio.objects.create(criterio_evaluacion=ce_h_RA02, porcentaje=12.5)


    ce_a_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='a')
    ce_b_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='b')
    ce_c_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='c')
    ce_d_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='d')
    ce_e_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='e')
    ce_f_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='f')
    ce_g_RA03 = CritEvaluacion.objects.get(resultado_aprendizaje=ra03, codigo='g')
    

    pond_ce_a_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA03, porcentaje=10.0)
    pond_ce_b_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA03, porcentaje=5.0)
    pond_ce_c_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA03, porcentaje=30.0)
    pond_ce_d_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA03, porcentaje=5.0)
    pond_ce_e_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA03, porcentaje=30.0)
    pond_ce_f_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA03, porcentaje=15.0)
    pond_ce_g_RA03 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA03, porcentaje=5.0)
    

    ce_a_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='a')
    ce_b_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='b')
    ce_c_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='c')
    ce_d_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='d')
    ce_e_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='e')
    ce_f_RA04 = CritEvaluacion.objects.get(resultado_aprendizaje=ra04, codigo='f')
    

    pond_ce_a_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA04, porcentaje=5.0)
    pond_ce_b_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA04, porcentaje=5.0)
    pond_ce_c_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA04, porcentaje=5.0)
    pond_ce_d_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA04, porcentaje=5.0)
    pond_ce_e_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA04, porcentaje=55.0)
    pond_ce_f_RA04 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA04, porcentaje=25.0)
    

    ce_a_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='a')
    ce_b_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='b')
    ce_c_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='c')
    ce_d_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='d')
    ce_e_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='e')
    ce_f_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='f')
    ce_g_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='g')
    ce_h_RA05 = CritEvaluacion.objects.get(resultado_aprendizaje=ra05, codigo='h')


    pond_ce_a_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA05, porcentaje=2.5)
    pond_ce_b_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA05, porcentaje=2.5)
    pond_ce_c_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA05, porcentaje=10.0)
    pond_ce_d_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA05, porcentaje=30.0)
    pond_ce_e_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA05, porcentaje=10.0)
    pond_ce_f_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA05, porcentaje=35.0)
    pond_ce_g_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA05, porcentaje=5.0)
    pond_ce_h_RA05 = PondCriterio.objects.create(criterio_evaluacion=ce_h_RA05, porcentaje=5.0)


    ce_a_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='a')
    ce_b_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='b')
    ce_c_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='c')
    ce_d_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='d')
    ce_e_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='e')
    ce_f_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='f')
    ce_g_RA06 = CritEvaluacion.objects.get(resultado_aprendizaje=ra06, codigo='g')
    

    pond_ce_a_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA06, porcentaje=5.0)
    pond_ce_b_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA06, porcentaje=5.0)
    pond_ce_c_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA06, porcentaje=30.0)
    pond_ce_d_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA06, porcentaje=12.5)
    pond_ce_e_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA06, porcentaje=12.5)
    pond_ce_f_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA06, porcentaje=30.0)
    pond_ce_g_RA06 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA06, porcentaje=5.0)
    

    ce_a_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='a')
    ce_b_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='b')
    ce_c_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='c')
    ce_d_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='d')
    ce_e_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='e')
    ce_f_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='f')
    ce_g_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='g')
    ce_h_RA07 = CritEvaluacion.objects.get(resultado_aprendizaje=ra07, codigo='h')


    pond_ce_a_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA07, porcentaje=2.5)
    pond_ce_b_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA07, porcentaje=2.5)
    pond_ce_c_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA07, porcentaje=2.5)
    pond_ce_d_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA07, porcentaje=2.5)
    pond_ce_e_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA07, porcentaje=75.0)
    pond_ce_f_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA07, porcentaje=5.0)
    pond_ce_g_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA07, porcentaje=5.0)
    pond_ce_h_RA07 = PondCriterio.objects.create(criterio_evaluacion=ce_h_RA07, porcentaje=5.0)


    ce_a_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='a')
    ce_b_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='b')
    ce_c_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='c')
    ce_d_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='d')
    ce_e_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='e')
    ce_f_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='f')
    ce_g_RA08 = CritEvaluacion.objects.get(resultado_aprendizaje=ra08, codigo='g')
    

    pond_ce_a_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA08, porcentaje=14.3)
    pond_ce_b_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA08, porcentaje=14.3)
    pond_ce_c_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA08, porcentaje=14.3)
    pond_ce_d_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA08, porcentaje=14.3)
    pond_ce_e_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA08, porcentaje=14.3)
    pond_ce_f_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA08, porcentaje=14.3)
    pond_ce_g_RA08 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA08, porcentaje=14.3)
    

    ce_a_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='a')
    ce_b_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='b')
    ce_c_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='c')
    ce_d_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='d')
    ce_e_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='e')
    ce_f_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='f')
    ce_g_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='g')
    ce_h_RA09 = CritEvaluacion.objects.get(resultado_aprendizaje=ra09, codigo='h')


    pond_ce_a_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_a_RA09, porcentaje=12.5)
    pond_ce_b_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_b_RA09, porcentaje=12.5)
    pond_ce_c_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_c_RA09, porcentaje=12.5)
    pond_ce_d_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_d_RA09, porcentaje=12.5)
    pond_ce_e_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_e_RA09, porcentaje=12.5)
    pond_ce_f_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_f_RA09, porcentaje=12.5)
    pond_ce_g_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_g_RA09, porcentaje=12.5)
    pond_ce_h_RA09 = PondCriterio.objects.create(criterio_evaluacion=ce_h_RA09, porcentaje=12.5)


    unidad1 = Unidad.objects.create(codigo='ud1', nombre='Arquitecturas y tecnologías web')


    pond_ce_a_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_b_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_c_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_d_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_e_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_f_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA01, unidad=unidad1, porcentaje=100)

    pond_ce_g_ud1_ra01 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA01, unidad=unidad1, porcentaje=100)


    unidad2 = Unidad.objects.create(codigo='ud2', nombre='Fundamentos de programación web ')


    pond_ce_a_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_b_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_c_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_d_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_e_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_f_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_g_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA02, unidad=unidad2, porcentaje=100)

    pond_ce_h_ud2_ra02 = PondCritUD.objects.create(criterio_evaluacion=ce_h_RA02, unidad=unidad2, porcentaje=100)


    unidad3 = Unidad.objects.create(codigo='ud3', nombre='Portfolio - Estructuras de control')

    pond_ce_a_ud3_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA03, unidad=unidad3, porcentaje=100)

    pond_ce_b_ud3_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA03, unidad=unidad3, porcentaje=100)

    pond_ce_c_ud3_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA03, unidad=unidad3, porcentaje=100)

    pond_ce_d_ud3_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA03, unidad=unidad3, porcentaje=100)

    pond_ce_g_ud3_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA03, unidad=unidad3, porcentaje=100)


    unidad4 = Unidad.objects.create(codigo='ud4', nombre='Portfolio - Estructuras de datos y formularios')


    pond_ce_e_ud4_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA03, unidad=unidad4, porcentaje=100)

    pond_ce_f_ud4_ra03 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA03, unidad=unidad4, porcentaje=100)
    
    pond_ce_a_ud4_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA04, unidad=unidad4, porcentaje=100)

    pond_ce_b_ud4_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA04, unidad=unidad4, porcentaje=100)

    pond_ce_c_ud4_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA04, unidad=unidad4, porcentaje=100)


    unidad5 = Unidad.objects.create(codigo='ud5', nombre='Portfolio - Acceso a datos y objetos del navegador')


    pond_ce_a_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA06, unidad=unidad5, porcentaje=50)

    pond_ce_b_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA06, unidad=unidad5, porcentaje=33)

    pond_ce_c_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA06, unidad=unidad5, porcentaje=50)

    pond_ce_d_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA06, unidad=unidad5, porcentaje=50)

    pond_ce_e_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA06, unidad=unidad5, porcentaje=50)

    pond_ce_f_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA06, unidad=unidad5, porcentaje=33)

    pond_ce_g_ud5_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA06, unidad=unidad5, porcentaje=100)


    unidad6 = Unidad.objects.create(codigo='ud6', nombre='Multicapa - Datos y modelo de objetos del documento')

    pond_ce_a_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA05, unidad=unidad6, porcentaje=100)

    pond_ce_b_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA05, unidad=unidad6, porcentaje=100)

    pond_ce_e_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA05, unidad=unidad6, porcentaje=50)

    pond_ce_f_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA05, unidad=unidad6, porcentaje=100)

    pond_ce_g_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA05, unidad=unidad6, porcentaje=100)

    pond_ce_h_ud6_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_h_RA05, unidad=unidad6, porcentaje=50)

    pond_ce_a_ud6_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA06, unidad=unidad6, porcentaje=50)

    pond_ce_b_ud6_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA06, unidad=unidad6, porcentaje=33)

    pond_ce_c_ud6_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA06, unidad=unidad6, porcentaje=50)

    pond_ce_d_ud6_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA06, unidad=unidad6, porcentaje=50)

    pond_ce_e_ud6_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA06, unidad=unidad6, porcentaje=50)


    unidad7 = Unidad.objects.create(codigo='ud7', nombre='Multicapa - Vistas y controladores, eventos e interactividad')


    pond_ce_c_ud7_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA05, unidad=unidad7, porcentaje=100)

    pond_ce_d_ud7_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA05, unidad=unidad7, porcentaje=100)

    pond_ce_h_ud7_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_h_RA05, unidad=unidad7, porcentaje=50)
    
    pond_ce_a_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_b_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_c_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_d_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_e_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_f_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_g_ud7_ra08 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA08, unidad=unidad7, porcentaje=100)

    pond_ce_f_ud7_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA06, unidad=unidad7, porcentaje=33)




    unidad8 = Unidad.objects.create(codigo='ud8', nombre='Multicapa - Autentificación y seguridad')


    pond_ce_d_ud8_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA04, unidad=unidad8, porcentaje=50)

    pond_ce_e_ud8_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA04, unidad=unidad8, porcentaje=50)

    pond_ce_e_ud8_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA09, unidad=unidad8, porcentaje=50)


    unidad9 = Unidad.objects.create(codigo='ud9', nombre='Servicios web - Introducción y consumo')


    pond_ce_e_ud9_ra05 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA05, unidad=unidad9, porcentaje=50)

    pond_ce_b_ud9_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA06, unidad=unidad9, porcentaje=33)

    pond_ce_f_ud9_ra06 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA06, unidad=unidad9, porcentaje=100)

    pond_ce_g_ud9_RA06 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA06, unidad=unidad6, porcentaje=50)



    unidad10 = Unidad.objects.create(codigo='ud10', nombre='Servicios web y aplicaciones web reactiva')


    pond_ce_a_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_b_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_c_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_d_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_e_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_f_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA07, unidad=unidad10, porcentaje=100)

    pond_ce_h_ud10_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_h_RA07, unidad=unidad10, porcentaje=100)




    unidad11 = Unidad.objects.create(codigo='ud11', nombre='Servicios web - Autentificación y seguridad')


    pond_ce_d_ud11_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA04, unidad=unidad11, porcentaje=50)
    
    pond_ce_e_ud11_ra04 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA04, unidad=unidad11, porcentaje=50)

    pond_ce_g_ud11_ra07 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA07, unidad=unidad11, porcentaje=100)


    unidad12 = Unidad.objects.create(codigo='ud12', nombre='Aplicaciones web híbridas')



    pond_ce_a_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_a_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_b_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_b_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_c_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_c_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_d_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_d_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_e_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_e_RA09, unidad=unidad12, porcentaje=50)

    pond_ce_f_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_f_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_g_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_g_RA09, unidad=unidad12, porcentaje=100)

    pond_ce_h_ud12_ra09 = PondCritUD.objects.create(criterio_evaluacion=ce_h_RA09, unidad=unidad12, porcentaje=100)

    
    


    
    
    
    

    
    
    
    
   
    
   
    
  
   
    
    
        
    

        

        

        

    
    


    

    

    

    

    

    

    
    

    

    

    

    

    

    
    
    

    

    

class Migration(migrations.Migration):

    dependencies = [('programacion_didactica', '0001_initial')]

    operations = [
        migrations.RunPython(migracion_didactica),
            ]