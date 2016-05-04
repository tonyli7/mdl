import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    points = new_matrix()
    screen = new_screen()
    ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']
    
    for command in commands:
        cmd = command[0]
        if cmd in ARG_COMMANDS:
            args = command[1:]

           
                    
            if cmd == 'line':
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult(stack[-1], points)
                draw_lines(points,screen,color)
                points=[]
                
            elif cmd == 'circle':
                add_circle( points, args[0], args[1], 0, args[2], .01 )
                matrix_mult(stack[-1],points)
                draw_lines(points,screen,color)
                points=[]
                
            elif cmd == 'bezier':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult(stack[-1], points)
                draw_lines(points,screen,color)
                points=[]
                
            elif cmd == 'hermite':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult(stack[-1], points)
                draw_lines(points,screen,color)
                points=[]
                
            elif cmd == 'sphere':
                add_sphere( points, args[0], args[1], args[2], args[3], 5 )
                matrix_mult(stack[-1], points)
                draw_polygons(points,screen,color)
                
                points=[]
                
            elif cmd == 'torus':
                add_torus( points, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult(stack[-1], points)
                draw_polygons(points,screen,color)
                points=[]
                
            elif cmd == 'box':
                add_box( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult(stack[-1], points)
                draw_polygons(points,screen,color)
                points=[]

            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult(stack[-1], s)
                stack[-1] = s

            elif cmd == 'move':
                t = make_translate( args[0], args[1], args[2] )
                
                matrix_mult( stack[-1], t )
                stack[-1] = t
                
            elif cmd == 'rotate':
               
                axis = args[0]
                angle = args[1] * ( math.pi / 180 )
               
               
                if axis == 'x':
                    r = make_rotX( angle )
                elif axis == 'y':
                    r = make_rotY( angle )
                elif axis == 'z':
                    r = make_rotZ( angle )
                matrix_mult( stack[-1], r)
                stack[-1] = r

        elif cmd == 'ident':
            ident( stack )
            
        elif cmd == 'apply':
            matrix_mult( stack, points )
            
        elif cmd == 'push':
            stack.append(stack[-1])
            
        elif cmd == 'pop':
            stack.pop()

        elif cmd == 'clear':
            points = []

        elif cmd in ['display', 'save' ]:
            
            #draw_polygons( points, screen, color )
            
            if cmd == 'display':
                display( screen )
                screen = new_screen()

            elif cmd == 'save':
                save_extension( screen, commands[c].strip() )
                
        elif cmd == 'quit':
            return    
        elif cmd[0] != '#' or cmd[0] != '/':
            print 'Invalid command: ' + cmd
        
