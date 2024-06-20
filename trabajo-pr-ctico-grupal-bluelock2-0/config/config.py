import configparser

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Agregar secciones y configuraciones
config['ENV'] = {
    'query_interval': '10',
    'tmp': './temp',
    'output': './salida'
}

config['TELAM'] = {
    'url_base': 'https://www.telam.com.ar',
    'ultimas_noticias': '/rss2/ultimasnoticias.xml',
    'politica': '/rss2/politica.xml',
    'economia': '/rss2/economia.xml',
    'sociedad': '/rss2/sociedad.xml',
    'deportes': '/rss2/deportes.xml',
    'policiales': '/rss2/policiales.xml',
    'internacional':'/rss2/internacional.xml',
    'latinoamerica': '/rss2/latinoamerica.xml',
    'cono_sur': '/rss2/conosur.xml',
    'provincias': '/rss2/provincias.xml',
    'agropecuario': '/rss2/agropecuario.xml',
    'tecnologia': '/rss2/tecnologia.xml',
    'cultura': '/rss2/cultura.xml',
    'espectaculos': '/rss2/espectaculos.xml',
    'turismo': '/rss2/turismo.xml',
    'salud': '/rss2/salud.xml',
    'educacion': '/rss2/educacion.xml',
    'redes': '/rss2/redes.xml'
}

config['CLARIN'] = {
    'url_base': 'https://www.clarin.com',
    'lo_ultimo': '/rss/lo-ultimo/',
    'politica': '/rss/politica/',
    'mundo': '/rss/mundo/',
    'sociedad': '/rss/sociedad/',
    'policiales': '/rss/policiales/',
    'ciudades': '/rss/ciudades/',
    'opinion':	'/rss/opinion/',
    'cartas_al_pais': '/rss/cartas_al_pais/',
    'cultura': '/rss/cultura/',
    'rural': '/rss/rural/',
    'economia': '/rss/economia/',
    'tecnologia': '/rss/tecnologia/',
    'internacional' : '/rss/internacional/',
    'revista_enie' : '/rss/revista-enie/',
    'viva' : '/rss/viva/',
    'clarin_em_portugues' : '/rss/br/',
    'futbol' : '/rss/deportes/',
    'fama' : '/rss/espectaculos/fama/',
    'tv' : '/rss/espectaculos/tv/',
    'cine' : '/rss/espectaculos/cine/',
    'musica' : 	'/rss/espectaculos/musica/',
    'teatro' : '/rss/espectaculos/teatro/',
    'espectaculos' : '/rss/espectaculos/',
    'autos' : '/rss/autos/',
    'buena_vida' : 'rss/buena-vida/',
    'viajes' : '/rss/viajes/'
}

config['LA_NACION'] = {
    'url_base': 'https://www.lanacion.com.ar',
    'ultimas_noticias': '/arc/outboundfeeds/rss/?outputType=xml',
}

config['LA_GACETA'] = {
    'url_base': 'https://www.lagaceta.com.ar',
    'ultimas_noticias': '/rss',
}

config['LA_VOZ'] = {
    'url_base': 'https://www.lavoz.com.ar',
    'ultimas_noticias': '/arc/outboundfeeds/feeds/rss/?outputType=xml',
}

config['PAGINA12'] = {
    'url_base': 'https://www.pagina12.com.ar',
    'portada': '/rss/portada',
    'espectaculos': '/rss/suplementos/cultura-y-espectaculos/notas',
    'el_pais': '/rss/secciones/el-pais/notas',
    'economia': '/rss/secciones/economia/notas',
    'sociedad':  '/rss/secciones/sociedad/notas',
    'el_mundo':  '/rss/secciones/el-mundo/notas',
    'deportes': '/rss/secciones/deportes/notas',
    'cultura': '/rss/secciones/cultura/notas',
    'universidad': '/rss/secciones/universidad/notas',
    'ciencia': '/rss/secciones/ciencia/notas',
    'psicologia': '/rss/secciones/psicologia/notas',
    'ajedrez': '/rss/secciones/ajedrez/notas',
    'la_ventana': '/rss/secciones/la-ventana/notas'
}

config['CRONICA'] = {
    'url_base': 'https://www.diariocronica.com.ar',
    'actualidad': '/rss/actualidad/',
    'tecno_ocio_ciencia': '/rss/tecno-ocio-ciencia/',
    'cultura': '/rss/cultura/',
    'policiales': '/rss/policiales/',
    'deportes': '/rss/deportes/',
    'sociedad': '/rss/sociedad/',
    'economia': '/rss/economia/',
    'politica': '/rss/politica/',
    'columnistas': '/rss/columnistas/',
    'energia': '/rss/energia/',
    'opinion': '/rss/opinion/',
    'ultimas_noticias': '/rss/noticias/'
}

# Guardar la configuracion en un archivo
with open('config.ini', 'w') as configfile:
    config.write(configfile)