import turtle as tu

tu.speed(5)

#Conocemos nuestra posición de inicio
print(tu.position())

#Cambiamos la forma del cursor a "tortuga"
tu.shape("turtle")

#Vamos a la posición que queremos y creamos el suelo
tu.pencolor(0,150,0)
tu.pensize(5)
tu.penup()
tu.goto(-300,-200)
tu.pendown()
tu.forward(600)

#Cambiamos de posición
tu.penup()
tu.goto(-150,-200)
tu.pendown()

#Creamos la base de la casa
tu.pencolor(150,0,0)
def casa():
  for c in range(4):
    tu.forward(100)
    tu.left(90)

casa()

#Vamos a la posición del tejado
tu.penup()
tu.right(270)
tu.forward(100)
tu.right(90)
tu.pendown()

#Creamos el tejado
tu.pencolor(0,0,150)
def tejado():
  for t in range(3):
    tu.forward(100)
    tu.left(120)
    
tejado()

#Creamos la puerta
tu.penup()
tu.goto(-125,-200)
tu.pendown()
tu.pencolor("black")

def puerta():
  for p in range(4):
    tu.forward(50)
    tu.left(90)
    
puerta()

#Vamos a la posición de la ventana1
tu.penup()
tu.left(90)
tu.forward(75)
tu.pendown()

#Creamos ventana1
def ventana():
  for v in range(4):
    tu.forward(15)
    tu.right(90)
    
ventana()

posicion1=tu.position()
print(posicion1)

#Creamos ventana2
tu.penup()
tu.goto(-90,-125)
tu.pendown()
ventana()

tu.penup()
tu.goto(50,-200)
tu.pendown()

#Creamos el árbol
tu.pensize(10)
tu.pencolor(0,50,0)
tu.forward(100)

def arbol():
  for c in range(4):
    tu.color(0,100,0)
    tu.fillcolor(0,100,0)
    tu.begin_fill()
    tu.circle(25)
    tu.end_fill()
    tu.right(90)

arbol()

tu.penup()
tu.forward(200)
tu.right(45)
tu.forward(75)
tu.pendown()


#Creamos un sol gigante
def sol():
  for s in range(36):
    tu.speed(15)
    tu.color("yellow")
    tu.fillcolor("yellow")
    tu.begin_fill()
    tejado()
    tu.end_fill()
    tu.right(10)

sol()


  
  
  
  












    



