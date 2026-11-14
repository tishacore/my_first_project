from OpenGL.GL import *      
from OpenGL.GLUT import *    
from OpenGL.GLU import *  
import random   

clr=0.0
rain_move=0
total_drops = 350
rain_drops = []
for i in range(total_drops):
    x = random.randint(10, 990) 
    y = random.randint(0, 500)
    rain_drops.append([x, y])




def draw_shapes():
    
    
    glPointSize(10)          
    glBegin(GL_TRIANGLES)      
    glColor3f(0.5,0.3,0.1)
    glVertex2f(990,300)
    glVertex2f(10,300)
    glVertex2f(10,0)
    
   
    glVertex2f(990,300)
    glVertex2f(10,0)
    glVertex2f(990,0)
    
    
    glColor3f(0.0, 1,0.0)
    glVertex2f(10,230)
    glVertex2f(30,295)
    glVertex2f(60,230)
    
    glVertex2f(60,230)
    glVertex2f(80,295)
    glVertex2f(110,230)
    
    glVertex2f(110,230)
    glVertex2f(130,295)
    glVertex2f(160,230)
    
    glVertex2f(160,230)
    glVertex2f(180,295)
    glVertex2f(210,230)
    
    glVertex2f(210,230)
    glVertex2f(230,295)
    glVertex2f(260,230)
    
    glVertex2f(260,230)
    glVertex2f(280,295)
    glVertex2f(310,230)
    
    glVertex2f(310,230)
    glVertex2f(330,295)
    glVertex2f(360,230)
    
    glVertex2f(660,230)
    glVertex2f(680,295)
    glVertex2f(710,230)
    
    glVertex2f(710,230)
    glVertex2f(730,295)
    glVertex2f(760,230)
    
    glVertex2f(760,230)
    glVertex2f(780,295)
    glVertex2f(810,230)
    
    glVertex2f(810,230)
    glVertex2f(830,295)
    glVertex2f(860,230)
    glVertex2f(860,230)
    glVertex2f(880,295)
    glVertex2f(910,230)
    
    glVertex2f(910,230)
    glVertex2f(930,295)
    glVertex2f(960,230)
    
    glVertex2f(960,230)
    glVertex2f(970,295)
    glVertex2f(990,230)
    
    
    glColor3f(0.3, 0.7,1)
    glVertex2f(500,320)
    glVertex2f(250,250)
    glVertex2f(750,250)
    
    glColor3f(1.0, 1.0,1)
    glVertex2f(325,150)
    glVertex2f(325,250)
    glVertex2f(675,250)
  
             
        
    glColor3f(1.0, 1.0,1)
    glVertex2f(325,150)
    glVertex2f(675,150)
    glVertex2f(675,250)
   
    glColor3f(0.3, 0.7,1)
    glVertex2f(480,150)
    glVertex2f(480,210)
    glVertex2f(530,210)
       
    glColor3f(0.3, 0.7,1)
    glVertex2f(480,150)
    glVertex2f(530,210)
    glVertex2f(530,150)
   
    
        
    glColor3f(0.0, 0.0,0)
    glVertex2f(510,180)
    glVertex2f(520,180)
    glVertex2f(520,190)
   
    glColor3f(0.0, 0.0,0)
    glVertex2f(510,180)
    glVertex2f(510,190)
    glVertex2f(520,190)
   
    glColor3f(0.3, 0.7,1)
    glVertex2f(450,190)
    glVertex2f(450,210)
    glVertex2f(430,190)
   
   
    glVertex2f(450,210)
    glVertex2f(430,210)
    glVertex2f(430,190)
    
    glColor3f(0.3, 0.7,1)
    glVertex2f(560,190)
    glVertex2f(560,210)
    glVertex2f(580,210)
    
    glVertex2f(580,210)
    glVertex2f(560,190)
    glVertex2f(580,190)
    
    glEnd() 
    
    
          
    glBegin(GL_LINES) 
    glColor3f(0.0, 0.0,0)
    glVertex2f(570,190)
    glVertex2f(570,210)
    glVertex2f(560,200)
    glVertex2f(580,200)
    
    glVertex2f(430,200)
    glVertex2f(450,200)
    glVertex2f(440,190)
    glVertex2f(440,210)
    
    
    glEnd()
    rain_func()

def rain_func():
    glColor3f(0.4, 0.8, 0.9)
    glLineWidth(1)
    glBegin(GL_LINES)
    
    for count in rain_drops:
        x1= count[0]
        y1=count[1]
        x2=x1 + (rain_move * 30)
        y2=y1-15
        if x1<10 or x2<10:
            continue
        
        
        if x1>990 or x2>990:
            continue
       
        glVertex2f(x1, y1)
        
        glVertex2f(x2,y2)
        
    glEnd()
      
def setup_projection():
    glViewport(0, 0, 1000, 500)     
    glMatrixMode(GL_PROJECTION)   
    glLoadIdentity()               
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)    
    
    
    
def animate():
    global rain_drops, rain_move
    for count  in rain_drops:
        count[1] -=0.5         
        count[0] += rain_move     
        
        
        if count[1] < 0:
            count[1] = random.randint(500, 520)
            count[0] = random.randint(10, 990)
            
       
        if count[0] < 10:
           count[0] = 990
        elif count[0] > 990:
            count[0] = 10
            
    glutPostRedisplay()
    
     
    
def change_bg():
    global clr
    glColor3f(clr,clr,clr)
    glBegin(GL_TRIANGLES)
    glVertex2f(10,300)
    glVertex2f(10,500)
    glVertex2f(990,500)
    
    glVertex2f(10,300)
    glVertex2f(990,300)
    glVertex2f(990,500)
    glEnd() 
 
def  keyboard_listener(key,x,y):
    global clr
    if key==b'b':
        clr+=0.01
        if clr>1:
            clr=1
    if key==b'w':
        clr-=0.01
        if clr<0:
            clr=0
        
def special_key_listener(key,x,y):
    global rain_move
    
    if key == GLUT_KEY_LEFT:
        rain_move -= 0.05 
    elif key == GLUT_KEY_RIGHT:
        rain_move += 0.05   
    
      
            
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                    
    setup_projection()                                  
    change_bg()
    draw_shapes()                                   
    glutSwapBuffers()                                   

def main():
    glutInit()                              
    glutInitDisplayMode(GLUT_RGBA)           
    glutInitWindowSize(1000, 500)             
    glutInitWindowPosition(350,100)            
    glutCreateWindow(b"House in Rainfall")     
    glutDisplayFunc(display)                 
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutIdleFunc(animate)
    glutMainLoop()  
if __name__ == "__main__":
    main()                 
    
    

