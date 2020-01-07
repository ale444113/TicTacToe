#Importaciones
import PySimpleGUI as sg
import sys
import os

#Variables
encendido = True
turno = 1
lista = ['VACIO','','','','','','','','','']

#Layouts
layout = [[sg.Button('',key = '1',size = (5,3)),sg.Button('',key = '2',size = (5,3)),sg.Button('',key = '3',size = (5,3))],
          [sg.Button('',key = '4',size = (5,3)),sg.Button('',key = '5',size = (5,3)),sg.Button('',key = '6',size = (5,3))],
          [sg.Button('',key = '7',size = (5,3)),sg.Button('',key = '8',size = (5,3)),sg.Button('',key = '9',size = (5,3))],
          [sg.Text('Turno de Jugador 1',key = 'texto')]
          ]

player1 = [[sg.Text('JUGADOR 1 GANA!',text_color = 'red', auto_size_text= True )],
           [sg.Button('Vover a Jugar',key = 'jug',size = (10,2))],
           [sg.Button('Salir', key = 'salir')]
           ]
player2 = [[sg.Text('JUGADOR 2 GANA!',text_color = 'red', auto_size_text= True )],
           [sg.Button('Vover a Jugar',key = 'jug',size = (10,2))],
           [sg.Button('Salir', key = 'salir')]
           ]
empate = [[sg.Text('EMPATE NINGUN JUGADOR GANA!',text_color = 'red', auto_size_text= True )],
           [sg.Button('Vover a Jugar',key = 'jug',size = (10,2))],
           [sg.Button('Salir', key = 'salir')]
           ]

#Mainloop
root = sg.Window('Tic Tac Toe').Layout(layout)

#Funciones
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def j1(x):
    global turno
    if events == str(x) and lista[x] == '':
        root.FindElement(str(x)).Update(text='X')
        lista[x] = '1'
        root.FindElement('texto').Update('Turno de Jugador 2')
        turno = 2
        root.Refresh()

def j2(y):
    global turno
    if events == str(y) and lista[y] == '' and turno == 2:
        root.FindElement(str(y)).Update(text='0')
        lista[y] = '2'
        root.FindElement('texto').Update('Turno de Jugador 1')
        turno = 1
        root.Refresh()

while encendido:
    events,values = root.read()

    if turno == 1:
        j1(1)
        j1(2)
        j1(3)
        j1(4)
        j1(5)
        j1(6)
        j1(7)
        j1(8)
        j1(9)

    elif turno == 2:
        j2(1)
        j2(2)
        j2(3)
        j2(4)
        j2(5)
        j2(6)
        j2(7)
        j2(8)
        j2(9)
    """JUGADOR 1"""
    if lista[1] == '1' and lista[2] == '1' and lista[3] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2,values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[3] == '1' and lista[6] == '1' and lista[9] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[7] == '1' and lista[8] == '1' and lista[9] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[1] == '1' and lista[4] == '1' and lista[7] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[2] == '1' and lista[5] == '1' and lista[8] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[1] == '1' and lista[5] == '1' and lista[9] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[3] == '1' and lista[5] == '1' and lista[7] == '1':
        root.close()
        root2 = sg.Window('Jugador1gana').Layout(player1)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()


    """JUGADOR 2"""
    if lista[1] == '2' and lista[2] == '2' and lista[3] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2,values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[3] == '2' and lista[6] == '2' and lista[9] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[7] == '2' and lista[8] == '2' and lista[9] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[1] == '2' and lista[4] == '2' and lista[7] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[2] == '2' and lista[5] == '2' and lista[8] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[1] == '2' and lista[5] == '2' and lista[9] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()
    elif lista[3] == '2' and lista[5] == '2' and lista[7] == '2':
        root.close()
        root2 = sg.Window('Jugador2gana').Layout(player2)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()

    """EMPATE"""
    if lista[1] != '' and lista[2] != '' and lista[3] != '' and lista[4] != '' and lista[5] != '' and lista[6] != '' and lista[7] != '' and lista[8] != '' and lista[9] != '':
        root.close()
        root2 = sg.Window('EMPATE').Layout(empate)
        events2, values2 = root2.read()
        if events2 == 'jug':
            restart_program()
        elif events2 == 'salir':
            sys.exit()