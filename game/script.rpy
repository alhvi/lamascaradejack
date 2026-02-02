# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define j = Character("Jack")
define a = Character("Alhvi")
define o = Character("Oscar")

define titeres=False
define entomologia = False
define pasalido = False
define ichneumonido = False
define alhvi = False
define oscar = False
define edificioi = False
define pasalidoring = False


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg cit

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show jack hello

    # Presenta las líneas del diálogo.

    j "¡Hola! Bienvenido a la UVG"

    j "Dicen que en esta universidad está escondida una máscara mágica"

    show jack love

    j "La leyenda dice que cuando te pones la máscara, puedes aprender todo lo que está en un libro, con sólo tocarlo"

    show jack hello

    j "Esta máscara fue encontrada en una de las expediciones que realizó el profesor Jack Schuster"
    show jack victory

    j "y dicen que solo aparece durante Global Game Jam únicamente cuando hay luna llena"
    show jack hello

    j "Búsca a los alumnos de Jack Schuster y a los organizadores del jam para saber dónde está la máscara"

    j "Te doy la primera pisa, busca el laboratorio de entomología"

    

    label jackback:
        scene bg cit
        show jack hello
       

       
        j "¿Qué te gustaría hacer?"

        menu :

            "Hablar con Oscar":
                if not oscar:
                    jump oscar
                else:
                    jump oscar_conversation

            "Hablar con Alhvi":
                if not alhvi:
                    jump alhvi 
                else:
                    jump alhvi_conversation

            "Ir al edificio I" if edificioi and not pasalidoring:
                jump edificioi
            
            "Encontrar la máscara" if edificioi and pasalidoring:
                jump mascara
    

    label alhvi:

        scene bg secretaria

        if not alhvi:
            show alhvi base
            a "¡Hola! Bienvenido a la UVG"
            a "¿Te puedo ayudar con algo"


        label alhvi_conversation:
            scene bg secretaria
        
            show alhvi base
          
            menu: 

                "¿Es cierto que tu recibiste clases con Jack Schuster"  if not titeres:
                    show alhvi feliz
                    a "Si, era uno de los mejores profesores en UVG"
                    show alhvi aja
                    a "Y además era muy chistoso"
                    show alhvi feliz
                    a "Recuerdo que a veces llevaba unos títeres a la clase. Tenía dos. Uno se llamaba Jorge el Pastelero y otro se llamaba Odo"
                    $ titeres = True
            
                "¿Qué clase deba Schuster?" if titeres:
                    show alhvi feliz
                    a "A mí me dio Biología General, pero daba muchas clases. Él era entomólogo"
                    "¿Qué es entomología?"
                    show alhvi brava
                    a "¿Cómo así que no sabés que es entomología y estudiás en la UVG?"
                    show alhvi base
                    a "Entomología es una especialización de la zoología que estudia a los insectos"
                    $entomologia = True
                    show alhvi feliz
                    a "A Schuster le gustaban mucho los escarabajos, estos son del género pasalidae y  les decimos pasálidos"
                    $ pasalido = True
                    show alhvi aja
                    a "En UVG tenemos varias investigaciones relacionadas a insectos"

                "Regresar con Jack":
                    jump jackback

        jump alhvi_conversation


    label oscar:
        scene bg parqueo
        show oscar base
        o "¡Hola! Bienvenido al global game jam"
        show oscar feliz
        o "¿Te puedo ayudar con algo?"

        label oscar_conversation:
            show oscar base
            menu:
                
                "¿Sabes dónde queda el laboratorio de entomología de la universidad?":
                    show oscar surprised
                    o "¿Qué es entomología?"
                
                    menu:
                        "No lo se":
                            show oscar dissappointed
                            o "Yo tampoco, averigua primero"
                            jump oscar_conversation
                    
                        "Es la ciencia que estudia los insectos" if entomologia:
                            show oscar asustado
                            o "Me dan miedo los insectos"
                            show oscar thinking
                            o "Pero cuando venia vi que había una exposición de insectos en el edificio I"
                            $edificioi = True

                "Regresar con Jack":
                    jump jackback
            

        jump jackback

    label edificioi:
        scene bg mapa
        show jack hello
        j "¿Sabes qué son los pasálidos?"
        menu:
            "Si, son escarabajos" if pasalido and not pasalidoring:
                j "¡Qué bien! Toma este anillo de pasálido"
                show jack victory
                j "Te servirá para encontrar la máscara"
                $pasalidoring = True
            
            "No":
                j "Ah qué lástima"


        jump jackback


    label mascara:

        scene bg mapa
        show jack hello
        j "Acá debería de ir más historia, pero ya no da tiempo"
        show  jack victory
        j "Así que toma la máscara"
        show jack hello
        j "Lo único es que funciona únicamente un día"
        show jack love
        j "Cada 29 de febrero"
        j "Ese dia era el cumpleaños de Jack Schuster"
        show jack hello
        j "Espero que hayas aprendido algo en el juego"
        show jack victory
        j "Y andá a la biblioteca"
        show jack love
        j "Y lee por favor"

        scene bg secretaria
        "Fin"
        $ renpy.quit()






       
                

       








    # Finaliza el juego:

    return
