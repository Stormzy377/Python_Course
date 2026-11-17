import turtle
import math
import random
import time

tela = turtle.Screen()
tela.title("Coração")
tela.bgcolor("black")
tela.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

frases = [
    "Te amo", "I love you", "Je t'aime", "Ich liebe dich", 
    "Ti amo", "Te quiero", "Eu te amo", "Aishiteru", 
    "S'agapo", "Mahal kita", "Saranghae", "Kocham cie"
]

def coracao_pos(t_val, escala=15):
    x = 16 * (math.sin(t_val) ** 3)
    y = 13 * math.cos(t_val) - 5 * math.cos(2 * t_val) - 2 * math.cos(3 * t_val) - math.cos(4 * t_val)
    return x * escala, y * escala


t.penup()
passo = 0.1
fade_cores = ["#4d1a1a", "#802626", "#b33333", "#e64d4d", "#ff4d4d"]

for i in range(-31, 32):
    t_val = i * passo
    x, y = coracao_pos(t_val, escala=15)
    
    t.goto(x, y)
    frase_atual = random.choice(frases)
    
    for cor in fade_cores:
        t.color(cor)
        t.write(frase_atual, align="center", font=("Georgia", 10, "italic bold"))
        time.sleep(0.002)
    time.sleep(0.01)

for escala_interna in range(13, 2, -2):
    passo_interno = 0.5 if escala_interna > 5 else 0.8
    
    t_valores_internos = [i * passo_interno for i in range(int(-math.pi/0.5), int(math.pi/0.5) + 1)]
    
    for t_val in t_valores_internos:
        fator_x = random.uniform(0.85, 0.98)
        fator_y = random.uniform(0.85, 0.98)
        
        x, y = coracao_pos(t_val, escala=escala_interna * fator_x)
        y = y * fator_y
        
        t.penup()
        t.goto(x, y)
        
        frase_atual = random.choice(frases)
        tamanho_fonte = max(6, escala_interna - 1)
        
        t.color(random.choice(["#ff6b81", "#ff4d4d", "#ff7979", "#ff94a2", "#ffa3b1"]))
        t.write(frase_atual, align="center", font=("Georgia", tamanho_fonte, "normal"))
        
        time.sleep(0.008)

turtle.done()