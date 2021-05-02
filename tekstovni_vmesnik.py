import pygame as p 
import model

SIRINA = VISINA = 512
DIMENZIJA = 8   # Sahovnica je 8x8
VELIKOST_KVADRATA = VISINA // DIMENZIJA
MAX_FPS = 15   # Za animacije figur
SLIKE = {}


def nalozi_slike():
    figure = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
    for figura in figure:
        SLIKE[figura] = p.transform.scale(p.image.load('slike/' + figura + '.png'),
        (VELIKOST_KVADRATA, VELIKOST_KVADRATA)) 
        # Nalozimo slike za posamezno figuro in jim nastavimo velikost enako kot je velikost
        # kvadrata na sahovnici.


def main():
    p.init()
    zaslon = p.display.set_mode((SIRINA, VISINA))
    ura = p.time.Clock()
    zaslon.fill(p.Color('white'))
    stanje = model.StanjeIgre()
    print(stanje.plosca)
    nalozi_slike() # To naredimo samo enkrat
    izbrani_kvadrat = () # Na zacetku ni noben izbran
    igralec_klikne = []  

    deluje = True
    while deluje:
        for e in p.event.get():
            if e.type == p.QUIT:
                deluje = False
            elif e.type == p.MOUSEBUTTONDOWN:
                lokacija = p.mouse.get_pos() # (x,y) lokacija miske
                stolpec = lokacija[0] // VELIKOST_KVADRATA
                vrstica = lokacija[1] // VELIKOST_KVADRATA

        narisi_stanje_igre(zaslon, stanje)
        ura.tick(MAX_FPS)
        p.display.flip()




# Funkcija je odgovorna za vso grafiko skozi stanje igre
def narisi_stanje_igre(zaslon, stanje):
    narisi_plosco(zaslon) # Narisemo kvadrate na plosco
    narisi_figure(zaslon, stanje.plosca) # Narisemo figure na kvadrate


# Narisemo kvadrate
def narisi_plosco(zaslon):
    barve = [p.Color('white'), p.Color('gray')]
    for vrstica in range(DIMENZIJA):
        for stolpec in range(DIMENZIJA):
            barva = barve[((vrstica + stolpec) % 2)] 
            p.draw.rect(zaslon, barva, p.Rect(stolpec * VELIKOST_KVADRATA,
            vrstica * VELIKOST_KVADRATA, VELIKOST_KVADRATA, VELIKOST_KVADRATA))



# Narisemo figure, glede na plosco
def narisi_figure(zaslon, plosca):
    for vrstica in range(DIMENZIJA):
        for stolpec in range(DIMENZIJA):
            figura = plosca[vrstica][stolpec]
            if figura != '--': # Torej ni prazen kvadratek
                zaslon.blit(SLIKE[figura], p.Rect(stolpec * VELIKOST_KVADRATA,
                vrstica * VELIKOST_KVADRATA, VELIKOST_KVADRATA, VELIKOST_KVADRATA))
                #blit uporabimo da lahko gre slika preko druge slike



# Da zazenemo program, samo go se poklice, ne pa tudi ko se importa
if __name__ == '__main__':
    main()