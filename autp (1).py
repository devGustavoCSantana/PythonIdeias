import turtle
import math

# Configuração da tartaruga e do fundo
t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

# Função que calcula o formato de um coração
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Loop para desenhar vários corações de diferentes tamanhos
t.penup()
for i in range(1, 15):  # Começamos de 1 para evitar multiplicação por zero
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 360):  # Desenha o coração com 360 pontos
        angle = math.radians(n)  # Converte para radianos
        x, y = corazon(angle)
        t.goto(x * i, y * i)  # Escala o coração por 'i'
    t.penup()

t.hideturtle()
turtle.done()
