import random
print("Willkomen in der Süßigkeitfabrik")
print(" ")
input("Debe presionar enter para pasar a la siguiente oración")
print(" ")
print("Dieses Spiel besteht darin, so viele Süßigkeiten zu sammeln, wie Sie möchten. Dafür müssen Sie die vorgeschlagenen Übungen richtig beantworten.")
objetivo=int(input("Ingrese el numero de caramelos que desea obtener: "))
for i in range(1,10000):
    if objetivo==3:
        objetivo= int(input("Por favor ingrese un número mayor a 3: "))
    if objetivo<3:
        objetivo=int(input("El número de caramelos ingresado es menor a 3. Por favor ingrese un número mayor a 3: "))
    if objetivo > 3:
        break
print("El número de caramelos ingresados es: ",objetivo)
input(" ")
caramelos=3
teoria=input("¿Desea realizar un repaso de los verbos en Perfekt? Antworten mit Ja oder Nein.:  ")
for i in range(10000):
    if teoria== " ":
        teoria=input("Debe elegir una opción. ¿Desea realizar un repaso de teoría? Antworten mit Ja oder Nein.: ")
if teoria.lower()=="ja":
    verbos = [
    "machen", "gehen", "kommen", "sehen", "essen", "trinken", "nehmen", "geben", "lesen", "schreiben",
    "fahren", "laufen", "bleiben", "singen", "tanzen", "springen", "fliegen", "schwimmen", "helfen", "kaufen",
    "verkaufen", "spielen", "arbeiten", "schlafen", "wachen", "lernen", "lehren", "warten", "fragen", "antworten",
    "raten", "verstehen", "vergleichen", "verlieren", "finden", "suchen", "treffen", "anrufen", "denken", "glauben",
    "hoffen", "lieben", "hassen", "brauchen", "wünschen", "tragen", "ziehen", "drücken", "öffnen", "schließen",
    "beginnen", "enden", "verlassen", "kennen", "erkennen", "verbinden", "trennen", "setzen", "stellen", "legen",
    "heben", "senken", "steigen", "fallen", "laufen", "springen", "kriechen", "rennen", "fahren", "reiten",
    "schleichen", "klettern", "ziehen", "drücken", "schieben", "treten", "schlagen", "werfen", "fangen", "halten",
    "lassen", "gehen", "kommen", "bleiben", "laufen", "fahren", "fliegen", "schwimmen", "sitzen", "stehen", "liegen",
    "schlafen", "wachen", "träumen", "schreien", "weinen", "lachen", "lächeln", "sprechen", "reden"
]
    perfekt=  [
    ("gemacht", "haben"), ("gegangen", "sein"), ("gekommen", "sein"), ("gesehen", "haben"), ("gegessen", "haben"),
    ("getrunken", "haben"), ("genommen", "haben"), ("gegeben", "haben"), ("gelesen", "haben"), ("geschrieben", "haben"),
    ("gefahren", "sein"), ("gelaufen", "sein"), ("geblieben", "sein"), ("gesungen", "haben"), ("getanzt", "haben"),
    ("gesprungen", "sein"), ("geflogen", "sein"), ("geschwommen", "sein"), ("geholfen", "haben"), ("gekauft", "haben"),
    ("verkauft", "haben"), ("gespielt", "haben"), ("gearbeitet", "haben"), ("geschlafen", "haben"), ("gewacht", "sein"),
    ("gelernt", "haben"), ("gelehrt", "haben"), ("gewartet", "haben"), ("gefragt", "haben"), ("geantwortet", "haben"),
    ("geraten", "sein"), ("verstanden", "haben"), ("verglichen", "haben"), ("verloren", "haben"), ("gefunden", "haben"),
    ("gesucht", "haben"), ("getroffen", "sein"), ("angerufen", "haben"), ("gedacht", "haben"), ("geglaubt", "haben"),
    ("gehofft", "haben"), ("geliebt", "haben"), ("gehasst", "haben"), ("gebraucht", "haben"), ("gewünscht", "haben"),
    ("getragen", "haben"), ("gezogen", "haben"), ("gedrückt", "haben"), ("geöffnet", "haben"), ("geschlossen", "haben"),
    ("begonnen", "haben"), ("geendet", "haben"), ("verlassen", "haben"), ("gekannt", "haben"), ("erkannt", "haben"),
    ("verbunden", "haben"), ("getrennt", "haben"), ("gesetzt", "haben"), ("gestellt", "haben"), ("gelegt", "haben"),
    ("gehoben", "haben"), ("gesenkt", "haben"), ("gestiegen", "sein"), ("gefallen", "sein"), ("gelaufen", "sein"),
    ("gesprungen", "sein"), ("gekrochen", "sein"), ("gerannt", "sein"), ("geritten", "sein"), ("geschlichen", "sein"),
    ("geklettert", "sein"), ("gezogen", "haben"), ("gedrückt", "haben"), ("geschoben", "haben"), ("getreten", "haben"),
    ("geschlagen", "haben"), ("geworfen", "haben"), ("gefangen", "haben"), ("gehalten", "haben"), ("gelassen", "haben"),
    ("gegangen", "sein"), ("gekommen", "sein"), ("geblieben", "sein"), ("gelaufen", "sein"), ("gefahren", "sein"),
    ("geflogen", "sein"), ("geschwommen", "sein"), ("gesessen", "haben"), ("gestanden", "haben"), ("gelegen", "haben"),
    ("geschlafen", "haben"), ("gewacht", "sein"), ("geträumt", "haben"), ("geschrien", "haben"), ("geweint", "haben"),
    ("gelacht", "haben"), ("gelächelt", "haben"), ("gesprochen", "haben"), ("geredet", "haben")
]
    español = [
    "hacer", "ir", "venir", "ver", "comer", "beber", "tomar", "dar", "leer", "escribir",
    "conducir", "correr", "quedarse", "cantar", "bailar", "saltar", "volar", "nadar", "ayudar",
    "comprar", "vender", "jugar", "trabajar", "dormir", "despertar", "aprender", "enseñar", "esperar",
    "preguntar", "responder", "adivinar", "entender", "comparar", "perder", "encontrar", "buscar",
    "encontrar(se) con", "llamar", "pensar", "creer", "esperar (tener esperanzas)", "amar", "odiar",
    "necesitar", "desear", "llevar (ropa)", "tirar", "empujar", "abrir", "cerrar", "comenzar",
    "terminar", "abandonar", "conocer", "reconocer", "conectar", "separar", "poner (sentarse)",
    "colocar (poner de pie)", "poner (acostar)", "levantar", "bajar", "subir", "caer", "correr (mismo verbo, diferente significado)",
    "saltar (mismo verbo, diferente significado)", "gatear", "correr (rápidamente)", "montar (a caballo)", "acechar", "escalar",
    "tirar (mismo verbo, diferente significado)", "presionar (mismo verbo, diferente significado)", "empujar (deslizar)", "pisar", "golpear",
    "lanzar", "atrapar", "sostener", "dejar", "ir (mismo verbo, diferente significado)", "venir (mismo verbo, diferente significado)",
    "quedarse (mismo verbo, diferente significado)", "correr (mismo verbo, diferente significado)", "conducir (mismo verbo, diferente significado)",
    "volar (mismo verbo, diferente significado)", "nadar (mismo verbo, diferente significado)", "sentarse", "estar de pie", "estar acostado",
    "dormir (mismo verbo, diferente significado)", "vigilar", "soñar", "gritar", "llorar", "reír", "sonreír", "hablar", "conversar"
]
    print("A continuación se le listarán los 100 verbos más utilizados junto con su significado en español y su forma en perfekt. Si desea que no se le muestren más, pulse cualquier caracter.")
    print("Verben","           ","Haben/Sein", "            ", "Perfekt", "        ", "Significado")
    for i in range(len(verbos)):
        a=perfekt[i]
        print(verbos[i], "            ",a[0], "               ",a[1], "            ", español[i])
        b=input("")
        if len(b)>0:
            break
