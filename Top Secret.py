#!/usr/bin/python
# Programme Python realise par Jean Feydy, dans le cadre du TPE de 1ere S:
# "pourquoi la lumiere est-elle attiree par les trous noirs?"
# Groupe : Aaron Demri, Nicolas Anne, Cassandre ????, Jean Feydy
# 1ere S 7, Lycee Marcelin Berthelot

# Note : En programmation, on designe par le terme "Widget" tout ce qui est affichable a l'ecran
#	 (zones de texte, boutons, nombre LCD, fenetres, etc...), en opposition avec les nombres, chaines de caracteres et autres,
#	 plus "abstraits"

# Note 2 : les caracteres accentues ne sont pas presents pour des raisons de compatibilite :
# 	 En programmation, il est generalement deconseille d'inclure des caracteres non ASCII (anglais)

# Ce programme a pour but de "simuler" un trou noir, dont on peut, par l'intermediaire de differents
# Widgets, modifier la masse


try:
	import psyco
	psyco.full()
except:
	pass


import sys, math		# on importe 'math' pour utiliser les fonction racine et hypoth
from PyQt4 import QtGui, QtCore	# on importe le module 'PyQt4', un toolkit graphique


def pui(p, nbre = 10):
	"Fonction 'puissance', les arguments sont la puissance et le nombre de base (par defaut 10))"
	if (p < 0):			# si la puissance < 0, on renvoit 1 / pui(puissance, nbre)
		return 1.0 / pui(-1 * p, nbre)
	ret = 1
	while p > 0:
		ret *= nbre
		p -= 1
	return ret


class MonAffichage(QtGui.QWidget):
	"Classe representant l'image du trou noir + son rayon (l'affichage)"
	def __init__(self):
		"Constructeur de la classe"
		QtGui.QWidget.__init__(self)	# on initialise le Widget
		self.setMinimumSize(500, 500)	# sa taille minimale est un carre de 500*500
		self.MassesSol = 0		# on initialise les variables a 0 ...
		self.Echelle = 250		# sauf l'echelle, a 250 m / pixel
		self.CursX = 0
		self.CursY = 0
	
	def paintEvent(self, event):
		"fonction appelee par la fenetre, qui repaint la surface de l'image (on l'actualise)"
		
		# note : le painter represente la main du dessinateur		
		painter = QtGui.QPainter(self)		# on cree le painter, qui repeindra notre image
		pen = QtGui.QPen()			# on cree le stylo
		pen.setColor (QtGui.QColor(0, 0, 255))	# le stylo est bleu...
		pen.setWidth(2)				# ...de taille 2 pixels...
		pen.setStyle(QtCore.Qt.DashLine)	# ...et ecrit en pointille
		painter.setPen(pen)			# la main prend le stylo
		
		# le coin de l'ellipse haut/gauche, tel que l'ellipse soit au centre de l'image
		self.CoinX = (self.width() / 2) - (self.MassesSol *2 * 2952 / self.Echelle) / 2
		self.CoinY = (self.height() / 2) - (self.MassesSol * 2 * 2952 / self.Echelle) / 2
		
		# la main dessine l'ellipse (le cercle dans notre cas, car la largeur = longueur),
		# avec le stylo si le cercle ne depasse pas les limites de l'ecran
		if (self.MassesSol / 100) * 2 * 2952 / (self.Echelle / 100) <\
		self.width() + self.height() / 2:
			painter.drawEllipse ( self.CoinX, self.CoinY, self.MassesSol* 2 * 2952 / self.Echelle, self.MassesSol * 2 *2952 / self.Echelle);
		
		# on change le stylo
		pen.setStyle(QtCore.Qt.NoPen)			# maintenant, il n'ecrit plus...	
		brush = QtGui.QBrush(QtCore.Qt.SolidPattern)	# mais il remplit la surface qu'il
								# delimite...
		brush.setColor(QtCore.Qt.black)			# ...en noir
		painter.setPen(pen)				# la main prend le nouveau stylo (seau)
		painter.setBrush(brush)			#la main prend les caracs. du nouveau stylo

		
		# la main trace un disque (plein) de diametre 10 km (arbitraire) au milieu de l'image
		painter.drawEllipse ((self.width() / 2) - 10000 / self.Echelle / 2 + 1, (self.height() / 2) - 10000 / self.Echelle / 2 + 1,\
		 10000 / self.Echelle + 1, 10000 / self.Echelle + 1)
		
		# on redetermine le centre de l'image
		self.CentreX = self.width()/2
		self.CentreY = self.height()/2
		
	def mouseReleaseEvent(self, event):
		"Fonction appelee lors d'un clic de souris sur l'image"
		self.CursX = event.x()				# on inscrit la position de la souris
		self.CursY = event.y()				# dans des variables
		self.emit(QtCore.SIGNAL('clicSouris()'))	# on emet le signal "clicSouris"


