# -*- coding: utf-8 -*-
# Version 1.1
# Changelog:
#   - Agregamos comillas simples y otros (\x91, \x92, \x85), 
#     stopwords = [ciento, pregunta, preguntamos, preguntar, pregunto,quieren,no,'podemos','podriamos',
#     trato,mil,miles,s,diputadas,diputades,
#     gente, hicimos,hicieron,hacemos, haran,haremos,hiciese, hiciesen, hizo, saber,saben,sabiamos,
#     siempre, nunca, oportunidad, plantearon, planteamos,importancia,mal,menos,mas,'tal']
#     agregamos 'Artículo. -' a reemplazos()      
import nltk
nltk.download('stopwords')

from string import punctuation
import re
import unicodedata

print('Gracias por usar nuestro módulo MF')

# Stopword de nltk
spanish_stopwords = nltk.corpus.stopwords.words('spanish')

# Agregamos palabras que nos queremos sacar de encima, porque no aportan a la
#  estructura de topicos o son muy frecuentes. 
new_stopwords = ['abajo','absoluta','absolutas','absolutamente','absoluto','absolutos','acá','acabar','acaba','acabamos','acaban',
'acabe','acabé','acaben','acabo','acabó','aclarar','aclara','aclaran','aclare','aclaré','aclaren',
'aclaro','aclaró','aires','acompañar','acompañe','acompañé','acompañamos','acompaño','acompañó','adelante','además',
'afortunada','afortunadas','afortunadamente','afortunado','afortunados','agradecer','agradece','agradecí','agradecida','agradecidas',
'agradecido','agradecidos','agradezco','agregar','agrego','agregó','agregue',
'agregué','ahí','ahora','alguien','algún','alguna','algunas','alguno','algunos','allá','allí','año','años',
'aplauso','aplausos','aquel','aquella','aquélla','aquellas','aquéllas','aquello','aquéllo','aquellos','aquéllos','aquí',
'argentina','argentinas','argentino','argentinos','artículo','artículos','así','atrás','aún',
'aunque',

'b','bajo','basta','bastante','bastantes','bloque','breve','brevemente','buen','buena','buenas','bueno','buenos',

'c','cada','cámara','carlos','casi','catorce','cero','ciento','cientos','cien','cierta','ciertas','cierto','ciertos',
'cinco','cincuenta','ciudad','claro','comienza','comienzo','comisión','cómo',
'común','comunes','congreso','considera','consideran','considere','consideré','considero',
'consideró','contra','conveniente','conviene','cosa','cosas','crea','cree','creemos','creer','creo','cuál','cuales',
'cuáles','cualquier','cualquiera','cuándo','cuanto','cuánto','cuantos','cuántos','cuarenta','cuatro','cuestión',
'cuya','cuyas','cuyos',

'd','da','damos','dando','daniel','dar','darle','darles','darse','dada','dadas','dado','dados','dar','dará','daré','dé',
'deba','debajo','debe','debemos','debo','debían','decir','decía','deja','dejá','dejan','dejar','dejaron','deje',
'dejé','dejo','dejó','demás','demos','den','dentro''des','dés','desear','desea','desean','deseé','deseó','detrás',
'di','dieciocho','dieciséis','diecisiete','dice','dicen','dicha','dicho','dichos','dieron','dimos','dió','dirá',
'diré','don','doscientos','doy','despues','después','día','días','dictamen','diez','dice','dije','dijera','dijeran',
'dijeron','dijo','digo','digan','díganle','diputada','diputadas','diputado','diputados','diputades','don','donde','dónde',
'doña','dos','duda',

'e','eduardo','efectivamente','ejecutar','ejecute','ejecuté','ejecuten','ejecuto','ejecutó','ejemplo','ejemplos',
'elemental','ella','ellas','elle','elles','ello','ellos','encima','ende','énfasis','enorme',
'entonces','es','esa','esas','ese','eso','esos','escuchar','escucho','escuchó',
'escucha','escuche','escuché','escuchamos','escuchen','espera','esperaba','esperar','espere','esta','está','ésta','estas',
'éstas','establece','establecen','establecer','este','éste','esté','esto','ésto','estos','éstos','etc','etcétera',
'eternamente','eventual','eventualmente','evidente','evidentemente','ex','expediente','expedientes','extra','extras',
'extraña','extrañas','extraño','extraños','extraordinaria','extraordinarias','extraordinario','extraordinarios',
'extrema','extremas','extremo','extremos',

'fácil','fáciles','fenomenal','fundamental',

'g','gente','gentes','gobierno','gran','grande','grandes','grandioso','gusta','gustar','gustaron','gustó',

'h','haber','habeas','había','habíamos','habían','habiendo','habla','hablaba','hablabamos','hablaban','hablamos','hablan',
'hablar','hablarán','hablaremos','hablaron','hable','hablé','hablen','hablo','habló','hago','hace',
'hacen','hacemos','hacer','haces','hacia','hacía','hacían','hacíamos','haciendo','haga','hagamos','hará','harán','haré',
'haremos','haría','haríamos','hecho','hice','hicimos','hicieron','hizo','hiciese','hiciesen','hincapié','honorable',
'hora','horas','hoy',

'i','ii','iii','iba','ibamos','iban','ido','importante','importancia','importantísimo','imprenscindible','in',
'inaceptable','inaceptables','inclusive','incluso','increíble','increíbles','indudablemente',
'inicio','inició','incisos','inicia','inician','iniciar','inmediata','inmediatamente','inmediatas','inmediato',
'inmensa','inmensas','inmenso','inmensos','innecesaria','innecesarias','innecesario','innecesarios','innumerables',
'insuficiente','insuficientes','intención','intencional','intencionalmente','intensa','intensas','intenso','intensos',
'ir','irregular','irresponsable','irresponsables',

'j','jose','josé','juan','justa','justo',

'ley','leyes','libremente','llega','llegaba','llegaban','llegábamos','llegamos','llegar','llegará','llegarán','llegaré','llegaremos',
'llegaron','llego','llegó','llegue','llegué','llevar','lleva','llevaba','llevaban','llevamos',
'llevan','llevará','llevarán','llevaré','llevaremos','lleve','llevé','llevo','llevó','luego','lugar','lugares','luis',

'maría','mario','más','manera','mediante','mejor','mejora','mejore','mejoré','menos','mera','mero','mes','mesa','mal','mientras',
'mil','miles','millón','millones','minuto','minutos','misma','mismas','mismo','mismos','momento','montón','montones','mucha','muchas',
'muchísima','muchísimas','muchísimo','muchísimos','mucho','muchos',

'n','nación','nacional','nadie','necesario','necesaria','necesarios','necesarias',
'necesita','necesitan','necesitamos','necesitabamos','ningún','ninguno','ninguna',
'ningunos','ningunas','no','norma','normal','normativa','notable','notables','nueva','nuevas','nueve','nuevo','nuevos',
'nunca',

'obviar','obviedad','obvio','ocho','ojalá','orden','oportunidad',

'pablo','página','páginas','pag','pág','país','países','palabra','parecer','parece','parecen',
'parecía','parecían','parecería','párrafo','párrafos','particular',
'pasa','pasamos','pasar','pasarán','pasaron','pase','pasé','paso','pasó','pe','pedir','plantea','peor',
'pero','pésima','pésimas','pésimo','pésimos','pidieran','pidiesen','pidieron','pidió','pido',
'planteaba','planteaban','plantean','plantear','plantearon','planteamos','planteo','planteó',
'plazo','plena','pleno','poca','pocas','poco','pocos','poder','pone','poné','poner','ponía','ponían',
'poníamos','poquita','poquitas','poquito','poquitos','pos','preferencia','preferentemente',
'prefiera','prefieran','prefiere','prefieren','prefiero','pregunta',
'preguntamos','preguntar','pregunte','pregunté',
'pregunto','preguntó','presente','presenté','presentar','presento','presentó',
'presentaron','presentamos','presidenta','presidente','primer','primero','primera',
'primeras','primeros','principal','principales','propongo','propone','proponen','proponemos','propuesta',
'propuestas','propuesto','propuestos','proyecto','proyectos','podemos','podrán','podría',
'podríamos','podrían','pro','probable','probablemente','pronto','pude','pudimos','pudo','pueda','puedan',
'puede','pueden','puedo','pues','puse','pusimos','pusieron','puso'

'queda','quedaba','quedamos','quedan','quedar','quedaron','quede','quedé','quedo','quedó','querer',
'quería','queríamos','querían','querría','querríamos','quién','quiénes','quiera','quieran','quiere',
'quieren','quiero','quise','quisiera','quisieran','quisiéramos','quisiese','quisiesen','quisimos','quiso'

'realmente','recién','respecto','responsable','responsables','responsabilidad','revés',

's','sabe','saber','sabemos','saben','sabían','sabía','sabíamos','san','santa','santo','satisfacción', 'satisfacciones',
'seguimos','según','segundo','segundos','segunda','segundas','segura','seguras','seguro','seis','senor','senora',
'ser','seremos','seré','sería','señor','señora','señoras','señores','señorita',
'señoritas','sesión','sesiona','sesionar','sesione','si','sido','siempre','siendo',
'sigo','sigue','siguen','siguiente','simplemente','sin','sino','siquiera','sola','sóla','solas','solo','sólo',
'solos','son','soy','sr','sra','supone','suponemos','supongo','supongamos','supuesto','supusieron','supuso',

'tal','tampoco','tan','tanta','tantas','tanto','tantos','tema','temas','tenemos','tenga',
'tengo','tener','tenía','tenían','tercer','tercera','tercero','terminar','termino','terminó','término','termine',
'terminé','terminen','terrible','terribles','tiempo','tiene','tienen','tipo','tipos','toda','todas',
'todavía','todes','todo','todos','toma',
'tome','tomé','tomo','tomó','trascendente','trascendentes','tratar','trate','traté','trato','trató','tratamos','tratan',
'trataron','través','trece','treinta','tremenda','tremendas','tremendo','tremendos','tres','trescientos',

'u','última','últimas','último','últimos','un','una','unas','uno','unos','usa','usar','uso','usó','usted',
'ustedes','utilice','utilicé','utiliza','utilizan','utilizar','utilizaron','utlilizo',
'utlilizó',

'va','vamos','van','varias','varios','ve','vea','vean','veces','vemos','ven','venga','vengan','vengo','venimos','venir','veo',
'ver','verán','veré','veremos','vez','viene','vienen','vi','viera','vieran','vieron','vimos','vine','voy','volvemos','volver',
'volverá','volverán','volveré','volveremos','volví','volvimos','volvieron','volvía','volvían','vuelva','vuelvan','vuelve','vuelvo',

'xx','xxi','yendo']

