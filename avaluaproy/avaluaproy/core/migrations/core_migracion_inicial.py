from django.db import migrations, models
from core.models import Modulo, ResAprendizaje, CritEvaluacion

#9.3.a MIGRACIONES CORE

def migra_modulos(apps, schema_editor):
    modulo_servidor = Modulo.objects.create(codigo="0613", nombre="Desarrollo Web en Entorno Servidor")

    ra01  = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA01', descripcion='Selecciona las arquitecturas y tecnologías de programación web en entorno servidor, analizando sus capacidades y características propias')
    
    ra01_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='a', descripcion='Se han caracterizado y diferenciado los modelos de ejecución de código en el servidor y en el cliente web.', minimo=0)
    ra01_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='b', descripcion='Se han reconocido las ventajas que proporciona la generación dinámica de páginas.', minimo=0)
    ra01_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='c', descripcion='Se han identificado los mecanismos de ejecución de código en los servidores web', minimo=0)
    ra01_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='d', descripcion='Se han reconocido las funcionalidades que aportan los servidores de aplicaciones y su integración con los servidores web', minimo=0)
    ra01_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='e', descripcion='Se han identificado y caracterizado los principales lenguajes y tecnologías relacionados con la programación web en entorno servidor.', minimo=0)
    ra01_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='f', descripcion='Se han verificado los mecanismos de integración de los lenguajes de marcas con los lenguajes de programación en entorno servidor.', minimo=0)
    ra01_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra01, codigo='g', descripcion=' Se han reconocido y evaluado las herramientas y frameworks de programación en entorno servidor', minimo=0)
    
    ra02 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA02', descripcion='Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.')
    
    ra02_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='a', descripcion='Se han reconocido los mecanismos de generación de páginas web a partir de lenguajes de marcas con código embebido.', minimo=0)
    ra02_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='b', descripcion='Se han identificado las principales tecnologías asociadas.', minimo=0)
    ra02_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='c', descripcion='Se han utilizado etiquetas para la inclusión de código en el lenguaje de marcas.', minimo=0)
    ra02_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='d', descripcion='Se ha reconocido la sintaxis del lenguaje de programación que se ha de utilizar', minimo=0)
    ra02_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='e', descripcion='Se han escrito sentencias simples y se han comprobado sus efectos en el documento resultante.', minimo=0)
    ra02_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='f', descripcion='Se han utilizado directivas para modificar el comportamiento predeterminado.', minimo=0)
    ra02_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='g', descripcion='Se han utilizado los distintos tipos de variables y operadores disponibles en el lenguaje.', minimo=0)
    ra02_h = CritEvaluacion.objects.create(resultado_aprendizaje=ra02, codigo='h', descripcion='Se han identificado los ámbitos de utilización de las variables', minimo=0)
   
    ra03 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA03', descripcion='Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación')
    
    ra03_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='a', descripcion='Se han utilizado mecanismos de decisión en la creación de bloques de sentencias.', minimo=0)
    ra03_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='b', descripcion='Se han utilizado bucles y se ha verificado su funcionamiento.', minimo=0)
    ra03_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='c', descripcion='Se han utilizado matrices (arrays) para almacenar y recuperar conjuntos de datos.', minimo=0)
    ra03_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='d', descripcion='Se han creado y utilizado funciones.', minimo=0)
    ra03_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='e', descripcion='Se han utilizado formularios web para interactuar con el usuario del navegador web', minimo=0)
    ra03_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='f', descripcion='Se han empleado métodos para recuperar la información introducida en el formulario.', minimo=0)
    ra03_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra03, codigo='g', descripcion='Se han añadido comentarios al código.', minimo=0)
    
    ra04 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA04', descripcion='Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.')
    
    ra04_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='a', descripcion='Se han identificado los mecanismos disponibles para el mantenimiento de la información que concierne a un cliente web concreto y se han señalado sus ventajas.', minimo=0)
    ra04_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='b', descripcion='Se han utilizado mecanismos para mantener el estado de las aplicaciones web', minimo=0)
    ra04_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='c', descripcion='Se han utilizado mecanismos para almacenar información en el cliente web y para recuperar su contenido', minimo=0)
    ra04_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='d', descripcion='Se han identificado y caracterizado los mecanismos disponibles para la autentificación de usuarios', minimo=0)
    ra04_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='e', descripcion='Se han escrito aplicaciones que integren mecanismos de autentificación de usuarios.', minimo=0)
    ra04_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra04, codigo='f', descripcion='Se han utilizado herramientas y entornos para facilitar la programación, prueba y depuración del código.', minimo=0)
    
    ra05 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA05', descripcion='Desarrolla aplicaciones web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio')
    
    ra05_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='a', descripcion='Se han identificado las ventajas de separar la lógica de negocio de los aspectos de presentación de la aplicación', minimo=0)
    ra05_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='b', descripcion='Se han analizado y utilizado mecanismos y frameworks que permiten realizar esta separación y sus características principales.', minimo=0)
    ra05_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='c', descripcion='Se han utilizado objetos y controles en el servidor para generar el aspecto visual de la aplicación web en el cliente.', minimo=0)
    ra05_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='d', descripcion='Se han utilizado formularios generados de forma dinámica para responder a los eventos de la aplicación web.', minimo=0)
    ra05_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='e', descripcion=' Se han identificado y aplicado los parámetros relativos a la configuración de la aplicación web.', minimo=0)
    ra05_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='f', descripcion='Se han escrito aplicaciones web con mantenimiento de estado y separación de la lógica de negocio', minimo=0)
    ra05_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='g', descripcion='Se han aplicado los principios y patrones de diseño de la programación orientada a objetos.', minimo=0)
    ra05_h = CritEvaluacion.objects.create(resultado_aprendizaje=ra05, codigo='h', descripcion='Se ha probado y documentado el código.', minimo=0)

    ra06 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA06', descripcion='Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información')
    
    ra06_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='a', descripcion='Se han analizado las tecnologías que permiten el acceso mediante programación a la información disponible en almacenes de datos.', minimo=0)
    ra06_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='b', descripcion='Se han creado aplicaciones que establezcan conexiones con bases de datos.', minimo=0)
    ra06_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='c', descripcion='Se ha recuperado información almacenada en bases de datos.', minimo=0)
    ra06_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='d', descripcion='Se ha publicado en aplicaciones web la información recuperada.', minimo=0)
    ra06_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='e', descripcion='Se han utilizado conjuntos de datos para almacenar la información.', minimo=0)
    ra06_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='f', descripcion='Se han creado aplicaciones web que permitan la actualización y la eliminación de información disponible en una base de datos', minimo=0)
    ra06_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra06, codigo='g', descripcion='Se han probado y documentado las aplicaciones web.', minimo=0)
    
    ra07 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA07', descripcion='Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información')
    
    ra07_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='a', descripcion='Se han reconocido las características propias y el ámbito de aplicación de los servicios web.', minimo=0)
    ra07_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='b', descripcion='Se han reconocido las ventajas de utilizar servicios web para proporcionar acceso a funcionalidades incorporadas a la lógica de negocio de una aplicación.', minimo=0)
    ra07_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='c', descripcion='Se han identificado las tecnologías y los protocolos implicados en el consumo de servicios web.', minimo=0)
    ra07_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='d', descripcion='Se han utilizado los estándares y arquitecturas más difundidos e implicados en el desarrollo de servicios web.', minimo=0)
    ra07_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='e', descripcion='Se ha programado un servicio web.', minimo=0)
    ra07_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='f', descripcion='Se ha verificado el funcionamiento del servicio web.', minimo=0)
    ra07_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='g', descripcion='Se ha consumido el servicio web.', minimo=0)
    ra07_h = CritEvaluacion.objects.create(resultado_aprendizaje=ra07, codigo='h', descripcion='Se ha documentado un servicio web', minimo=0)

    ra08 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA08', descripcion='Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas')
    
    ra08_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='a', descripcion='Se han identificado las diferencias entre la ejecución de código en el servidor y en el cliente web.', minimo=0)
    ra08_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='b', descripcion='Se han reconocido las ventajas de unir ambas tecnologías en el proceso de desarrollo de programas', minimo=0)
    ra08_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='c', descripcion='Se han identificado las tecnologías y frameworks relacionadas con la generación por parte del servidor de páginas web con guiones embebidos', minimo=0)
    ra08_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='d', descripcion='Se han utilizado estas tecnologías y frameworks para generar páginas web que incluyan interacción con el usuario.', minimo=0)
    ra08_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='e', descripcion='Se han utilizado estas tecnologías y frameworks, para generar páginas web que incluyan verificación de formularios', minimo=0)
    ra08_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='f', descripcion=' Se han utilizado estas tecnologías y frameworks para generar páginas web que incluyan modificación dinámica de su contenido y su estructura.', minimo=0)
    ra08_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra08, codigo='g', descripcion='Se han aplicado estas tecnologías y frameworks en la programación de aplicaciones web', minimo=0)
    
    ra09 = ResAprendizaje.objects.create(modulo = modulo_servidor, codigo='RA09', descripcion='Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas')
    
    ra09_a = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='a', descripcion='Se han reconocido las ventajas que proporciona la reutilización de código y el aprovechamiento de información ya existente', minimo=0)
    ra09_b = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='b', descripcion='Se han identificado tecnologías y frameworks aplicables en la creación de aplicaciones web híbridas', minimo=0)
    ra09_c = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='c', descripcion='Se ha creado una aplicación web que recupere y procese repositorios de información ya existentes..', minimo=0)
    ra09_d = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='d', descripcion='Se han creado repositorios específicos a partir de información existente en almacenes de información', minimo=0)
    ra09_e = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='e', descripcion='Se han utilizado librerías de código y frameworks para incorporar funcionalidades específicas a una aplicación web.', minimo=0)
    ra09_f = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='f', descripcion='Se han programado servicios y aplicaciones web utilizando como base información y código generados por terceros.', minimo=0)
    ra09_g = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='g', descripcion='Se han analizado y utilizado librerías de código relacionadas con Big Data e inteligencia de negocios, para incorporar análisis e inteligencia de datos proveniente de repositorios.', minimo=0)
    ra09_h = CritEvaluacion.objects.create(resultado_aprendizaje=ra09, codigo='h', descripcion='Se han probado, depurado y documentado las aplicaciones generadas', minimo=0)


class Migration(migrations.Migration):

    dependencies = [('core', '0001_initial')]

    operations = [
        migrations.RunPython(migra_modulos),
            ]