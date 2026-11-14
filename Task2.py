from OpenGL.GL import *      
from OpenGL.GLUT import *    
from OpenGL.GLU import *    
import random
import time


ball_size = 5
ball_speed = 0.03
blink_state = False
show_blink = True
Freeze = False
Balls = []
last_blink_time = time.time()


def draw_point(x, y, size):
    
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def convert_coordinate(x, y):
    
    a = x - (600 / 2)
    b = (500/ 2) - y
    return a, b



def keyboard_listener(key, x, y):
    global Freeze
    if key == b' ':
        Freeze = not Freeze

    glutPostRedisplay()



def mouse_listener(button, state, x, y):
    global Balls, blink_state, Freeze
    if Freeze:
        return
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        px, py = convert_coordinate(x, y)

        x1= random.choice([-1, 1])
        y1= random.choice([-1, 1])
        clr = (random.random(), random.random(), random.random())
        Balls.append([px, py, x1, y1, clr])
        

    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        blink_state = not blink_state
        
        
def special_key_listener(key, x, y):
    global ball_speed, Freeze
    if Freeze:
        return
    if key == GLUT_KEY_UP:
        ball_speed *= 1.99
       
    elif key == GLUT_KEY_DOWN:
        ball_speed /= 1.99
       

    glutPostRedisplay()

       



def setup_projection():
    
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300, -250, 250, 0, 1)
    glMatrixMode(GL_MODELVIEW)



def display():

    glClearColor(0,0,0,1)  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()

    for count in Balls:
        ball_x, ball_y, x1, y1, clr =count
        if blink_state and  not show_blink:
            glColor3f(0,0,0)  
        else:
            glColor3f(*clr)
        draw_point(ball_x, ball_y, ball_size)

    glutSwapBuffers()


def animate():
    
    
    
    global Balls, ball_speed, blink_state, show_blink, Freeze, last_blink_time

    
    if Freeze:
        
        glutPostRedisplay()
        return

    
    for cntrl in Balls:
        
        cntrl[0] +=cntrl[2] * ball_speed
        cntrl[1] +=  cntrl[3] * ball_speed

        if  cntrl[0]>300 or  cntrl[0]<-300:
            cntrl[2] *= -1

        if  cntrl[1]>250 or  cntrl[1]<-250:
            cntrl[3] *= -1

    
    if blink_state:
        
        ctrnt = time.time()

        if ctrnt - last_blink_time >= 0.4:
            last_blink_time = ctrnt
            show_blink = not show_blink

    glutPostRedisplay()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600,500)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b"Amazing Box")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)

    glutMainLoop()



if __name__ == "__main__":
    main()