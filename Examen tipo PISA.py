from tkinter import *#Esta es una librería local para cargar imágenes, por lo que no será necesario instalar una externa

def grade(x,y):#Esta función permite calcular el promedio para el total de aciertos obtenidos en cada área.
    z=x/y*100
    return str(round(z,2))

'''La siguiente función contiene la parte de Biología. Al final escribe los resultados en el archivo de texto "ResultadoB"
y regresa un valor que determina la continuidad o finalización del programa'''
def bio():
    area='Biología'
    questions=11
    print('Estás a punto de comenzar la parte de Biología. ¿Estás listo(a)? ')
    ready=input('\n\tEscribe \"1\" para comenzar.\n\tEscribe cualquier otro valor para volver al menú principal.' )
    while ready=='1':
        score=0
        print('1'.center(100,'*'),'\nLee el siguiente fragmento:\n\n"Un hombre ha fallecido hoy en Smithville \
después de recibir múltiples puñaladas. Según fuentes policiales, había señales de lucha y parte de la sangre \
hallada en la escena del crimen no se corresponde con la sangre de la víctima. Sospechan que dicha sangre pertenece \
al asesino. Para ayudar a capturar al culpable, los miembros de la policía científica han elaborado un perfil del \
ADN de la muestra de sangre...\"')
        answer=(input('\nEn este artículo periodístico se menciona una sustancia denominada ADN. ¿Qué es \
el ADN?\n\n\tA.Una sustancia presente en las membranas celulares que impide que se salga el contenido de la \
célula.\n\tB.Una molécula que contiene las instrucciones para la fabricación de nuestros cuerpos.\n\tC.Una \
proteína presente en la sangre que ayuda a transportar oxígeno a los tejidos.\n\tD.Una hormona de la sangre \
que ayuda a regular el contenido de glucosa en las células del cuerpo. '))
        if answer.lower()=='b':
                score+=1
        print('2'.center(100,'*'),'\nLa cirugía con anestesia, realizada en salas de operaciones especialmente \
equipadas, es necesaria para tratar numerosas enfermedades. ')
        answer=str(input('\nPuede suceder, después de una operación, que los pacientes sean incapaces de comer \
y de beber, y entonces se les pone un gota a gota con suero que contiene agua, azúcares y sales minerales. A veces \
también se le añaden antibióticos y tranquilizantes.\n¿Por qué los azúcares que se añaden al gota a gota son \
importantes para el paciente recién operado?\n\n\tA.Para evitar la deshidratación.\n\tB.Para controlar el dolor \
del postoperatorio.\n\tC.Para curar las infecciones del postoperatorio.\n\tD.Para proporcionar la nutrición necesaria. '))
        if answer.lower()=='d':
            score+=1
        print('3'.center(100,'*'),'\nLos trasplantes de órganos requieren cirugía con anestesia y cada vez son \
más frecuentes. En la gráfica siguiente, se representa el número de trasplantes realizados en un hospital durante \
el año 2003.\n\n¿Se puede deducir la conclusión siguiente de la gráfica? Escribe Sí o No\n\n\t\"Si los pulmones \
se trasplantan, también se debe tranplantar el corazón\"\n\n*Cierra la ventana con la gráfica una vez que estés \
listo(a) y escribe Sí o No según tu razonamiento ')
        win=Tk()
        win.geometry("700x300")
        win.config(bg="white")
        img=PhotoImage(file="1-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='no':
            score+=1
        print('4'.center(100,'*'),'\nLee el artículo de periódico de la ventana emergente y contesta a las \
siguientes preguntas: ')
        print('\nEn  la  última  frase  del  artículo  se  dice  que  muchos  gobiernos  ya  han  decidido  \
prohibir  por  ley  la  clonación  de  seres  humanos.  Más  abajo,  se  mencionan  dos  posibles razones para \
que hayan tomado esta decisión.\n\n¿La siguiente razón es científica? Escribe Sí o No\n\n\t"Las personas no \
deberían asumir el papel de un Creador."\n\n*Cierra la ventana con el artículo periodístico una vez que vayas a contestar')
        win=Tk()
        win.geometry("800x400")
        win.config(bg="white")
        img=PhotoImage(file="2-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='no':
            score+=1
        print('5'.center(100,'*'),'\nEn  la  línea  14, se  describe  la  parte  de  la  ubre  que  se  \
usó  como  \"un  trozo  muy  pequeño\". Por el texto del artículo, ¿puedes deducir a qué se refiere con \"un \
trozo muy pequeño\"?\n\n\tA. Una célula.\n\tB. Un gen.\n\tC. El núcleo de una célula.\n\tD. Un cromosoma. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('6'.center(100,'*'),'\nEl espinoso es un pez que es fácil de mantener en un acuario.\
\n\n\t~Durante la época de reproducción el vientre del espinoso macho cambia de color plateado a rojo.\
\n\t~El espinoso macho atacará a cualquier macho rival que invada su territorio y lo intentará ahuyentar.\
\n\t~Si se aproxima una hembra de color plateado, intentará guiarla hasta su nido para que ponga allí \
sus huevos.\n\nEn un experimento, un alumno quiere investigar qué provoca la aparición de un comportamiento \
agresivo en el espinoso macho.\nEn el acuario del alumno sólo hay un espinoso macho. El alumno ha hecho tres \
modelos de cera unidos a trozos de alambre. Cuelga los modelos dentro del acuario, por separado, durante \
el mismo tiempo. Cuando están dentro, el alumno cuenta el número de veces que el espinoso macho ataca la \
figura de cera empujándola de forma agresiva.\nEl resultado del experimento se presenta en la gráfica.\
\n\n¿Qué pregunta intenta responder este experimento?\n\n\tA. ¿Reacciona el espinoso macho de forma más \
agresiva al modelo rojo que al plateado?\n\tB. ¿El espinoso macho reacciona más agresivamente ante la \
falta de alimento?\n\tC. ¿El espinoso macho no se adapta al acuario?\n\tD. Ninguna de las anteriores\
\n\n*Cierra la ventana con la gráfica una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("750x300")
        win.config(bg="white")
        img=PhotoImage(file="3-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('7'.center(100,'*'),'\nDurante el tiempo de reproducción, si el espinoso macho ve una \
hembra, tratará de atraerla con un comportamiento de cortejo parecido a una danza. En un segundo experimento \
se investiga este comportamiento de cortejo.\nDe nuevo, se usan tres modelos de cera atados a un alambre. \
Uno es de color rojo; los otros dos son de color plateado, pero uno tiene el vientre plano y el otro tiene \
el vientre redondeado. Los alumnos cuentan el número de veces (en un determinado periodo de tiempo) que el \
macho reacciona ante cada modelo con un comportamiento de cortejo.\nLos resultados de este experimento se \
presentan en la gráfica.\n\nDe acuerdo con la información de la gráfica, ¿qué conclusión es correcta?\
\n\n\tA. El color rojo provoca el comportamiento de cortejo del espinoso macho.\n\tB. La hembra del \
espinoso con el vientre plano provoca la mayor cantidad de reacciones en el espinoso macho.\n\tC. \
El espinoso macho reacciona con mayor frecuencia ante una hembra con el vientre redondeado que ante \
una hembra con el vientre plano.\n\tD. Todas son correctas\n\n*Cierra la ventana con la gráfica una \
vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("775x400")
        win.config(bg="white")
        img=PhotoImage(file="4-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('8'.center(100,'*'),'\nLee el texto contenido en la ventana. Después lee los siguientes \
datos:\n\t~Se plantó maíz en 200 campos de todo el país.\n\t~Cada campo se dividió en dos. En una mitad se \
cultivó el maíz genéticamente modificado (OGM), tratado con el poderoso herbicida nuevo, y en la otra mitad \
se cultivó el maíz tradicional tratado con un herbicida convencional.\n\t~Se encontró aproximadamente el \
mismo número de insectos en el maíz OGM, tratado con el nuevo herbicida, que en el maíz tradicional, tratado \
con el herbicida convencional.\n\nEl maíz se plantó en 200 campos de todo el país. ¿Por qué los científicos \
realizaron el estudio en varios lugares?\n\n\tA. Con el fin de que muchos agricultores probaran el nuevo \
maíz OGM.\n\tB. Para observar cuánta cantidad de maíz OGM serían capaces de cultivar.\n\tC. Para cubrir \
la mayor cantidad posible de terrenos con el maíz OGM.\n\tD. Para incluir varias condiciones del cultivo \
del maíz.\n\n*Cierra la ventana con el texto una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("725x300")
        win.config(bg="white")
        img=PhotoImage(file="5-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='d':
            score+=1
        print('9'.center(100,'*'),'\nLee el resumen de un artículo del periódico Daily Mail del 30 de \
marzo de 1998 contenido en la ventana.')
        print('\nLos expertos en nutrición afirman que Jessica «... no obtiene las vitaminas suficientes». \
Una de esas vitaminas que no contiene el chocolate es la vitamina C. Quizás podría compensar esta carencia \
de vitamina C incluyendo algún alimento que contenga un alto porcentaje de vitamina C en «la comida normal \
que hace cada cinco días».\n\nAquí tienes una lista de tipos de alimentos:\n\n\t1. Pescado.\n\t2. Fruta.\
\n\t3. Arroz.\n\t4.Vegetales.\n\n¿Qué dos tipos de alimentos, de los que aparecen en esta lista, recomendarías \
a Jessica para que pudiera compensar la carencia de vitamina C?\n\n\tA. 1 y 2.\n\tB. 1 y 3.\n\tC. 1 y 4.\
\n\tD. 2 y 3.\n\tE. 2 y 4.\n\tF. 3 y 4.\n\n*Cierra la ventana con la información una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("725x300")
        win.config(bg="white")
        img=PhotoImage(file="6-Biología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='e':
            score+=1
        print('10'.center(100,'*'),'\nEl ejercicio físico practicado con regularidad, pero con moderación, \
es bueno para la salud.\n\n¿Cuál de los soguientes NO es un beneficio del ejercicio físico practicado con \
regularidad?\n\n\tA. El ejercicio físico ayuda a prevenir las enfermedades del corazón y los problemas \
circulatorios.\n\tB. El ejercicio físico hace que tengas una dieta saludable.\n\tC. El ejercicio físico \
ayuda a prevenir la obesidad. ')
        answer=input()
        if answer.lower()=='b':
            score+=1
        print('11'.center(100,'*'),'\n¿Qué sucede cuando se ejercitan los músculos? Escribe Verdadero o Falso \
para cada afirmación.\n')
        answer=input('\t~Los músculos reciben un mayor flujo de sangre. ')
        answer2=input('\t~Se forma grasa en los músculos. ')
        if answer.lower()=='verdadero' and answer2.lower()=='falso':
            score+=1
        print(f'\n\U0001F64C ¡Felicidades! Has terminado la parte de Biología. Tu promedio es de {grade(score,questions)}.')
        print('\U0001F440 Considera repasar en los temas que se te dificultaron. Puedes mostrar el archivo \
\"ResultadoB\" a tu profesor(a). ')
        resultado=open('ResultadoB.txt','w')
        resultado.write('Nombre del alumno(a): ')
        resultado.write(name)
        resultado.write('\nÁrea respondida: ')
        resultado.write(area)
        resultado.write('\nPromedio: ')
        resultado.write(grade(score,questions))
        resultado.close()
        ready=input('\n¿Quieres volver a contestar la parte de Biología?\n\nEscribe \"1\" para volver a contestarla.\
\nEscribe cualquier otro valor para volver al menú principal. ') 
    if ready!='1':
        firstanswer='10'
        return firstanswer
    
'''La siguiente función contiene la parte de Física y Química. Al final escribe los resultados en el archivo de texto "ResultadoFQ"
y regresa un valor que determina la continuidad o finalización del programa'''  
def fis_quim():
    area='Física-Química'
    questions=10
    print('Estás a punto de comenzar la parte de Física-Química. ¿Estás listo(a)? ')
    ready=input('\n\tEscribe \"1\" para comenzar.\n\tEscribe cualquier otro valor para volver al menú principal.' )
    while ready=='1':
        #Parte de Física
        score=0
        print('1'.center(100,'~'),'\nUn autobús circula por un tramo recto de carretera. Raimundo, el conductor \
del autobús, tiene un vaso de agua sobre el panel de mandos. De repente, Raimundo tiene que frenar violentamente. ')
        print('\n¿Qué es más probable que le ocurra al agua del vaso inmediatamente después de que Raimundo frene \
violentamente?\n\tA. El agua permanecerá horizontal.\n\tB. El agua se derramará hacia atrás (lado 1).\n\tC. El agua se \
derramará hacia adelante (lado 2).\n\tD. El agua se derramará, pero no sabes si lo hará hacia atrás o hacia adelante\
\n\n*Cierra la ventana con la imagen una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("225x300")
        win.config(bg="white")
        img=PhotoImage(file="1-Física.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('2'.center(100,'~'),'\nEl autobús  de Raimundo, como la  mayoría de los autobuses, funciona con \
un motor diesel. Estos autobuses contribuyen a la contaminación del medio ambiente.\nUn compañero de Raimundo trabaja \
en una ciudad donde se usan trolebuses que funcionan  con  un  motor  eléctrico.  El  voltaje  necesario  para  este  \
tipo  de  motores  eléctricos es suministrado por cables eléctricos (como en los trenes eléctricos). La electricidad \
procede de una central que utiliza carbón.\n\nLos  partidarios  del  uso  de  trolebuses  en  la  ciudad  argumentan  \
que  este  tipo  de  transporte no contribuye a la contaminación del aire. ¿Tienen razón los partidarios del trolebús?\
\n\n\tA. No, porque la central eléctrica, también contamina el aire.\n\tB. Sí,  pero  esto  es  cierto  sólo  para  los  \
trolebuses;  ya  que,  sin  embargo,  la  combustión del carbón contamina el aire.\n\tC. Ambas son correctas. ')
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('3'.center(100,'~'),'\nPedro está haciendo reparaciones en una casa vieja. Ha dejado una botella de \
agua, algunos clavos metálicos y un trozo de madera dentro del maletero de su coche. Después de que el coche ha estado \
tres horas al sol, la temperatura dentro del coche llega a unos 40°C.\n\n¿Qué les pasa a los objetos dentro del coche? \
Escribe una V si es verdadero o una F si es falso para cada afirmación.')
        answer1=input('\n\t~Todos tienen la misma temperatura. ')
        answer2=input('\t~Después de un rato el agua empieza a hervir.')
        answer3=input('\t~Después de un rato los clavos están rojos incandescentes. ')
        answer4=input('\t~La temperatura de los clavos es mayor que la temperatura del agua. ')
        if answer1.lower()=='v' and answer2.lower()=='f' and answer3.lower()=='f' and answer4.lower()=='f':
            score+=1
        print('4'.center(100,'~'),'\nPara beber durante el día, Pedro tiene una taza con café caliente, a unos 90°C de \
temperatura, y una taza con agua mineral fría, a unos 5 °C de temperatura. Las tazas son del mismo material y tamaño, y \
el volumen contenido en cada taza es el mismo. Pedro deja las tazas en una habitación donde la temperatura es de unos 20°C.\
\n¿Cuáles serán probablemente las temperaturas del café y del agua mineral después de 10 minutos?\n\n\tA. 70°C y 10°C.\
\n\tB. 90°C y 5°C.\n\tC. 70°C y 25°C.\n\tD. 20°C y 20°C. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('5'.center(100,'~'),'\nEn muchos países se pueden tomar imágenes del feto (bebé en desarrollo en el \
vientre de su madre) utilizando imágenes tomadas por ultrasonidos (ecografía). Los ultrasonidos se consideran seguros \
tanto para la madre como para el feto.\nLa médico utiliza una sonda y la desplaza sobre el abdomen de la madre. Las \
ondas de ultrasonido penetran en el abdomen de la madre y se reflejan en la superficie de feto. Estas ondas reflejadas \
son captadas de nuevo por la sonda y transmitidas a una máquina que produce la imagen.\n\n*Cierra la ventana con la \
imagen para continuar ')
        win=Tk()
        win.geometry("600x275")
        win.config(bg="white")
        img=PhotoImage(file="2-Física.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        print('\nPara formar la imagen, la máquina de ultrasonidos necesita calcular la distancia entre el feto \
y la sonda. Las ondas de ultrasonido se mueven a través del abdomen a una velocidad de 1.540 m/s. ¿Qué tiene que medir \
la máquina para poder calcular la distancia?\n\n\tA. La aceleración de la onda.\n\tB. El tiempo que viaja la onda.\
\n\tC. La distancia. ')
        answer=input()
        if answer.lower()=='b':
            score+=1
        print('6'.center(100,'~'),'\nTambién se puede obtener una imagen del feto utilizando rayos X. Sin embargo, \
a las mujeres se les aconseja evitar los rayos X en el abdomen durante el embarazo.¿Por qué debe una mujer embarazada \
evitar las exploraciones con rayos X?\n\n\tA. Los rayos X no producen una foto clara del feto.\n\tB. Los rayos X \
representan un gasto extra.\n\tC. Los rayos X son perjudiciales para el feto. ')
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('7'.center(100,'~'),'\n¿Cuál de las siguientes preguntas NO pueden responder las exploraciones con \
ultrasonidos de las madres embarazadas?\n\n\tA. ¿Hay más de un bebé?\n\tB. ¿De qué sexo es el bebé?\n\tC. ¿De qué \
color son los ojos del bebé?\n\tD. ¿Tiene el bebé el tamaño adecuado? ')
        answer=input()
        if answer.lower()=='c':
            score+=1
        #Parte de Química
        print('8'.center(100,'~'),'\nLa tabla siguiente tiene dos recetas de cosméticos que se pueden hacer en casa.\
\nLa barra de labios es más dura que el brillo de labios, que es suave y cremoso.\nAl hacer la barra de labios y el \
brillo de labios, el aceite y las ceras se mezclan entre sí. El colorante y el aroma se añaden después.La barra de \
labios hecha con esta receta es dura y no es fácil utilizarla.\n\n¿Cómo cambiarías la proporción de los ingredientes \
para hacer una barra de labios más blanda?\n\n\tA. Se puede usar menos cera de abejas y cera de palmera.\n\tB. \
Añadiendo más aceite de ricino.\n\tC. Calentando la mezcla más tiempo se ablandará.\n\n*Cierra la ventana con la \
tabla una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("800x325")
        win.config(bg="white")
        img=PhotoImage(file="1-Química.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='a' or answer.lower()=='b':
            score+=1
        print('9'.center(100,'~'),'\nAceites y ceras son sustancias que se mezclan bien entre sí. El agua no \
se mezcla con los aceites, y las ceras no son solubles en agua.\nSi se vuelca mucha agua dentro de la mezcla de \
la barra de labios cuando se está calentando, ¿qué ocurrirá con mayor probabilidad?\n\n\tA. Se producirá una \
mezcla más cremosa y blanda.\n\tB. La mezcla se hará más dura.\n\tC. La mezcla apenas cambiará.\n\tD. Grumos \
grasos de la mezcla flotarán sobre el agua. ')
        answer=input()
        if answer.lower()=='d':
            score+=1
        print('10'.center(100,'~'),'\nCuando se añade un emulsionante, éste hace que se mezclen bien los aceites \
y las ceras con el agua.\n¿Por qué el jabón y el agua limpian una mancha de barra de labios?\n\n\tA. El agua tiene \
un emulsionante que permite que se mezclen el jabón y la barra de labios.\n\tB. El jabón actúa como un emulsionante \
y permite que el agua y la barra de labios se mezclen.\n\tC. Los emulsionantes de la barra de labios permiten que \
el jabón y el agua se mezclen.\n\tD. El jabón y la barra de labios se combinan y forman un emulsionante que se \
mezcla con el agua. ')
        answer=input()
        if answer.lower()=='b':
            score+=1
        print(f'\n\U0001F64C ¡Felicidades! Has terminado la parte de Física-Química. Tu promedio es de \
{grade(score,questions)}.')
        print('\U0001F440 Considera repasar en los temas que se te dificultaron. Puedes mostrar el archivo \
\"ResultadoFQ\" a tu profesor(a). ')
        resultado=open('ResultadoFQ.txt','w')
        resultado.write('Nombre del alumno: ')
        resultado.write(name)
        resultado.write('\nÁrea respondida: ')
        resultado.write(area)
        resultado.write('\nPromedio: ')
        resultado.write(grade(score,questions))
        resultado.close()
        ready=input('\n¿Quieres volver a contestar la parte de Física-Química?\n\nEscribe \"1\" para volver a contestarla.\
\nEscribe cualquier otro valor para volver al menú principal. ') 
    if ready!='1':
        firstanswer='10'
        return firstanswer

'''La siguiente función contiene la parte de Geología. Al final escribe los resultados en el archivo de texto "ResultadoG"
y regresa un valor que determina la continuidad o finalización del programa''' 
def geo():#Parte de Geología
    area='Geología'
    questions=11
    print('Estás a punto de comenzar la parte de Geología. ¿Estás listo(a)? ')
    ready=input('\n\tEscribe \"1\" para comenzar.\n\tEscribe cualquier otro valor para volver al menú principal.' )
    while ready=='1':
        score=0
        print('1'.center(100,'-'),'\nLa figura muestra cómo se potabiliza el agua que se suministra a las viviendas \
de las ciudades.\nEs importante tener una reserva de agua potable de buena calidad. El agua que se encuentra bajo tierra \
se llama agua subterránea.\n\n¿Por qué hay menos bacterias y partículas contaminantes en las aguas subterráneas que en \
las aguas de la superficie, como las de lagos y ríos?\n\n\tA. Porque cuando el agua desciende a través del suelo, será \
filtrada por las rocas y la arena.\n\tB. Porque el agua subterránea no está al aire libre, está localizada debajo de algo.\
\n\tC. Porque el agua subterránea es un agua sin muchos nutrientes para las bacterias; por eso no sobrevivirán en ella.\
\n\tD. Todas son correctas.\n\n*Cierra la ventana con la figura una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("800x650")
        win.config(bg="white")
        img=PhotoImage(file="1-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='d':
            score+=1
        print('2'.center(100,'-'),'\nLa potabilización del agua suele hacerse en varias etapas, que requieren \
técnicas diferentes. El proceso de potabilización mostrado en la figura comprende cuatro etapas (numeradas de 1 a 4). \
En la segunda etapa, el agua se recoge en un decantador.\n\n¿De qué forma contribuye esta etapa a que el agua esté \
más limpia?\n\n\tA. El agua se hace menos ácida.\n\tB. Las bacterias del agua mueren.\n\tC. Se añade oxígeno al agua.\
\n\tD. La grava y la arena se depositan en el fondo.\n\n*Cierra la ventana con la figura una vez que estés listo(a) \
para contestar ')
        win=Tk()
        win.geometry("800x650")
        win.config(bg="white")
        img=PhotoImage(file="1-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='d':
            score+=1
        print('3'.center(100,'-'),'\nEn la cuarta etapa de potabilización se añade cloro al agua. ¿Por qué se \
añade cloro al agua?\n\n\tA. El cloro mata las bacterias.\n\tB. El agua se hace menos ácida y no habrá algas.\n\tC. \
Es como el flúor.\n\tD. El cloro permite la propagación de bacterias. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('4'.center(100,'-'),'\n¿Puede el agua contaminada producir los problemas de salud siguientes? \
Escribe Verdadero o Falso para cada uno.')
        answer1=input('\n\t~Diabetes. ')
        answer2=input('\t~Diarrea. ')
        answer3=input('\t~VIH / SIDA. ')
        answer4=input('\t~Lombrices intestinales / Tenia solitaria. ')
        if answer1.lower()=='falso' and answer2.lower()=='verdadero' and answer3.lower()=='falso' and answer3.lower()=='verdadero':
            score+=1
        print('5'.center(100,'-'),'\nEl Gran Cañón está situado en un desierto de los Estados Unidos. Es un cañón \
muy largo y profundo que contiene muchos estratos de rocas. En algún momento del pasado, los movimientos de la corteza \
terrestre levantaron estos estratos. Hoy en día el Gran Cañón tiene 1,6 km de profundidad en algunas zonas. El río \
Colorado fluye por el fondo del cañón.\nMira la foto del Gran Cañón, tomada desde su orilla sur. En las paredes del \
cañón se pueden ver los diferentes estratos de rocas.\nCada año unos cinco millones de personas visitan el parque \
nacional del Gran Cañón. Existe preocupación por el deterioro que está sufriendo el parque debido al elevado número \
de visitantes.\n\n¿Es posible responder la pregunta siguiente mediante una investigación científica? Escribe Sí o No.\
\n\n\t\"¿El parque es tan bello como lo era hace 100 años?\"\n\n*Cierra la ventana con la foto una vez que estés \
listo(a) para contestar ')
        win=Tk()
        win.geometry("700x350")
        win.config(bg="white")
        img=PhotoImage(file="2-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='no':
            score+=1
        print('6'.center(100,'-'),'\nLa temperatura en el Gran Cañón varía de menos de 0°C a más de 40°C. Aunque \
la zona es desértica, las grietas de las rocas a veces contienen agua. ¿De qué manera estos cambios de temperatura y \
la presencia de agua en las grietas de las rocas contribuyen a acelerar el desmenuzamiento de las rocas?\n\n\tA. El \
agua congelada disuelve las rocas calientes.\n\tB. El agua cementa a las rocas entre sí.\n\tC. El hielo pule la \
superficie de las rocas.\n\tD. El agua congelada se dilata en las grietas de las rocas. ')
        answer=input()
        if answer.lower()=='d':
            score+=1
        print('7'.center(100,'-'),'\nEn el estrato de caliza A del Gran Cañón se encuentran muchos fósiles de \
animales marinos, como almejas, peces y corales.\n\n¿Qué sucedió hace millones de años para que aparezcan estos \
fósiles en este estrato?\n\n\tA. Antiguamente los habitantes transportaban alimentos marinos desde el océano a \
esta área.\n\tB. En otro tiempo, los océanos eran más violentos, y olas gigantes arrastraban criaturas marinas \
hacia el interior.\n\tC. En esa época, la zona estaba cubierta por un océano que más tarde se retiró.\n\tD. \
Algunos animales marinos vivieron una vez sobre la tierra antes de emigrar al mar.\n\n*Cierra la ventana con \
la foto una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("700x350")
        win.config(bg="white")
        img=PhotoImage(file="2-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('8'.center(100,'-'),'\nEl 8 de junio del 2004 fue posible ver, desde numerosos lugares de la \
Tierra, el paso del  planeta  Venus  por  delante  del  Sol.  A  esto  se  le  llama  el  “tránsito”  de  Venus,  \
y  sucede  cuando  la  órbita  de  Venus  sitúa  a  este  planeta  entre  el  Sol  y  la  Tierra.  El  tránsito \
anterior de Venus sucedió en 1882.\nEn la imagen se puede observar una foto del tránsito de Venus de 2004. Se \
enfocó el telescopio hacia el Sol, y se proyectó la imagen en una hoja blanca de papel.\n\n¿Por qué se observó \
el tránsito proyectando la imagen en una hoja blanca en lugar de mirar directamente por el telescopio?\n\n\tA. \
La luz del Sol es tan intensa que no se ve el planeta Venus.\n\tB. El Sol es tan grande que puede verse sin \
necesidad de aumentos.\n\tC. Observar el Sol a través de un telescopio puede dañar los ojos.\n\tD. Era necesario \
reducir la imagen para proyectarla en una hoja.\n\n*Cierra la ventana con la foto una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("475x300")
        win.config(bg="white")
        img=PhotoImage(file="3-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('9'.center(100,'-'),'\nDe los planetas siguientes, ¿cuál puede ser observado algunas veces desde \
la Tierra en tránsito delante del Sol?\n\n\tA. Mercurio.\n\tB. Marte.\n\tC. Júpiter. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('10'.center(100,'-'),'\n\"Los astrónomos  predicen  que  se  producirá  un  tránsito  de Saturno  \
delante  del  Sol, que se verá desde Neptuno en algún momento de este siglo\".\n\nDel texto anterior, ¿cuáles  \
serían  las palabras  más  útiles  para  buscar  en  Internet o en una biblioteca el momento en el que se va a \
producir este tránsito?\n\n\tA. Saturno/Neptuno/Tránsito.\n\tB. Tránsito/Saturno/Sol/Neptuno.\n\tC. Astrónomos\
/Tránsito/Saturno/Neptuno. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('11'.center(100,'-'),'\nLee el texto contenido en la ventana.\n\n¿Qué frase explica por qué hay \
día y noche en la Tierra?\n\n\tA. La Tierra gira alrededor del Sol.\n\tB. El Sol gira alrededor de su eje.\n\tC. \
El eje de la Tierra está inclinado.\n\tD. La Tierra gira alrededor de su eje.\n\n*Cierra la ventana con el texto \
una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("850x450")
        win.config(bg="white")
        img=PhotoImage(file="4-Geología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='d':
            score+=1
        print(f'\n\U0001F64C ¡Felicidades! Has terminado la parte de Geología. Tu promedio es de {grade(score,questions)}.')
        print('\U0001F440 Considera repasar en los temas que se te dificultaron. Puedes mostrar el archivo \
\"ResultadoG\" a tu profesor(a). ')
        resultado=open('ResultadoG.txt','w')
        resultado.write('Nombre del alumno: ')
        resultado.write(name)
        resultado.write('\nÁrea respondida: ')
        resultado.write(area)
        resultado.write('\nPromedio: ')
        resultado.write(grade(score,questions))
        resultado.close()
        ready=input('\n¿Quieres volver a contestar la parte de Geología?\n\nEscribe \"1\" para volver a contestarla.\
\nEscribe cualquier otro valor para volver al menú principal. ') 
    if ready!='1':
        firstanswer='10'
        return firstanswer
    
'''La siguiente función contiene la parte de tecnología. Al final escribe los resultados en el archivo de texto "ResultadoT"
y regresa un valor que determina la continuidad o finalización del programa''' 
def tec():
    area='Tecnología'
    questions=10
    print('Estás a punto de comenzar la parte de Tecnología. ¿Estás listo(a)? ')
    ready=input('\n\tEscribe \"1\" para comenzar.\n\tEscribe cualquier otro valor para volver al menú principal.' )
    while ready=='1':
        score=0
        print('1'.center(100,'\''),'\nMucha gente piensa que la energía eólica es una fuente de energía eléctrica \
que puede reemplazar las centrales térmicas de petróleo y de carbón. Las estructuras que se observan en la foto son \
aerogeneradores con palas que el viento hace girar. Estos giros producen energía eléctrica en unos generadores que \
son movidos por las palas del rotor.\n\n*Cierra la ventana con la imagen para continuar ')
        win=Tk()
        win.geometry("425x125")
        win.config(bg="white")
        img=PhotoImage(file="1-Tecnología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        print('\nLas gráficas siguientes representan la velocidad media del viento en cuatro lugares diferentes en \
el transcurso de un año. ¿Qué gráfica indica el lugar más apropiado para la instalación de un aerogenerador?\
\n\n\tA\n\tB\n\tC\n\tD\n\n*Cierra la ventana con las gráficas una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("675x425")
        win.config(bg="white")
        img=PhotoImage(file="2-Tecnología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('2'.center(100,'\''),'\nA mayor fuerza del viento, las palas del aerogenerador giran más rápido y \
más electricidad se genera. No obstante, en la realidad no existe una relación directa entre la velocidad del viento \
y la electricidad generada. A continuación se presentan cuatro condiciones de trabajo reales en el funcionamiento de \
un aerogenerador:\n\n\t~Las palas empezarán a girar cuando el viento llegue a la velocidad V1.\n\t~Por razones de \
seguridad, el giro de las palas no aumentará cuando la velocidad del viento sea superior a V2.\n\t~La producción de \
electricidad llega a su máximo (W) cuando la velocidad del viento es V2.\n\t~Las palas dejarán de girar cuando el \
viento alcance la velocidad V3.\n\nDe las siguientes gráficas, ¿cuál es la que mejor representa la relación entre \
la velocidad del viento y la electricidad generada, teniendo en cuenta las cuatro condiciones de trabajo anteriormente \
mencionadas?\n\n\tA\n\tB\n\tC\n\tD\n\n*Cierra la ventana con las gráficas una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("675x425")
        win.config(bg="white")
        img=PhotoImage(file="3-Tecnología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='b':
            score+=1
        print('3'.center(100,'\''),'\nA igual velocidad del viento, si los aerogeneradores están situados a mayor \
altitud, giran con mayor lentitud. Entre las razones siguientes, ¿cuál es la que mejor explica por qué las palas de \
los aerogeneradores giran más despacio en los lugares situados a mayor altitud, a igual velocidad del viento?\n\n\tA. \
El aire es menos denso cuando aumenta la altitud.\n\tB. La temperatura es más baja cuando aumenta la altitud.\n\tC. \
La gravedad disminuye cuando aumenta la altitud.\n\tD. Llueve más a menudo cuando aumenta la altitud. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('4'.center(100,'\''),'\nDe las afirmaciones que aparecerán a continuación, escribe Ventaja o \
Desventaja según sea el caso en la producción de energía eléctrica a partir de la energía eólica en comparación \
a la producción de energía eléctrica a partir de los combustibles fósiles, como el carbón y el petróleo. ')
        answer1=input('\n\tNo se emite dióxido de carbono (CO2). ')
        answer2=input('\tEn algunos casos, provoca contaminación acústica. ')
        answer3=input('\tSe destruyen los paisajes naturales (impacto visual). ')
        answer4=input('\tUtiliza la fuerza de la naturaleza o es una energía limpia. ')
        if answer1.lower()=='ventaja' and answer2.lower()=='desventaja' and answer3.lower()=='desventaja' and answer4.lower()=='ventaja':
            score+=1
        print('5'.center(100,'\''),'\n\U0001F31F A Tomás le gusta mirar las estrellas. Sin embargo, no puede \
observarlas muy bien por la noche porque vive en una gran ciudad.\nEl  año  pasado  Tomás  fue  al  campo  y  escaló  una  montaña  desde  donde  observó un gran número de estrellas que no puede ver habitualmente cuando está en la ciudad. \U0001F31F ')
        print('\n¿Por qué se pueden observar más estrellas en el campo que en las ciudades donde vive la mayoría de \
la gente?\n\n\tA. La luna es más luminosa en las ciudades y amortigua la luz de muchas estrellas.\n\tB. Hay más polvo \
que refleja la luz en el aire del campo que en el aire de la ciudad.\n\tC. La luminosidad de las luces de la ciudad \
dificulta la visibilidad de las estrellas.\n\tD. El aire de la ciudad es más caliente por el calor que emiten los \
coches, las máquinas y las casas. ')
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('6'.center(100,'\''),'\nPara  observar  estrellas  de  escaso  brillo, Tomás utiliza un  telescopio \
con  una  lente  de gran diámetro.\n¿Por  qué  un  telescopio  con  una  lente  de  gran  diámetro  permite  observar  \
las  estrellas de escaso brillo?\n\n\tA. Cuanto mayor es la lente más luz capta.\n\tB. Cuanto mayor es la lente mayor \
es el aumento.\n\tC. Las lentes grandes permiten ver más cantidad de cielo.\n\tD. Las lentes grandes detectan los \
colores oscuros en las estrellas. ')
        answer=input()
        if answer.lower()=='a':
            score+=1
        print('7'.center(100,'\''),'\nLee el el fragmento contenido en la ventana.\n\nSi Peter quiere estar \
seguro de que está recomendando lo correcto, quizá deba obtener más información además de sus filmaciones.\
\nDe  las  afirmaciones  que aparecerán a continuación,  ¿cuál  o  cuáles  le  ayudarían  a  estar  más  seguro  \
de  su  recomendación sobre los efectos de pintar líneas en carreteras estrechas? Escribe Verdadero o Falso.\
\n\n*Cierra la ventana con el texto una vez que estés listo(a) para contestar ')
        win=Tk()
        win.geometry("725x500")
        win.config(bg="white")
        img=PhotoImage(file="4-Tecnología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer1=input('\n\tHacer lo mismo en otras carreteras estrechas. ')
        answer2=input('\tHacer lo mismo en otras carreteras anchas. ')
        answer3=input('\tComprobar el número de accidentes un tiempo antes y después de pintar las líneas ')
        answer4=input('\tComprobar el número de coches que utilizan la carretera antes y después de pintar las líneas.')
        if answer1.lower()=='verdadero' and answer2.lower()=='falso' and answer3.lower()=='verdadero' and answer4.lower()=='falso':
            score+=1
        print('8'.center(100,'\''),'\nSe  aconseja  a  los  conductores  que  dejen  más  espacio  entre  su  vehículo  \
y  el  de  delante  cuando  viajan  a  mayor  velocidad  que  cuando  viajan  a menor  velocidad,  porque los coches que \
van más rápido necesitan más tiempo para frenar.\n\n¿Por qué un coche que va más rápido necesita más distancia para \
detenerse que un coche que va más lento?\n\n\tA. La mayor inercia de un vehículo que va más rápido significa que, \
dada la misma fuerza, avanzará más mientras reduce su velocidad que un vehículo que va más lento.\n\tB. Cuanto mayor \
es la velocidad, más tiempo se necesita para reducirla a cero, así que el coche avanzará más en este tiempo.\n\tC. \
Ambas son correctas ')
        answer=input()
        if answer.lower()=='c':
            score+=1
        print('9'.center(100,'\''),'\nAl ver la televisión, Peter ve un coche (A) que va a 45 km/h que es \
adelantado por otro coche (B) que va a 60 km/h.¿A qué velocidad le parece que va el coche B a alguien que va \
viajando en el coche A?\n\n\tA. 0 km/h.\n\tB. 15 km/h.\n\tC. 45 km/h.\n\tD. 60 km/h.\n\tE. 105 km/h. ')
        answer=input()
        if answer.lower()=='b':
            score+=1
        print('10'.center(100,'\''),'\nLee el texto sobre los tejidos contenido en la ventana.\n\n¿Qué  \
instrumento  del  equipo  del  laboratorio  sería  el  instrumento  que  necesitarías  para comprobar que la \
tela es conductora de la electricidad?\n\n\tA. Un voltímetro.\n\tB. Un fotómetro.\n\tC. Un micrómetro.\n\tD. \
Un sonómetro.\n\n*Cierra la ventana con el texto una vez que estés listo para contestar ')
        win=Tk()
        win.geometry("410x600")
        win.config(bg="white")
        img=PhotoImage(file="5-Tecnología.gif")
        lblImagen=Label(win,image=img).place(x=0,y=0)
        win.mainloop()
        answer=input()
        if answer.lower()=='a':
            score+=1
        print(f'\n\U0001F64C ¡Felicidades! Has terminado la parte de Tecnología. Tu promedio es de {grade(score,questions)}.')
        print('\U0001F440 Considera repasar en los temas que se te dificultaron. Puedes mostrar el archivo \
\"ResultadoT\" a tu profesor(a). ')
        resultado=open('ResultadoT.txt','w')
        resultado.write('Nombre del alumno: ')
        resultado.write(name)
        resultado.write('\nÁrea respondida: ')
        resultado.write(area)
        resultado.write('\nPromedio: ')
        resultado.write(grade(score,questions))
        resultado.close()
        ready=input('\n¿Quieres volver a contestar la parte de Tecnología?\n\nEscribe \"1\" para volver a contestarla.\
\nEscribe cualquier otro valor para volver al menú principal. ') 
    if ready!='1':
        firstanswer='10'
        return firstanswer

'''Las siguientes funciones corresponden a una parte "oculta de cultura general". Esta parte tiene como objetivo el hacer \
del conocimiento de los estudiantes un poco más amplio, y de una forma un poco más interactiva'''
def pregunta1():
    print('\n')
    print('\U0001F9D0'*30)  
    sabores=['dulce','amargo','ácido','salado','umami']
    print('\nEl gusto es uno de nuestros cinco sentidos. Los sabores primarios son:\n') 
    for i in range(4):
        print(sabores[i])
    sabor=input('y...\n\nCompleta la lista escribiendo el último sabor ')
    if sabor.lower() in sabores:
        print('\n¡Correcto!, los sabores primarios son: ',', '.join(sabores))
    else:
        print('\n¡Incorrecto!, los sabores primarios son: ',', '.join(sabores))
def pregunta2():
    print('\n')
    print('\U0001F9D0'*30)
    resp=input('\n¿Cuál es el lugar de origen del autor de La Odisea?\n\n¿Springfield o Grecia? (escribe tu respuesta) ')
    if resp.lower()=='grecia':
        print('\n¡Correcto!, el autor de La Odisea es Homero, de Grecia. ')
    else:
        print('\n¡Incorrecto! El autor de La Odisea es Homero, de Grecia. ')
def pregunta3():
    sigla='FIFA'
    sigla2='Federation Internationale Football Association'
    lista=[]
    print('\n')
    print('\U0001F9D0'*30)
    print('\nCompleta las siglas de la federación internacional del fut bol. ')
    for i in sigla:
        print(i)
        palabra=input()
        i+=palabra.lower()
        lista.append(i)
    lista=' '.join(lista)
    if lista==sigla2:
        print(f'\n¡Correcto! La FIFA es la {sigla2}. ')
    else:
        print(f'\n¡Inorrecto! La FIFA es la {sigla2}. ') 
def pregunta4():
    print('\n')
    print('\U0001F9D0'*30)
    print('\nEl padre del psicoanálisis es Sigmund... ')
    resp=input()
    if resp.lower()=='freud':
        print('\n¡Correcto! El padre del psicoanálisis es Sigmund Freud ')
    else:
        print('\n¡Incorrecto! El padre del psicoanálisis es Sigmund Freud ')
def pregunta5():
    sistema=['Sol','Mercurio','Venus','Tierra','Marte','Júpiter','Saturno', 'Urano', 'Neptuno']
    print('\n')
    print('\U0001F9D0'*30)
    print('\nEscribe el número que corresponde al planeta Marte dentro del Sistema Solar. ')
    resp=(input())
    if resp=='4':
        print('\n¡Correcto! Marte es el 4° planeta del Sistema Solar. ')
        for i in range(1,len(sistema)):
            print(f'{i}.- {sistema[i]}')
    else:
        print('\n¡Incorrecto! Marte es el 4° planeta del Sistema Solar. ')
        for i in range(1,len(sistema)):
            print(f'{i}.- {sistema[i]}')
def pregunta6():
    print('\n')
    print('\U0001F9D0'*30)
    print('\n¿Cuántas patas tiene una araña? Ingresa un \"1\" por cada pata, y un \"*\" cuando hayas terminado. ')
    resp='0'
    lista=[]
    while resp!='*':
        resp=input()
        if resp=='1':
            lista.append(resp)
    if len(lista)==8:
        print('\n¡Correcto! Una araña tiene 8 patas. ')
    else:
        print('\n¡Incorrecto! Una araña tiene 8 patas. ')
def pregunta7():
    print('\n')
    print('\U0001F9D0'*30)
    print('\n¿Quién era el general de los nazis en la Segunda Guerra Mundial?\n\nAdolf... ')
    resp=input()
    if resp.lower()=='hitler':
        print('\n¡Correcto!: Adolf Hitler; uno de los personajes más tristemente recordados del siglo XX. ')
    else:
        print('\n¡Incorrecto!: Adolf Hitler; uno de los personajes más tristemente recordados del siglo XX. ')
def pregunta8():
    print('\n')
    print('\U0001F9D0'*30)
    print('\nIngresa los valores (en orden) de los primeros 5 números primos. Ingresa un \"*\" cuando termines. ')
    nprimos=['2','3','5','7','11']
    lista=[]
    resp='0'
    while resp!='*':
        resp=input()
        if resp!='*':
            lista.append(resp)
    if lista==nprimos:
        print('\n¡Correcto! Los primeros 5 números primos son:\n')
    else:
        print('\n¡Incorrecto! Los primeros 5 números primos son:\n')
    for i in range(5):
            print(nprimos[i])  
def pregunta9():
    print('\n')
    print('\U0001F9D0'*30)
    notas=['Si','Fa','Do','Mi','Re', 'Sol', 'La']
    notasorden=['Do','Re','Mi','Fa','Sol','La','Si']
    print(f'\nLas notas musicales, en desorden, son: {notas}.\n\n¿Cuál es la tercera nota EN ORDEN? ')
    resp=input()
    if resp.lower()==notasorden[2].lower():
        print(f'\n¡Correcto! El orden de las notas es: {notasorden}.')
    else:
        print(f'\n¡Incorrecto! El orden de las notas es: {notasorden}.')     
def pregunta10():
    print('\n')
    print('\U0001F9D0'*30)
    resp=input('\nEl fundador de Facebook se llama Clark Zuckerberg. ¿Verdadero o Falso? ')
    if resp.lower()=='falso':
        print('\n¡Correcto! Mark Zuckerberg es el fundador de esta conocida red social. ')
    else:
        print('\n¡Incorrecto! Mark Zuckerberg es el fundador de esta conocida red social. ')

#Inicio del programa
print('\U0001F600 ¡Bienvenido(a)!\nEste es un programa que tiene como fin ayudarte a repasar algunos de los temas \
del área de ciecias de la prueba PISA.\n\nInstrucciones:\n\n\t~Este programa contiene una serie de preguntas que te \
permitirán comprender la dinámica de la prueba PISA.\n\t~Existen preguntas de opción múltiple, para las cuales \
deberás introducir la letra correspondiente al inciso de la respuesta correcta y presionar Enter.\n\t~En algunas \
preguntas escribirás palabras, por lo que tendrás que ingresar una de acuerdo a la indicación de la \
pregunta y presionar Enter para continuar.\n\t~En algunas preguntas te aparecerá una ventana emergente con su \
gráfico correspondiente. Atiende a la indicación de la pregunta para saber qué hacer con él.\n')
name=input('\nEscribe tu nombre completo a continuación ')
firstans='10'
while firstans!='0':
    print('-'*100)
    firstans=(input('Introduce el número correspondiente al área que deseas reforzar:\n\n\t1.Biología\t\U0001F340\
\n\t2.Física-Química\U0001F4E1\n\t3.Geología\t\U0001F30D\n\t4.Tecnología\t\U0001F4BB\n\n\tIngresa cualquier otro \
valor para salir \U0001F6D1\n'))
    if firstans=='1':
        firstans=bio()
    elif firstans=='2':
        firstans=fis_quim()
    elif firstans=='3':
        firstans=geo()
    elif firstans=='4':
        firstans=tec()
    else:
        secondans='10'
        while secondans!='0':
            print('-'*100)
            secondans=input('Has descubierto una zona secreta \U0001F92B\n\nEsta sección secreta consiste en \
una serie de preguntas de cultura general, la cual no implica puntuación o promedio alguno.\n\nEscribe uno de \
los siguentes números para elegir su opción correspondiente.\n\n\t1. Orden 1.\n\t2. Orden 2.\n\t3. Volver al \
menú principal.\n\nEscribe cualquier otro valor para salir definitivamente. ')
            if secondans=='1':
                pregunta1()
                pregunta2()
                pregunta3()
                pregunta4()
                pregunta5()
                thirdans=input('\nHas concluido esta sección. Presiona Enter para regresar al menú de cultura general. ')
                secondans='10'
            elif secondans=='2':
                pregunta6()
                pregunta7()
                pregunta8()
                pregunta9()
                pregunta10()
                thirdans=input('\nHas concluido esta sección. Presiona Enter para regresar al menú de cultura general. ')
                secondans='10'
            elif secondans=='3':
                secondans='0'
                firstans='10'
            else:
                secondans='0'
                firstans='0'
print('\nVuelve cuando lo consideres necesario \U0001F609 ')    
 