input(" ")
oraciones= [
    "Ich trinke gerne Kaffee am Morgen.",
    "Mein Bruder spielt oft Fußball im Park.",
    "Sie arbeitet als Lehrerin an einer Schule.",
    "Wir lernen Deutsch an der Universität.",
    "Du gehst jeden Tag zur Arbeit mit dem Bus.",
    "Mein Vater liest gerne Zeitung am Abend.",
    "Sie kauft Obst und Gemüse im Supermarkt.",
    "Mein Hund schläft viel auf dem Sofa.",
    "Ich helfe meiner Mutter in der Küche.",
    "Wir machen einen Spaziergang im Park.",
    "Du telefonierst mit deinem Freund am Abend.",
    "Meine Schwester tanzt gern zu Musik.",
    "Er besucht oft seine Großeltern am Wochenende.",
    "Sie trägt immer eine Brille zum Lesen.",
    "Wir essen gemeinsam zu Mittag in der Kantine.",
    "Ich spiele Klavier in meiner Freizeit.",
    "Du fährst mit dem Fahrrad zur Schule.",
    "Mein Onkel arbeitet als Ingenieur in einer Firma.",
    "Sie geht ins Fitnessstudio zweimal pro Woche.",
    "Er schreibt Briefe an seine Freunde.",
    "Wir treffen uns am Wochenende zum Kaffee.",
    "Du machst deine Hausaufgaben nach der Schule.",
    "Meine Eltern reisen gerne in den Urlaub.",
    "Sie sprechen Deutsch und Englisch.",
    "Ich lese ein Buch im Bett vor dem Schlafengehen.",
    "Wir sehen uns oft Filme im Kino an.",
    "Du spielst Fußball im Park mit deinen Freunden.",
    "Meine Tante arbeitet als Ärztin im Krankenhaus.",
    "Sie singt gern Lieder beim Kochen.",
    "Er tanzt mit seiner Schwester auf Familienfesten.",
    "Wir nehmen den Zug, um in die Stadt zu fahren.",
    "Ich trinke Tee, wenn ich erkältet bin.",
    "Du kaufst ein Geschenk für deine Mutter.",
    "Meine Cousine lernt Klavier spielen.",
    "Sie spielt Basketball in der Schule.",
    "Wir machen einen Ausflug ins Museum.",
    "Er telefoniert mit seinem Chef am Nachmittag.",
    "Sie geht spazieren im Park mit ihrem Hund.",
    "Ich fahre in den Ferien ans Meer.",
    "Wir essen gerne Pizza am Wochenende.",
    "Du trinkst Wasser zum Abendessen.",
    "Meine Großeltern lesen die Zeitung am Morgen.",
    "Sie kaufen neue Möbel für das Wohnzimmer.",
    "Er spielt Computerspiele in seiner Freizeit.",
    "Wir besuchen unsere Verwandten im Sommer.",
    "Sie machen einen Spaziergang am Fluss.",
    "Ich tanze gern bei Partys mit meinen Freunden.",
    "Du telefonierst mit deiner Schwester jeden Tag.",
    "Mein Bruder fährt mit dem Auto zur Arbeit.",
    "Sie arbeitet hart für ihre Ziele."
]
opciones=[
    ["Ich habe gerne Kaffee am Morgen getrunken.", "Ich trinke gerne Kaffee am Morgen.", "Ich habe gern Kaffee am Morgen getrinken."],
    ["Mein Bruder habe oft Fußball im Park gespielt.", "Mein Bruder spielt oft Fußball im Park.", "Mein Bruder hat oft Fußball im Park gespielt."],
    ["Sie ist als Lehrerin an einer Schule gearbeitet.",  "Sie hat als Lehrerin an einer Schule gearbeitet.","Sie arbeitet als Lehrerin an einer Schule."],
    ["Wir haben Deutsch an der Universität gelernt.", "Wir lernen Deutsch an der Universität.", "Wir hatten Deutsch an der Universität gelernt."],
    ["Du hast jeden Tag zur Arbeit mit dem Bus gegangen.", "Du gehst jeden Tag zur Arbeit mit dem Bus.", "Du bist jeden Tag zur Arbeit mit dem Bus gegangen."],
    ["Mein Vater hat gerne Zeitung am Abend gelesen.", "Mein Vater liest gerne Zeitung am Abend.", "Mein Vater ist gerne Zeitung am Abend gelesen."],
    ["Sie hat Obst und Gemüse im Supermarkt gekaufen.", "Sie kauft Obst und Gemüse im Supermarkt.", "Sie hat Obst und Gemüse im Supermarkt gekauft."],
    ["Mein Hund hat viel auf dem Sofa geschlafen.", "Mein Hund schläft viel auf dem Sofa.", "Mein Hund habt viel auf dem Sofa geschlafen."],
    ["Ich habe meiner Mutter in dem Küche geholfen.", "Ich helfe meiner Mutter in der Küche.", "Ich habe meiner Mutter in der Küche geholfen."],
    ["Wir machen einen Spaziergang im Park.","Wir haben einen Spaziergang im Park gemacht.",  "Wir haben einen Spaziergang im Park gemachet."],
    ["Du hast mit deinem Freund am Abend telefonieren.", "Du telefonierst mit deinem Freund am Abend.", "Du hast mit deinem Freund am Abend telefoniert."],
    ["Meine Schwester hat gern zu Musik getanzen.", "Meine Schwester tanzt gern zu Musik.", "Meine Schwester hat gern zu Musik getanzt."],
    ["Er hat oft seine Großeltern am Wochenende besucht.", "Er besuchte oft seine Großeltern am Wochenende.", "Er habe oft seine Großeltern am Wochenende besucht."],
    [ "Sie trägt immer eine Brille zum Lesen.","Sie hat immer eine Brille zum Lesen getragen.", "Sie haben immer eine Brille zum Lesen getragt."],
    ["Wir haben gemeinsam zu Mittag in der Kantine gegessen.", "Wir essen gemeinsam zu Mittag in der Kantine.", "Wir sind zu Mittag in der Kantine gegessen."],
    ["Ich bin Klavier in meiner Freizeit gespielt.", "Ich spiele Klavier in meiner Freizeit.", "Ich habe Klavier in meiner Freizeit gespielt."],
    ["Du hast mit der Fahrrad zur Schule gefahren.", "Du bist mit dem Fahrrad zur Schule gefahren.", "Du fährst mit dem Fahrrad zur Schule."],
    ["Mein Onkel hat als Ingenieur in einem Firma gearbeitet.", "Mein Onkel hat als Ingenieur in einer Firma gearbeitet.", "Mein Onkel arbeitet als Ingenieur in einer Firma."],
    ["Sie ist ins Fitnessstudio zweimal pro Woche gegangen.", "Sie geht ins Fitnessstudio zweimal pro Woche.", "Sie hat ins Fitnessstudio zweimal pro Woche gegangen."],
    ["Er hat Briefe an seine Freunde geschreiben.", "Er schreibt Briefe an seine Freunde.", "Er hat Briefe an seine Freunde geschrieben."],
    ["Wir haben uns am Wochenende zum Kaffee getroffen.", "Wir treffen uns am Wochenende zum Kaffee.", "Wir haben uns an der Wochenende zum Kaffee getroffen."],
    ["Du hast deine Hausaufgaben nach der Schule gemacht.", "Du machst deine Hausaufgaben nach der Schule.", "Du hast deines Hausaufgaben nach dem Schule gemacht."],
    [ "Meine Eltern reisen gerne in den Urlaub.","Meine Eltern haben gerne in den Urlaub gereist.", "Meine Eltern haben in den Urlaub gereisen."],
    ["Sie haben Deutsch und Englisch gesprochen.", "Sie sprechen Deutsch und Englisch.", "Sie haben Deutsch und Englisch gesprechen."],
    ["Ich hat ein Buch im Bett vor dem Schlafengehen gelesen.", "Ich lese ein Buch im Bett vor dem Schlafengehen.", "Ich habe ein Buch im Bett vor dem Schlafengehen gelesen."],
    ["Wir haben uns oft Filme im Kino angeseht.", "Wir haben uns oft Filme im Kino angesehen.", "Wir sehen uns oft Filme im Kino an."],
    ["Du hast Fußball im Park mit deinen Freunden gespielen.", "Du spielst Fußball im Park mit deinen Freunden.", "Du hast Fußball im Park mit deinen Freunden gespielt."],
    ["Meine Tante hat als Ärztin im Krankenhaus gearbeitet.", "Meine Tante arbeitet als Ärztin im Krankenhaus.", "Meine Tante hat als Ärztin in der Krankenhaus gearbeitet."],
    ["Sie hat Lieder beim Kochen gesungt.", "Sie singt gern Lieder beim Kochen.", "Sie hat Lieder beim Kochen gesungen."],
    ["Er hat mit seinem Schwester auf Familienfesten getanzt.", "Er tanzt mit seiner Schwester auf Familienfesten.", "Er hat mit seiner Schwester auf Familienfesten getanzt."],
    ["Wir nehmen den Zug, um in die Stadt zu fahren.","Wir haben den Zug genommen, um in die Stadt zu fahren.",  "Wir haben dem Zug genommen, um in die Stadt zu fahren."],
    ["Ich habe Tee getrunken, als ich erkältet war.", "Ich trinke Tee, wenn ich erkältet bin.", "Ich habe Tee getrinken, als ich erkältet war."],
    ["Du hast einem Geschenk für deiner Mutter gekauft.", "Du kaufst ein Geschenk für deine Mutter.", "Du hast ein Geschenk für deine Mutter gekauft."],
    ["Meine Cousine hat Klavier spielen gelernet.", "Meine Cousine lernt Klavier spielen.", "Meine Cousine hat Klavier spielen gelernt."],
    ["Sie spielte Basketball in der Schule.", "Sie hat Basketball in der Schule gespielt.", "Sie hat Basketball in das Schule gespielt."],
    ["Wir haben einen Ausflug ins Museum gemacht.", "Wir machen einen Ausflug ins Museum.", "Wir haben einen Ausflug ins Museum gemachen."],
    ["Er hat mit seinem Chef an die Nachmittag telefoniert.", "Er hat mit seinem Chef am Nachmittag telefoniert.", "Er telefoniert mit seinem Chef am Nachmittag."],
    ["Sie ist spazieren im Park mit ihrem Hund gegangen.", "Sie geht spazieren im Park mit ihrem Hund.", "Sie hat spazieren im Park mit ihrem Hund gegangen."],
    ["Ich bin in dem Ferien an der Meer gefahren.", "Ich fahre in den Ferien ans Meer.", "Ich bin in den Ferien ans Meer gefahren."],
    ["Wir haben am Wochenende gerne Pizza gegessen.", "Wir essen gerne Pizza am Wochenende.", "Wir haben am Wochenende gerne Pizza gegesst."],
    ["Du ist Wasser zum Abendessen getrunken.", "Du trinkst Wasser zum Abendessen.", "Du hast Wasser zum Abendessen getrunken."],
    ["Meine Großeltern haben die Zeitung an das Morgen gelesen.", "Meine Großeltern lesen die Zeitung am Morgen.", "Meine Großeltern haben die Zeitung am Morgen gelesen."],
    ["Sie kaufen neue Möbel für das Wohnzimmer.","Sie haben neue Möbel für das Wohnzimmer gekauft.",  "Sie haben neue Möbel für das Wohnzimmer gekaufen."],
    ["Er hat Computerspiele in seiner Freizeit gespielt.", "Er spielt Computerspiele in seiner Freizeit.", "Er hat Computerspiele in seines Freizeit gespielt."],
    ["Wir haben unsere Verwandten im Sommer besacht.", "Wir besuchen unsere Verwandten im Sommer.", "Wir haben unsere Verwandten im Sommer besucht."],
    ["Sie haben einen Spaziergang an das Fluss gemacht.", "Sie machen einen Spaziergang am Fluss.", "Sie haben einen Spaziergang am Fluss gemacht."],
    ["Ich habe gern bei Partys mit meinen Freunden getanzt.", "Ich tanze gern bei Partys mit meinen Freunden.", "Ich bin gern bei Partys mit meinen Freunden getanzt."],
    ["Du hast mit deines Schwester jeden Tag telefoniert.", "Du telefonierst mit deiner Schwester jeden Tag.", "Du hast mit deiner Schwester jeden Tag telefoniert."],
    ["Mein Bruder ist mit dem Auto zur Arbeit gefahren.", "Mein Bruder fährt mit dem Auto zur Arbeit.", "Mein Bruder hast mit dem Auto zur Arbeit gefahren."],
    ["Sie ist hart für ihre Ziele gearbeitet.", "Sie arbeitet hart für ihre Ziele.", "Sie hat hart für ihre Ziele gearbeitet."]
    ]
