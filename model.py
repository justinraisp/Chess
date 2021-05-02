class StanjeIgre():

    def __init__(self):
        #Plosca je 8x8 2d seznam, vsak element lista ima dve crki. 
        #Prva crka elementa predstavlja barvo figure, drugi element pa 
        #katera figura je. '--' predstavlja prazno mesto brez figur.
        self.plosca = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.beli_na_potezi = True
        self.zapisnik_potez = []
        