# Las anexamos spanish_stopwords 
spanish_stopwords.extend(new_stopwords)

# Armamos un diccionario para mandar las palabras a nada
stopwords_dic = {word:'' for word in spanish_stopwords}

# Reemplazamos stems que se identifican como distintos 
# (ver funcion reemplazos_stem(cadena, rep_stem))
rep_stem = {'abarqu':'abarc','abismal':'abism','abogac':'abog',
'abolicion':'abol','aborigen':'aborig', 'abra':'abri',
'abram':'abri','abran':'abri','abre':'abri','abren':'abri','abriend':'abri','abrier':'abri',
'abrieron':'abri', 'abrim':'abri','abrir':'abri','abrirs':'abri','absorcion':'absorb',
'abstencion':'absten', 'abstendr':'absten','abstuv':'absten','abstraccion':'abstract',
'absteng':'absten','absuelt':'absolv','academi':'academ','acarre':'acarr',
'acced':'acces','accesibil':'acces','acerqu':'acerc','aciert':'acert','acentu':'acent',
'actos':'acto','actuacion':'actu','acusatori':'acus','adhesion':'adher','adhier':'adher',
'adquisicion':'adquir','aduaner':'aduan','adviert':'advert','advirt':'advert','agradezc':'agradec',
'agricultur':'agricol','alcanc':'alcanz','alimentari':'aliment','alta':'alt','altas':'alt','altisim':'alt',
'alto':'alt','altur':'alt','ambiental':'ambient','amig':'amist','analisis':'analiz','anunci':'anunc',
'apliqu':'aplic','aprendizaj':'aprend','asciend':'ascend','asesinat':'asesin','atencion':'atend','atiend':'atend',
'atravies':'atraves','ausenci':'ausent','automotriz':'automotor','atac':'ataqu','avanc':'avanz',

'balanz':'balanc','blanque':'blanqu','brevement':'brev','busqu':'busc','busqued':'busc',

'cae':'caer','caid':'caer','cay':'caer','calif':'calific','camb':'cambi','capacit':'capac',
'caracterist':'caracteriz','carenci':'carec','central':'centr','circunstancial':'circunst','clarid':'clar',
'climat':'clim', 'coinc':'coincid','coincident':'coincid','comentari':'coment','comercial':'comerci',
'comercializ':'comerci','comienz':'comenz','competit':'compet','complementari':'complement','conceptual':'concept',
'conclusion':'conclu','conduccion':'conduc','confianz':'confi','confund':'confuns','confusion':'confuns','conozc':'conoc',
'consensu':'consens','consigu':'consegu','consultor':'consult','consumidor':'consum','construccion':'constru',
'continental':'continent','contradec':'contradictori','contradiccion':'contradictori',
'contribut':'contribuyent','convencional':'convencion','conviert':'convert','convirt':'convert','convivent':'conviv',
'convocatori':'convoc','cordobes':'cordob','correccion':'correg','correspondient':'correspond','corrupt':'corrupcion',
'creacion':'cre','crecient':'crec','crecimient':'crec','crimen':'crim','criminal':'crim','culpabl':'culp',
'cultural':'cultur','cumplimient':'cumpl',

'debid':'deber','decision':'decid','defend':'defens','defiend':'defens','definicion':'defin','delict':'delit',
'democrat':'democraci','democraciiz':'democraci','demuestr':'demostr','dependent':'depend','dependient':'depend',
'desaparicion':'desaparec','descalif':'descalific','desigualdad':'desiguald','desped':'desp','destruccion':'destru',
'detencion': 'deten','dictamin': 'dictamen', 'diferenci': 'diferent',
'dificil':'dificult','dificultad':'dificult','difusion': 'difund', 'discusion':'discut','disposicion':'dispon',
'dispong': 'dispon', 'dispus': 'dispon','distincion':'distingu', 'dolor': 'dol',

'efect':'efectu','efectuu':'efectu','eficaz':'eficaci','ejes':'eje','ejecu':'ejecut','elector':'elect','electoral':'elect',
'elig':'eleg','emision':'emit','empec':'empez','empiec':'empez','empiez':'empez','empleador':'emple','emprendedor':'emprend',
'empresari':'empres','empresarial':'empres','encuentr':'encontr','energet':'energ','enfermed':'enferm','enfermedad':'enferm',
'entiend':'entend','entra':'entrar','entrad':'entrar','entram':'entrar','entran':'entrar','entro':'entrar', 'equilibri': 'equilibr',
'equipar':'equip','equivalent':'equival','escolar':'escol','escuel':'escol','espanol':'espan',
'establezc':'establec','estrategi':'estrateg','estructural':'estructur','europe':'europ','excedent':'exced','exces':'exced',
'exclus':'exclu','exclusion':'exclu','exigent':'exig','existent':'exist','expliqu':'explic','expuest':'expon','extension':'extens',

'facultad': 'facult', 'familiar': 'famili', 'favorec': 'favor', 'ferrocarril': 'ferroviari','fijens': 'fij','financii': 'financi',
'financiier':'financier','financ':'financi','finanz':'financi','fortalec':'fortalez', 'fraudulent': 'fraud','fuertement':'fuert',
'funcional':'funcion',

'garantic': 'garantiz','genocidi': 'genoc', 'grandez':'grand','graved':'grav','gravisim':'grav','gremial':'gremi',
'gubernamental':'gobern',

'hered':'herenci','hidrocarburifer': 'hidrocarbur','histori':'histor',

'ideal':'ide','ident':'identific','identif':'identific','iguald':'igual','igualitari':'igual','imperial':'imperi',
'impid':'imped','impus':'impon','incent':'incentiv','inclusion':'inclu','individual':'individu','industrial':'industri',
'industrializ':'industri','infantil':'infanci','inflacionari':'inflacion','inicial':'inici','injustici':'injust',
'inmobiliari':'inmuebl','insercion':'insert','institucional':'institu','institut':'institu','integral':'integr',
'intencional':'intencion','interrupcion':'interrump','intervencion':'interven','intervien':'interven','intervin':'interven',
'introduccion':'introduc','inversion':'invert','inversor':'invert', 'inviert':'invert','invirt':'invert',

'jubilatori': 'jubil','judicializ':'judicial','juec':'juez','jurid':'judicial','jurisdiccional':'jurisdiccion',
'justific': 'justif', 'kirchn':'kirchner',  'latinoamerican':'latinoamer',  'leer':'lectur',  'lei':'lectur','leid':'lectur', 
'luchador':'luch',

'magistratur': 'magistr','manteng': 'manten','mantuv': 'manten', 'mantien':'manten','matern':'madr', 'mediat':'medi',
'medicinal': 'medicin', 'metodolog':'metod','mid':'med', 'mient':'ment', 'mint':'ment','modif':'modific',
'modificic':'modific','modificic':'modific','modificicatori':'modific','modificiqu':'modific', 'muer':'muert', 
'muestr':'mostr', 'muev':'mov', 'muj':'mujer', 'mundial': 'mund', 'municipi':'municipal',

'nacimient':'nac','necesari': 'neces','necesit': 'neces','neuquin':'neuquen', 'nieg':'neg', 'ninez':'nin',
'normat':'norm', 'nucl':'nucle','nulid':'nul','obedient':'obedec','obligatoried':'obligatori','obras':'obra',
'obtien':'obten','obtuv': 'obten', 'omision':'omit', 'opin':'opinion','opositor':'oposicion', 'opus':'opon','origin': 'orig',

'parezc':'parec','parlamentari':'parlament','partidari':'partid','patagon':'patagoni','patrimonial':'patrimoni',
'patronal':'patron', 'pen':'penal','penaliz':'penal','pensamient':'pens','perfeccion':'perfect','perjud':'perjudic',
'permanent':'permanec','permis':'permit','permitanm':'permit','persecu':'persegu','persig':'persegu','personal':'persona',
'pertenecient':'pertenec','pertenezc':'pertenec','pertenent':'pertenec','petroler':'petrole','piens':'pens',
'pierd':'perd','planif':'planific','pobr':'pobrez',
'poder':'pod','policial':'polic','popular':'popul','posibil':'posibl','potencial':'potenci','precedent':'preced',
'precision':'precis','presencial':'presenci','presidencial':'president','prestador':'prest','prestam':'prest',
'presuncion':'presunt','pretension':'pretend','presupuestari':'presupuest','prevencion':'preven','prevent':'preven',
'previsibil':'prevision','previst':'prevision','priorid':'prioriz','prioridad':'prioriz','prioritari':'prioriz',
'problemat':'problem','produccion':'produc', 'product':'produc','producor':'produc','produj':'produc','produzc':'produc',
'profesional':'profesion','profund':'profundiz','prohibicion':'prohib','promes':'promet','promuev':'promov',
'propietari':'propied','propus':'propon','proporcional':'proporcion','proteccion':'proteg','proveng':'proven',
'provenient':'proven','provien':'proven','provincial':'provinci','prudent':'prudenci','pymes':'pyme',

'quiebr':'quebr','ratific': 'ratif', 'realidad':'realid', 'realic': 'realiz', 'recl':'reclam', 'reconozc': 'reconoc',
'redaccion':'redact','reduccion':'reduc','refier':'refer','refir':'refer','regimen':'regim','regional': 'region', 'reglamentari':'reglament',
'regulatori':'regul','reivind':'reivindic',  'repit':'repet','requier':'requer', 'respetu': 'respet',  'restrict': 'restring',
'restriccion': 'restring', 'retroces':'retroced', 'revision':'revis', 'rig':'reg', 'rigur': 'rigor','rios':'rio',

 'salarial':'salari', 'salg':'sal', 'saqu':'saque', 'satisfac':'satisfaccion', 'sensibil':'sensibl', 'sep':'sab',  
 'signif':'signific','significic':'signific', 'simil':'similar',  'sindicat':'sindical', 'sintesis':'sintetiz', 'socied':'sociedad', 
 'solicitud':'solicit', 'solidar':'solidari', 'sorprend':'sorpres','sosteng':'sosten','sostien':'sosten','sostuv':'sosten',
 'sufrimient':'sufr', 'sugerent':'suger','sugier':'suger','sup':'sab', 'suscript': 'suscrib', 'suspension':'suspend',

'tarifari':'tarif','tarifaz':'tarif','tasacion':'tas','temari':'tem','temat':'tem','tendenci':'tend','tendient':'tend',
'teoric':'teor','territorial':'territori','testimoni':'testig','titular':'titul','tradicional':'tradicion','tragic':'tragedi',
'traid':'traicion','transcurs':'transcurr','transferent':'transfer','tratamient':'trat','tributari':'tribut','tristez':'trist',
'turist':'turism',

 'unif':'unific','urgent':'urgenci','utiliz': 'util','vac':'vacun','vent':'vend','verdader':'verd','vergonz':'verguenz',
 'via': 'vial','vias': 'vial','vigenci':'vigent','violacion':'viol','violent':'violenci','virtuos':'virtud','votacion':'vot'

}


