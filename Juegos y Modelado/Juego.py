import random
print("Willkomen in der Süßigkeitfabrik")
print(" ")
input("Debe presionar enter para pasar a la siguiente oración")
print(" ")
print("Dieses Spiel besteht darin, so viele Süßigkeiten zu sammeln, wie Sie möchten. Dafür müssen Sie die vorgeschlagenen Übungen richtig beantworten.")
objetivo=input("Ingrese el numero de caramelos que desea obtener")
for i in range(1,10000):
    if objetivo==3:
        objetivo= int(input("Por favor ingrese un número mayor a 3: "))
    if objetivo <3:
        objetivo=int(input("El número de caramelos ingresado es menor a 3. Por favor ingrese un número mayor a 3: "))
    if objetivo > 3:
        break
print("El número de caramelos ingresados es: ",objetivo)
input(" ")
caramelos=3
teoria=input("¿Desea realizar un repaso de teoría? Antworten mit Ja oder Nein.:  ")
for i in range(10000):
    if teoria== " ":
        teoria=input("Debe elegir una opción. ¿Desea realizar un repaso de teoría? Antworten mit Ja oder Nein.: ")
if teoria.lower()=="ja":
    print(" ")
    print("Denken Sie daran, dass die Artikel so dekliniert werden: ")
    print(" ")
    print("Recuerde que los articulos se declinan de la siguiente manera: ")
    print(" ")
    articulos=["der","das","die","die (Pl)"]
    dativ=["dem", "dem", "der", "den"]
    akk= ["den","das","die","die"]
    print("Articulo","        ","Dativo","        ","Acusativo")
    input(" ")
    for i in range(len(articulos)):
        print(articulos[i], "              ",dativ[i], "              ", akk[i])
        input(" ")
    print("Die Artikel werden im Dativ dekliniert, wenn es keine Bewegung gibt oder wenn man angeben möchte, wem etwas gehört. Sie werden im Akkusativ dekliniert, wenn es eine Bewegung gibt oder wenn man angeben möchte, von wem etwas kommt.")
    print(" ")
    print("Los articulos se declinan en dativo cuando no hay movimiento o se quiere indicar ¿A quién? y se declinan en acusativo cuando sí hay movimiento o se quiere indicar ¿de quién? es algo")
input("Presione enter para comenzar con el juego")

print(" ")


oraciones = [
    "Ich gebe ... (der) Hund ein... (der) Knochen.", 
    "Der Lehrer hilft ... (der) Schülern.",
    "Sie sieht ...(der) Film in ... (das) Kino.",
    "Die Katze liegt auf ...(das) Sofa.",
    "Er fährt mit ... (der) Bus zu ... (die) Schule.",
    "Wir kaufen eine Pizza für ... (die) Party.",
    "Das Buch ist für mein... (der) Bruder.",
    "Ich gehe in ... (die) Bibliothek.",
    "Die Blumen stehen auf ...(der) Tisch.",
    "Sie trinkt ein... (der) Tee mit Zucker.",
    "Der Mann geht zu ... (der) Arzt.",
    "Sie kommt aus ... (die) Stadt.",
    "Die Kinder spielen in ...(der) Park.",
    "Ich sehe den Vogel in ...(der) Baum.",
    "Er gibt dem Mädchen ein... (der) Apfel.",
    "Wir gehen in ...(das) Kino am Samstag.",
    "Die Frau liest ein Buch in ... (die) Bibliothek.",
    "Ich kaufe ... (der) Kind ein Geschenk.",
    "Sie hat ... (der) Schlüssel in ...(das) Auto.",
    "Der Mann läuft zu... (der) Supermarkt.",
    "Die Schülerin hört ...(die) Lehrerin zu.",
    "Er malt ein Bild für ... (die) Oma.",
    "Wir essen ... (das) Mittagessen zu Hause.",
    "Die Katze liegt unter ... (der) Tisch.",
    "Ich gehe mit mein... (der) Freund ins Restaurant.",
    "Der Hund spielt mit ... (der) Ball im Garten.",
    "Sie hat ein...(der) Hund und ein... (die) Katze.",
    "Die Kinder gehen zu ... (das) Spielplatz.",
    "Der Vater kauft ... (die) Tochter ein Fahrrad.",
    "Wir trinken ein... (der) Kaffee nach ... (das) Essen.",
    "Der Mann wartet auf ... (der) Bus.",
    "Die Frau geht zu ... (der) Arzttermin.",
    "Ich lese das Buch auf ... Sofa.",
    "Die Blumen sind für mein... Mutter.",
    "Sie gibt ... Lehrer das Heft.",
    "Der Junge spielt mit sein... Bruder in ... Park.",
    "Er isst ein... Apfel ohne Schale.",
    "Wir laufen durch ... Park.",
    "Die Eltern kommen aus ... Urlaub.",
    "Das Mädchen geht mit ... Mutter einkaufen.",
    "Er hat ein... Hund und ein... Katze.",
    "Sie bringt ... Kuchen zur Party.",
    "Der Vater hilft ... Sohn bei den Hausaufgaben.",
    "Ich gebe mein... Schwester das Buch.",
    "Die Kinder spielen in ... Garten.",
    "Sie kommt aus ... Haus.",
    "Wir gehen in ... Stadt am Wochenende.",
    "Der Mann fährt mit ... Fahrrad zur Arbeit.",
    "Die Frau liest ein... Zeitung im Park."
];
respuestas=["dem/einen","der","den/dem","dem","dem/der","die", "meinen", "die","dem","einen","der","der","dem","dem","einen", "das","der", "dem","den/dem","dem","der","die","das","dem","meinem","dem","einen/eine","dem","der","einem/dem","den","dem","dem","meine","dem","seinem/dem", "einen", "den","dem","der", "einen/eine","den","dem", "meiner","dem","dem","die","dem","eine"];
Correcion= ["¿Está quieto o se mueve?}","¿A quién ayuda la profesora?","¿Qué ven?¿Donde? (¿se mueve el lugar?)",
            "¿El gato se mueve?","¿Estar en un vehículo con qué declinación va? y ¿zu?","¿La Fiesta se mueve?"," ¿Para quién es el libro?",
            " ¿Me muevo?"," Las flores están quietas o se mueven"," ¿De quién es el Té?", "Zu qué tipo de preposición es",
            "Aus que tipo de preposición es", " ¿Se mueven?","¿Se mueve?","¿De quién es la manzana?", "¿Qué verbo usa?",
            "¿Dónde?¿Se mueve?"," ¿A quién?", " ¿Que tiene?¿Dónde?","¿Qué preposición usa?", "¿A quién escucha?", " ¿Para quién?",
            "¿Se mueven?",  " ¿Se mueve?¿Qué Verbo usa?"," ¿Se mueve?", " ¿Qué tipo de preposición es mit?"," ¿De quiénes son los animales?",
         " ¿Qué tipo de preposición es Zu","¿A quién le compra una bicileta?", " ¿Quién toma?¿Que tipo de preposición es nach?"," ¿Se mueve el hombre?",
         "¿Se mueve la mujer?", "¿Me muevo?","¿Para quién son las flores?","¿A quién?", " ¿Qué preposicion es mit?¿Donde juegan?",
         " ¿De quién es la manzana?", " ¿Se mueven?", " ¿Qué tipo de preposición es aus?", " ¿Se mueve?", 
         "¿De quién es el perro y el gato?", "¿A qué está dando?", "¿A quién ayuda?", "¿A quién le da eso?",
           " ¿Donde?", "¿Qué tipo de preposición es?"," ¿Se mueven?", " ¿Se mueven? ", " ¿Qué está leyendo?¿De quién es?"]