correctas=["a","c","b","a","c"," a","c","a","c","b","c","c","a","b","a","c","b","b","a","c","a","a","b","a","c","b","c","a","c","c","b","a","c","c","b","a","b","a","c","a", "c","c","b","a","c","c","a","c","a","c"]

print("Im nächsten Spiel sehen Sie einen Satz in der Gegenwart und 3 Optionen für den Satz in der Vergangenheit. Sie müssen mit der richtigen Option antworten ")
print(" ")
print("En el siguiente juego observará una oración en presente y 3 opciones de la oracion en pasado. Deberá responder con la opcion correcta")
print("Que comience el juego :)")
for i in range(1,10000):
    numintentos= int(input("¿Le gustaría tener 1 o 2 intentos por oración?: "))
    if numintentos!=1 and numintentos!=2:
        numintentos=int(input("El número de intentos debe ser 1 o 2: "))
    if numintentos==1 or numintentos==2:
        break
for i in range(1000):
    num=random.randint(0, 49)
    print("Der Satz im Präsens ist: ", oraciones[num])
    input("")
    d=1
    c=opciones[num]
    print("Die Optionen im Perfekt sind: ")
    print("")
    print("a) ",c[0] )
    print("b) ",c[1])
    print("c) ",c[2])
    input(" ")
    respondio=input("Escriba su respuesta de la forma a, b, c (sin paréntesis): ")
    if respondio==correctas[num]:
        print("Richtig")
        input(" ")
        caramelos=caramelos+1
        print("Jetz hast du: ",caramelos, "Süßigkeiten.")
        input(" ")
    if respondio!=correctas[num] and numintentos==1:
        print ("Unrichtig")
        input(" ")
        print("Die richtige Antwort ist: ", correctas[num])
        caramelos=caramelos-1
        if caramelos==1:
            print("Jetz hast du: ",caramelos, "Süßigkeit.")
            input(" ")
        elif caramelos>1:
            print("Jetz hast du: ",caramelos, "Süßigkeiten.")
            input(" ")
    if respondio!=correctas[num] and numintentos==2:
        print("Unrichtig")
        print(" ")
        print("Die Optionen im Perfekt sind: ")
        print("")
        print("a) ",c[0] )
        print("b) ",c[1])
        print("c) ",c[2])
        input(" ")
        respondio=input("Escriba su respuesta de la forma a, b, c (sin paréntesis): ")
        if respondio!=correctas[num]:
            print ("Unrichtig")
            input(" ")
            print("Die richtige Antwort ist: ", correctas[num])
            caramelos=caramelos-1
            if caramelos==1:
                print("Jetz hast du: ",caramelos, "Süßigkeit.")
                input(" ")
            elif caramelos>1:
                print("Jetz hast du: ",caramelos, "Süßigkeiten.")
                input(" ")
        if respondio==correctas[num]:
            print("Richtig")
            input(" ")
            caramelos=caramelos+1
            print("Jetz hast du: ",caramelos, "Süßigkeiten.")
            input(" ")
        
    if caramelos==objetivo:
        print("Herzlichen Glückwunsch. Du hast dein Ziel erreicht. / Felicitaciones. Has logrado tu objetivo.")
        break
    if caramelos==0:
        print("Du hast keine Süßigkeiten mehr. Viel Glück beim nächsten Mal. / Te has quedado sin caramelos. Mejor suerte la próxima.")
        break