# Usamo el extractor de raices de palabras de nltk
stemmer = nltk.stem.SnowballStemmer('spanish')

# Filtramos caracteres especiales (ojo con la basura de encodings)
non_words = list(punctuation)
non_words.extend(['¿', '¡','nº','n°','º','°','/n','"','-','…','”','“',
	              '\x94','\x93','–','–','\x91','\x92','\x85','‑','ª'])
# Agrego numeros (digitos)
non_words.extend(map(str,range(10)))


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
                  #Mn = mark, nonspacing

def preprocess(text):
    """ Preprocesa el texto de una string separandolo en una lista de palabras relevantes
	(filtradas) reducidas a su raiz """

    # remove uppercase
    text = text.lower()
    # remove non_words
    text = ''.join([c for c in text if c not in non_words])
    # remove repeated characters
    text = re.sub(r'(.)\1+', r'\1\1', text)

    # remove accents: [à,á,ä,ã] -> a
    #text = strip_accents(text)
    # also remove accents in stopwords
    #stopwords = [strip_accents(w) for w in spanish_stopwords]
    #stopwords = spanish_stopwords

    # El stemmer necesita las tildes para funcionar bien!
    #stem_words = [reemplazos_stem(strip_accents(stemmer.stem(w)), rep_stem) 
    #              for w in text.split() if w not in stopwords]
    pre_stem_words = [stopwords_dic.get(word, word) for word in text.split()]

    stem_words = [strip_accents(stemmer.stem(w)) for w in pre_stem_words if w!='']

    post_stem_words = [rep_stem.get(word, word) for word in stem_words]              

    # return stem words with removed stopwords
    return post_stem_words