orresp=[]
for i in range(len(respuestas)):
    orresp.append((oraciones[i],respuestas[i],Correcion[i]))

print("In dem folgenden Spiel müssen Sie die Sätze mit dem fehlenden Artikel vervollständigen. Sie starten mit 3 Süßigkeiten und erhalten für jede richtige Antwort eine Süßigkeit. Aber für jede falsche Antwort wird Ihnen eine Süßigkeit weggenommen. Wenn Sie keine Süßigkeiten mehr haben, verlieren Sie. Das Spiel beginnt. Viel Glück.")
print(" ")
print("En el siguiente juego deberá completar las oraciones con el artículo faltante. Comenzará teniendo 3 caramelos y por cada respuesta correcta recibirá un caramelo. Pero por cada respuesta incorrecta se le quitará uno. Si se queda sin caramelos pierde. Que comience el juego. Buena suerte.")
input(" ")
for i in range(1,10000):
    numintentos= int(input("¿Le gustaría tener 1 o 2 intentos por oración?: "))
    if numintentos!=1 and numintentos!=2:
        numintentos=int(input("El número de intentos debe ser 1 o 2: "))
    if numintentos==1 or numintentos==2:
        break
for i in range(1,10000):
    tupla= random.choice(orresp)
    if numintentos==2:
        a=1
    print(tupla[0])
    input(" ")
    if len(tupla[1])>6:
        print("La respuesta debe ser de la forma: aaa/aaa (sin espacios).")
    respondio= input("Geben Sie Ihre Antwort ein / Ingrese su respuesta: ")
    respondio=respondio.lower().strip()
    if respondio==tupla[1]:
        print("Richtig")
        input(" ")
        caramelos=caramelos+1
        print("Jetz hast du: ",caramelos, "Süßigkeiten.")
        input(" ")
    if respondio!=tupla[1] and numintentos==1:
        print ("Unrichtig")
        input(" ")
        print("Die richtige Antwort ist: ", tupla[1])
        caramelos=caramelos-1
        if caramelos==1:
            print("Jetz hast du: ",caramelos, "Süßigkeit.")
            input(" ")
        elif caramelos>1:
            print("Jetz hast du: ",caramelos, "Süßigkeiten.")
            input(" ")
    if respondio != tupla[1] and a==1:
     print ("Unrichtig")
     input(" ")
     print("Hier ist eine Hilfe.: ", tupla[2])
     print(tupla[0])
     input(" ")
     a=2
     if len(tupla[1])>6:
         print("La respuesta debe ser de la forma: aaa/aaa (sin espacios).")
     respondio= input("Geben Sie Ihre Antwort ein: ")
     respondio=respondio.lower().strip()
    if respondio==tupla[1] and a==2:
        print("Richtig")
        input(" ")
        caramelos=caramelos+1
        print("Jetz hast du: ",caramelos, "Süßigkeiten.")
        input(" ")
    if respondio != tupla[1] and a==2:
     print ("Unrichtig")
     input(" ")
     print("Die richtige Antwort ist: ", tupla[1])
     caramelos=caramelos-1
     if caramelos==1:
            print("Jetz hast du: ",caramelos, "Süßigkeit.")
            input(" ")
     elif caramelos>1:
            print("Jetz hast du: ",caramelos, "Süßigkeiten.")
            input(" ")
    if caramelos==objetivo:
        print("Herzlichen Glückwunsch. Du hast dein Ziel erreicht. / Felicitaciones. Has logrado tu objetivo.")
        break
    if caramelos==0:
        print("Du hast keine Süßigkeiten mehr. Viel Glück beim nächsten Mal. / Te has quedado sin caramelos. Mejor suerte la próxima.")
        break



    