class MaFenetre(QtGui.QWidget):
	"Classe fenetre. C'est elle qui gere tout le programme"
	
	def clicSurAffichage(self):
		"fonction appellee lors du clic sur l'image"
		# on clacule la distance en metres (virtuels) entre le curseur et le centre du trou
		# noir (= distance en pixel * echelle en m / pixel)
		distanceMetre = int(math.hypot((self.Affichage_W.CursX - self.Affichage_W.CentreX),
		(self.Affichage_W.CursY - self.Affichage_W.CentreY)) * self.Echelle_SB.value())
		
		# on actualise le chiffre LCD de la distance curseur/centre du trou noir
		self.Distance_LCD.display(distanceMetre)
		
		# on actualise la vitesse de liberation du curseur
		# v = racine( (2 * G * Mtrou_noir) / Distance)
		self.VitAct_LCD.display(int(math.sqrt((2 * 6.67*pui(-11) * self.Masse_Slider.value() * pui(self.Puissance_SB.value())* 1.989 * pui(30))/(distanceMetre))))
	
	def chgtMasse(self, masse):
		"fonction appelee lors d'un mouvement du slider de masse"
		puiss =  pui(self.Puissance_SB.value())
		self.Masse_LCD.display(int(masse))		# on actualise le nombre LCD des masses
		self.Rayon_LCD.display(int(masse  * puiss * 2952))	# on actualise le nombre LCD du rayon
		self.Affichage_W.MassesSol = int(masse  * puiss)# on actualise la valeur interne de 
								# l'image la masse de
		self.Affichage_W.Echelle = self.Echelle_SB.value()	# on actualise l'echelle
		self.Affichage_W.repaint()		# et enfin, on repaint l'image
	
	def chgtEchelle(self, echelle):
		"fonction appellee lors d'un changement d'echelle"
		self.chgtMasse(self.Masse_Slider.value())	# on reactualise l'image

	def chgtPui(self, puiss):
		"fonction appellee lors d'un changement de puissance de 10 de la masse"
		self.chgtMasse(self.Masse_Slider.value())	# on reactualise l'image
		
	def __init__(self):
		"Constructeur de la fenetre"
		QtGui.QWidget.__init__(self)			# on initialise le Widget
		self.setWindowTitle("Simulateur de trou noir")	# on donne un titre a la fenetre
		
		# On cree tout les Widgets
		# note: QLabel = texte, QSlider = slider, QLCDNumber = nombre LCD,
		# QSpinBox = pour choisir un chiffre
		self.Affichage_W = MonAffichage()
		self.Masse_Lbl = QtGui.QLabel("Masse du trou noir :")
		self.Masse_Slider = QtGui.QSlider(QtCore.Qt.Horizontal)
		self.Masse_LCD = QtGui.QLCDNumber(10)
		self.Masse3_Lbl = QtGui.QLabel("* 10 ^ ")
		self.Puissance_SB = QtGui.QSpinBox()
		self.Masse2_Lbl = QtGui.QLabel("masses solaires")
		self.VitAct_LCD = QtGui.QLCDNumber(15)
		self.VitAct_Lbl = QtGui.QLabel("Vitesse de liberation actuelle (m / s)")
		self.Rayon_LCD = QtGui.QLCDNumber(12)
		self.Rayon_Lbl = QtGui.QLabel("Rayon de l'horizon du trou noir (m)")
		self.Distance_LCD = QtGui.QLCDNumber(12)
		self.Distance_Lbl = QtGui.QLabel("Distance du centre du trou noir au curseur (m)")
		self.Echelle_Lbl = QtGui.QLabel("Echelle : 1 pixel = ")
		self.Echelle2_Lbl = QtGui.QLabel("m")
		self.Echelle_SB = QtGui.QSpinBox()
		
		self.Echelle_SB.setRange(100, 10000000)	# l'echelle va de 100 a 2000 m / pixel
		self.Echelle_SB.setValue(250)		# par defaut, l'echelle est de 250 m / pixel
		self.Puissance_SB.setRange(0, 3)	# la puissance va de 0 a 9
		self.Puissance_SB.setValue(0)		# par defaut, la puissance est de 0

		# On met un "joli" style au nombres LCD
		self.Masse_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
		self.VitAct_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
		self.Rayon_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
		self.Distance_LCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
		
	
		# on cree les layouts (des conteneurs de Widgets, permettants de les organiser)
		self.layout_principal = QtGui.QVBoxLayout()
		self.layout_masse = QtGui.QHBoxLayout()
		self.layout_Rayon = QtGui.QHBoxLayout()
		self.layout_3 = QtGui.QHBoxLayout()
		
		# On ajoute les Widgets aux layouts ("mise en page" de la fenetre)
		self.layout_principal.addWidget(self.Affichage_W)
		
		self.layout_masse.addWidget(self.Masse_Lbl)
		self.layout_masse.addWidget(self.Masse_Slider)
		self.layout_masse.addWidget(self.Masse_LCD)
		self.layout_masse.addWidget(self.Masse3_Lbl)
		self.layout_masse.addWidget(self.Puissance_SB)
		self.layout_masse.addWidget(self.Masse2_Lbl)
		
		
		self.layout_Rayon.addWidget(self.Rayon_Lbl)
		self.layout_Rayon.addWidget(self.Rayon_LCD)		
		self.layout_Rayon.addWidget(self.Echelle_Lbl)
		self.layout_Rayon.addWidget(self.Echelle_SB)
		self.layout_Rayon.addWidget(self.Echelle2_Lbl)
		
		self.layout_3.addWidget(self.VitAct_Lbl)
		self.layout_3.addWidget(self.VitAct_LCD)
		self.layout_3.addWidget(self.Distance_Lbl)
		self.layout_3.addWidget(self.Distance_LCD)
		
		self.layout_principal.addLayout(self.layout_masse)
		self.layout_principal.addLayout(self.layout_Rayon)
		self.layout_principal.addLayout(self.layout_3)
		
		self.setLayout(self.layout_principal)	# on assigne le layout principal a la fenetre
		
		# on connecte :
		# un mouvement du slider a une actualisation de la fenetre (fonction 'chgtMasse')
		self.connect(self.Masse_Slider, QtCore.SIGNAL('sliderMoved(int)'), self.chgtMasse)
		
		# un changement d'echelle a une actualisation de la fenetre (fonction 'chgtEchelle')
		self.connect(self.Echelle_SB, QtCore.SIGNAL('valueChanged(int)'), self.chgtEchelle)
		
		# un changement de puissance a une actualisation de la fenetre (fonction 'chgtPui')
		self.connect(self.Puissance_SB, QtCore.SIGNAL('valueChanged(int)'), self.chgtPui)
		
		#un clic sur l'image a une actualisation de les nombres LCD(fonction 'clicSurAffichage')
		self.connect(self.Affichage_W, QtCore.SIGNAL('clicSouris()'), self.clicSurAffichage)
		
	
#	SCRIPT (tout le code precedent etait preliminaire) :

app = QtGui.QApplication(sys.argv)	# on lance l'application
fenetre = MaFenetre()			# on cree la fenetre
fenetre.show()				# on l'active
sys.exit(app.exec_())			# quand la fenetre est fermee, on ferme l'application