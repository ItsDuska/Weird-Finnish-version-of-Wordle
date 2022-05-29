import random
import pygame
pygame.init()
pygame.font.init()

def Random_sana():
    lista = []
    sanat =  open("SanatWord.txt","rb")
    Nimi_lista = sanat.read().decode("utf-8").split(" ")
    for kohta in Nimi_lista:
        lista.append(kohta) 
    sana = lista[random.randint(0,(len(lista)-1))]
    sanat.close()
    return sana
       
def lista_clear(lista):
    Tämä_rivi = ""
    for sus in range(5):
        Tämä_rivi += lista[sus]
    lista.clear()
    return Tämä_rivi

class Kirjaimet:
    def __init__(self,näyttö,oikea_sana):
        self.teksti_layer = []
        self.teksti_layer_pos = []
        self.lista = [] # lista
        self.listat = [] #listat
        self.näyttö = näyttö
        self.cord_x = 200
        self.cord_y = 25
        self.oikea_sana = oikea_sana
        self.vihreä_lista = []
        self.keltainen_lista = []
        self.oikein = False
        self.lines = []
        self.pyörii = 6
        self.YELLOW = (240,240,0)
        self.GREEN = (99,255,76)
        self.GRAY = (65,65,65)
        self.offset = 5
        self.rivi = 0
        self.väri_lista = []
        self.näppäin_väri_lista = []

        for Y in range(6):
            for X in range(5):
                self.kuutio = pygame.Rect(X*40+self.cord_x,self.cord_y+Y*60,30,50)
                self.lines.append(self.kuutio)
                self.väri_lista.append(self.GRAY)

    def piirrä_kuutiot(self):
        for indexi,kuutio in enumerate(self.lines):
            pygame.draw.rect(self.näyttö,self.väri_lista[indexi], kuutio)

    def Katso_nappi_ja_kirjoita(self,nappi):
        if nappi == 8 and len(self.lista) != 0:
            del self.lista[len(self.lista)-1]
        elif len(self.lista) < 5:
            näppäimet = {pygame.K_q:"Q", pygame.K_w:"W",pygame.K_e:"E",pygame.K_r:"R",pygame.K_t:"T",pygame.K_y:"Y"
            ,pygame.K_u:"U",pygame.K_i:"I",pygame.K_o:"O",pygame.K_p:"P",pygame.K_a:"A",pygame.K_s:"S",pygame.K_d:"D"
            ,pygame.K_f:"F",pygame.K_g:"G",pygame.K_h:"H",pygame.K_j:"J",pygame.K_k:"K",pygame.K_l:"L",246:"Ö",228:"Ä"
            ,pygame.K_z:"Z",pygame.K_x:"X",pygame.K_c:"C",pygame.K_v:"V",pygame.K_b:"B",pygame.K_n:"N",pygame.K_m:"M"}
            if nappi in näppäimet:
                painettu_nappi = näppäimet[nappi]
                self.lista.append(painettu_nappi)

    def piirrä_rivit(self):
        self.fontti = pygame.font.SysFont('Arial', 30)
        if len(self.teksti_layer) > 0:
            for x in range(len(self.teksti_layer)):
                self.näyttö.blit(self.teksti_layer[x],self.teksti_layer_pos[x])
        for kirjain in range(len(self.lista)):
            self.tekstijuttu = self.fontti.render(self.lista[kirjain], 1, (255,255,255))
            self.näyttö.blit(self.tekstijuttu,((kirjain*40)+self.cord_x+self.offset,self.cord_y+self.offset))

    def renderaa_värit(self,kohta,väri):
        if väri is not None:
            self.väri_lista[kohta+self.rivi*5] = väri
        self.tekstijuttu = self.fontti.render(self.lista[kohta], 1, (255,255,255)) 
        self.teksti_layer.append(self.tekstijuttu)
        self.teksti_layer_pos.append(((kohta*40)+self.cord_x+self.offset,self.cord_y+self.offset))
        
    def Tarkistus(self):
        for x in range(len(self.lista)):
            sana_määrä = self.oikea_sana.count(self.lista[x])
            vihreä_lista_sana_määrä = self.vihreä_lista.count(self.lista[x])
            keltainen_lista_sana_määrä = self.keltainen_lista.count(self.lista[x])
            if self.lista[x] == self.oikea_sana[x]:
                self.vihreä_lista.append(self.lista[x])
                self.renderaa_värit(x,self.GREEN)
            elif self.lista[x] in self.oikea_sana and self.lista[x] != self.oikea_sana[x]:
                if vihreä_lista_sana_määrä+keltainen_lista_sana_määrä < sana_määrä:
                    self.keltainen_lista.append(self.lista[x])
                    self.renderaa_värit(x,(self.YELLOW))
                else:
                    self.renderaa_värit(x,None)
            
            else:
                self.renderaa_värit(x,None)

        if len(self.vihreä_lista) == 5:
            self.pyörii=0
        self.vihreä_lista.clear()
        self.keltainen_lista.clear()
        self.cord_y += 60
        self.pyörii -= 1
        self.rivi += 1 
        
    def generate_laatikko(self):
        fontti = pygame.font.SysFont('Arial', 45)
        merkit = [["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L","Ö","Ä"],["Enter","Z","X","C","V","B","N","M","Del"]]
        self.näppäin_lista = pygame.sprite.Group()
        for lista_num,osa in enumerate(merkit): 
            for indexi,merkki in enumerate(osa):
                teksti = fontti.render(merkki, 1, (255,255,255))
                
                if lista_num == 0:
                    if indexi >= 8:
                        self.näppäin = Laatikot(105+indexi*40-20,400+lista_num*55,self.näyttö,teksti,merkki)
                    else:
                        self.näppäin = Laatikot(105+indexi*40,400+lista_num*55,self.näyttö,teksti,merkki)
                elif lista_num == 1:
                    self.näppäin = Laatikot(75+indexi*40,400+lista_num*55,self.näyttö,teksti,merkki)
                elif lista_num == 2 and indexi == 0:
                    self.näppäin = Laatikot(70+indexi*40,400+lista_num*55,self.näyttö,teksti,merkki)
                else:
                    self.näppäin = Laatikot(130+indexi*40,400+lista_num*55,self.näyttö,teksti,merkki)
                self.näppäin_lista.add(self.näppäin)

    def päivitä_näp(self):
        for indexi,kuutio in enumerate(self.näppäin_lista):
            pygame.draw.rect(self.näyttö,self.väri_lista[indexi], kuutio)
        self.näppäin_lista.draw(self.näyttö)

        
    def näpäytä_laatikkoa(self,pos):
        for laatikko in self.näppäin_lista:
            if laatikko.rect.collidepoint(pos):
                if laatikko.merkki == "Del" and len(self.lista) != 0:
                    del self.lista[len(self.lista)-1]

                elif laatikko.merkki == "Enter" and len(self.lista) == 5:
                    self.Tarkistus() 
                    self.listat.append(lista_clear(self.lista))

                if len(self.lista) < 5 and laatikko.merkki != "Del" and laatikko.merkki != "Enter":
                    self.lista.append(laatikko.merkki)

class Laatikot(pygame.sprite.Sprite):
    def __init__(self,x,y,näyttö,teksti,merkki):
        super().__init__()
        self.merkki = merkki
        self.x = x
        self.y = y
        self.image = teksti
        näyttö.blit(self.image,(x,y))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.kuutio = pygame.Rect(x,y,0,0)
        
        
        