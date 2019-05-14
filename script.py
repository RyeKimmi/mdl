import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    print symbols

    systems = [tmp]
    for command in commands:
        print command
        if command == 'push''':
            systems.append( [x[:] for x in systems[-1]] )
        elif command == 'pop''':
            systems.pop()
        elif command == 'move':
            for 
        elif command == 'scale':
            pass
        elif command == 'rotate':
            pass
        elif command == 'box':
            pass
        elif command == 'sphere':
            pass
        elif command == 'torus':
            pass
        elif command == 'constants''':
            pass
        elif command == 'line':
            pass
        elif command == 'save':
            pass
        elif command == 'display':
            pass