def reemplazos_stem(cadena, rep_stem):
    """ Elimina caracteres que dificultan la separacion de discursos con el split
	    input: string
	    output: string """
    # Robado de Stack-Exchange

    # rep_stem: define desired replacements here

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep_stem.items())
    # Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))

    cadena = pattern.sub(lambda m: rep[re.escape(m.group(0))], cadena)

    return cadena

# Tambien armamos una funcion para reemplazar caracteres que dificultan 
#  la separacion entre diputado y discurso.

def reemplazos(cadena):
    """ Elimina caracteres que dificultan la separacion de discursos con el split
	    input: string
	    output: string """
    # Robado de Stack-Exchange
    
    # Hacemos dos reemplazos concatenados para unificar
    rep = {'\x96': '–', '.–':'. –', '.-':'. –', '.Sr.':'.\nSr.', '.Sra.':'. \nSra.',
           '.)Sr.':'.)\nSr.', '.)Sra.':'.)\nSra.', ':Sr.':':\nSr.', ':Sra.':':\nSra.',
           '\x94':' ', '\x93':' ', '\x85':' '} # define desired replacements here
    rep2 = {'D. –':'D.', 'E. –':'E.', 'M. –':'M.', 'S. –':'S.', 'V. –':'V.',
            '°. –':'°.', 'º. –':'°.', 'Artículo. –':'Artículo'}

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.items())
    rep2 = dict((re.escape(k), v) for k, v in rep2.items())
    # Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))
    pattern2 = re.compile("|".join(rep2.keys()))

    cadena = pattern.sub(lambda m: rep[re.escape(m.group(0))], cadena)
    cadena = pattern2.sub(lambda m: rep2[re.escape(m.group(0))], cadena)

    return cadena

def clean_dip(cadena):
    """ Es como reemplazos(), pero limpia los nombres de diputados """

    # Hacemos dos reemplazos concatenados para unificar
    rep = {'**':'', '0':'', '1':'', '2':'', '3':'', '4':'', '5':'', '6':'',
           '7':'', '8':'', '9':''} # define desired replacements here

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.items())
    # Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))

    cadena = pattern.sub(lambda m: rep[re.escape(m.group(0))], cadena)

    return cadena