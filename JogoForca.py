import pyglet
import string
from pyglet.gl import *
from random import choice

window = pyglet.window.Window(width = 1280, height = 720, caption = 'Jogo da Forca')
logo = image = pyglet.resource.image("resource/forca.png")
window.set_icon(logo)

class Game:
        
    def __init__(self, palavra_correta):
        self.errado = 0                                     # Quantas vezes o jogador errou
        self.testado = []                                   # Quantas letras foram tentadas
        self.palavra_correta = palavra_correta.lower()      # palavra correta
        
        self.palavra = ["_" for letter in self.palavra_correta]          # palavra que está sendo adivinhada 
        
        self.background = pyglet.resource.image("resource/background.png")
        
        self.cabeca = pyglet.resource.image("resource/cabeca.png")
        self.tronco = pyglet.resource.image("resource/tronco.png")
        self.braco1 = pyglet.resource.image("resource/braco1.png")
        self.braco2 = pyglet.resource.image("resource/braco2.png")
        self.perna1 = pyglet.resource.image("resource/perna1.png")
        self.perna2 = pyglet.resource.image("resource/perna2.png")
        
        self.parabens = pyglet.resource.image("resource/cowboy.png")
        
        self.palavra_label = None
        self.testado_label = None
        self.msg_label = None
        self.msg2_label = None
        
        self.__update_label()
             
    def __update_label(self):
        self.palavra_label = pyglet.text.Label(" ".join(self.palavra),
            font_name="Helvetica",
            font_size=41,
            x=window.width // 2 - 120,
            y=window.height // 2 - 160
        )
        
        self.testado_label = pyglet.text.Label(" ".join(list(self.testado)),
            font_name="Helvetica",
            font_size=37,
            color=(255, 46, 52, 255),
            x=window.width // 2 - 100,
            y=window.height // 2 - 250,
            anchor_x="center",
            anchor_y="center",
        )
        
        self.msg_label = pyglet.text.Label('PARABÉNS!  Você acertou.',
            font_name="Helvetica",
            font_size=20,
            x=window.width // 2 + 180,
            y=window.height // 2 + 160
        )
        
        self.msg2_label = pyglet.text.Label('Infelizmente você errou. Talvez na próxima.',
            font_name="Helvetica",
            font_size=18,
            x=window.width // 2 + 130,
            y=window.height // 2 - 252
        )
           
    def run(self):
        self.background.blit(0, 0)
        self.palavra_label.draw()
        self.testado_label.draw()
        
        if self.errado > 5:
            self.msg2_label.draw()

        if  ''.join(map(str, self.palavra)) == self.palavra_correta.upper():
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.parabens.blit(700, 470)
            self.msg_label.draw()
        
        if self.errado > 0:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.cabeca.blit(323, 375)
        
        if self.errado > 1:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.tronco.blit(303, 278)
        
        if self.errado > 2:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.braco1.blit(293, 284)
        
        if self.errado > 3:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.braco2.blit(405, 284)
        
        if self.errado > 4:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.perna1.blit(328, 233)
        
        if self.errado > 5:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.perna2.blit(363, 234)
        
        else:
            pass
        
    def press(self, chave):
        if self.errado <= 5:
            found = False
            for i in range(len(self.palavra_correta)):
                if self.palavra_correta[i] == chave:
                    self.palavra[i] = chave.upper()
                    found = True
                        
            if not found:
                if ''.join(map(str, self.palavra)) != self.palavra_correta.upper():
                    if chave not in self.testado:
                        self.testado.append(chave)
                    self.errado += 1
                
            self.__update_label()
        
with open('/Users/nrm/Documents/1_TI_programação/Python/Jogo_da_forca/resource/palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

p = choice(lista_de_palavras).upper()

game = Game(p)

@window.event
def on_draw():
    window.clear()
    game.run()
    
    
@window.event
def on_key_press(symbol, modifiers):
    if chr(symbol) in string.ascii_lowercase:
        game.press(chr(symbol))

if __name__ == "__main__":
    pyglet.app.run()