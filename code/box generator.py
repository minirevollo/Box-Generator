# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:59:30 2018

@author: Andreas Reheis
member of the erfindergarden
"""

from random import randint 
from tkinter import *
from time import *
import os #für die Vorschau



class BOX:
    
    def __init__(self, breite, hoehe, tiefe, material, zahnbreite):
        ###Initialisiert die Box.###
        self.svg = 0 
        self.name = "Box_Version_1.svg"
        self.breite = breite
        self.hoehe = hoehe
        self.tiefe = tiefe
        self.material = material
        self.zahnbreite = zahnbreite
        #Berechnung der Reste der Breite br
        self.bzm = round((self.breite - (2 * self.material)) / (self.zahnbreite * 2))
        self.br = (self.breite - (self.bzm * self.zahnbreite * 2)) / 2
        #Berechnung der Reste der Hoehe hr
        self.hzm = round((self.hoehe - (2 * self.material)) / (self.zahnbreite * 2))
        self.hr = (self.hoehe - (self.hzm * self.zahnbreite * 2)) / 2 
        #Berechnung der Reste der Tiefe tr
        self.tzm = round((self.tiefe - (2 * self.material)) / (self.zahnbreite * 2)) - 1
        self.tr = (self.tiefe - (self.tzm * self.zahnbreite * 2)) / 2
        print(self.tr)
        #Eigenschaften der SVG
        self.svg_breite = self.breite + self.tiefe + self.tiefe + 10
        if self.hoehe > self.breite:
           self.svg_hoehe = self.hoehe
        else:
            self.svg_hoehe = self.breite
        self.dokumenten_anfang = "<?xml version=\"1.1\" encoding=\"UTF-8\"?>" + "\n"\
                                   + "<svg" + "\n"\
                                   + "xmlns = \"http://www.w3.org/2000/svg\"" + "\n" 
        self.dokumenten_breite = "width = \"" + str(self.svg_breite) + "mm" + "\""
        self.dokumenten_hoehe = "height = \"" + str(self.svg_hoehe) + "mm" + "\""
        self.dokumenten_viewbox = "viewBox= \"0 0 " + str(self.svg_breite) + " " + str(self.svg_hoehe) + "\">\n"
        self.pfad_nr = 0
        self.dokumenten_ende = "</svg>"    
    
    def schreiben_einleitung(self):
        ###Erzeugt eine neue Datei und schreibt die Dokumenteneinstellungen.###
        
       self.svg = open(self.name, "w")
       self.svg.write(self.dokumenten_anfang + "\n")
       self.svg.write(self.dokumenten_breite + "\n")
       self.svg.write(self.dokumenten_hoehe + "\n")
       self.svg.write(self.dokumenten_viewbox + "\n")
       self.svg.close()
    
    def front_erstellen(self):
        ###Erstellt eine Front und fügt sie der Datei hinzu.###
        x = 0
        y = 0
        ###Öffnen der Datei.###
        self.svg = open(self.name, "a")
        ###Position x wird auf 0 gesetzt. 
        self.pfad_anfang()
        self.svg.write(" d=\"M " + str(x) + "," + str(y) + " ")
        #### 1. Seite.
        x = x + self.br
        self.svg.write(str(x) + "," + str(y) + " ")    
        for item in range(self.bzm):
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
        x = x + self.br
        self.svg.write(str(x) + "," + str(y) + " ")    
        ### 2. Seite.
        y += self.hr 
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.hzm):
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y += self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 3. Seite.
        x -= self.br
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.bzm):
            x -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite /2
            self.svg.write(str(x) + "," + str(y) + " ")
        x -= self.br
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 4. Seite.
        y -= self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.hzm):
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y -= self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        ### Pfad schließen
        self.pfad_ende()
        self.svg.close()
        
    def seite_erstellen(self):
        ###Erstellt eine Seite und fügt sie der Datei hinzu.###
        
        x = self.breite + 5 + self.material
        y = 0
        ###Öffnen der Datei.###
        self.svg = open(self.name, "a")
        self.pfad_anfang()
        self.svg.write(" d=\"M " + str(x) + "," + str(y) + " ")
        #### 1. Seite.
        x = x + self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")    
        for item in range(self.tzm):
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
        x = x + self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")    
        ### 2. Seite.
        y += self.hr 
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.hzm):
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y += self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 3. Seite.
        x -= self.tr - self.material 
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.tzm):
            x -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite /2
            self.svg.write(str(x) + "," + str(y) + " ")
        x -= self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 4. Seite.
        y -= self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.hzm):
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y -= self.hr
        self.svg.write(str(x) + "," + str(y) + " ")
        ### Pfad schließen
        self.pfad_ende()
        self.svg.close()

    def deckel_erstellen(self):
        ###Erstellt einen Deckel und fügt ihn der Datei hinzu.###
        
        x = self.breite + 5 + self.tiefe + 5 + self.material
        y = self.material
        ###Öffnen der Datei.###
        self.svg = open(self.name, "a")
        self.pfad_anfang()
        self.svg.write(" d=\"M " + str(x) + "," + str(y) + " ")
        #### 1. Seite.
        x = x + self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")    
        for item in range(self.tzm):
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x += (self.zahnbreite / 2)
            self.svg.write(str(x) + "," + str(y) + " ")
        x = x + self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")    
        ### 2. Seite.
        y += self.br - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.bzm):
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y += self.br - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 3. Seite.
        x -= self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.tzm):
            x -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            y += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.zahnbreite /2
            self.svg.write(str(x) + "," + str(y) + " ")
        x -= self.tr - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        ### 4. Seite.
        y -= self.br - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        for item in range(self.bzm):
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
            x -= self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite
            self.svg.write(str(x) + "," + str(y) + " ")
            x += self.material
            self.svg.write(str(x) + "," + str(y) + " ")
            y -= self.zahnbreite / 2
            self.svg.write(str(x) + "," + str(y) + " ")
        y -= self.br - self.material
        self.svg.write(str(x) + "," + str(y) + " ")
        ### Pfad schließen
        self.pfad_ende()
        self.svg.close()

    def pfad_anfang(self):
        ###Schreibt den Anfang eines Pfades mit allen seinen Eigenschaften###
        
        self.svg.write("<path\n\t style=\"fill:none;stroke:#000000;stroke-width:0.50px;stroke-linecap:round;stroke-linejoin:miter;stroke-opacity:1\"\n")
        
         
    def pfad_ende(self):
        ###Schreibt das Ende des Pfades.###
        
        pfad_id = "pfad_" + str(self.pfad_nr)
        self.svg.write("\"" + "\n\tid=\"" + pfad_id  + "\" \n\tinkscape:connector-curvature=\"0\"\n />\n" + "\n")
        self.pfad_nr += 1
        
    def schreiben_ende(self):
        ###Schreibt das Ende der Datei.###
        
       self.svg = open(self.name, "a")
       self.svg.write(self.dokumenten_ende)
       self.svg.close()
       
    def rand_erstellen(self):
        ###Erstellt die Umrandung des Puzzles.###
        
        self.svg = open(self.name, "a")
        self.svg.write("<rect" + "\n"\
                        + "style=\"fill:none;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linejoin:round;stroke-miterlimit:4;"\
                        + "stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1\"" + "\n"\
                        + "id=\"Umrandung\"" + "\n"\
                        + "width=\"" + str(self.breite) + "\"" + "\n"\
                        + "height=\"" + str(self.hoehe) + "\"" + "\n"\
                        + "x=\"0\"" + "\n"\
                        + "y=\"0\"" + "\n"\
                        + "rx=\"5\"" + "\n"\
                        + "ry=\"5\" />" + "\n")
        self.svg.close()

    def branding_erstellen(self):
            ###Erstellt das Branding auf der Box.###
            
            self.svg = open(self.name, "a")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-anchor:middle;font-size:15px;font-family:Consolas;writing-mode:lr-tb;fill:#ff0000;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.svg_breite / 2) +"\"" + "\n"\
                            + "y=\"" + str(self.svg_hoehe / 3) +"\"" + "\n"\
                            + "id=\"Branding\"" + "\n"\
                            + ">Box Generator by mini revollo</text>" + "\n")
            self.svg.close()
    
    def beschriftung_erstellen(self):
            ###Erstellt die Beschriftung für die Bauteile auf der Box.###
            
            self.svg = open(self.name, "a")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-anchor:middle;font-size:8px;font-family:Consolas;writing-mode:lr-tb;fill:#969696;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.breite / 2) +"\"" + "\n"\
                            + "y=\"" + str(self.svg_hoehe / 2) +"\"" + "\n"\
                            + "id=\"Front\"" + "\n"\
                            + ">vorne/hinten</text>" + "\n")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-anchor:middle;font-size:8px;font-family:Consolas;writing-mode:lr-tb;fill:#969696;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.breite + (self.tiefe/2)) +"\"" + "\n"\
                            + "y=\"" + str(self.svg_hoehe / 2) +"\"" + "\n"\
                            + "id=\"Seite\"" + "\n"\
                            + ">links/rechts</text>" + "\n")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-anchor:middle;font-size:8px;font-family:Consolas;writing-mode:lr-tb;fill:#969696;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.breite + self.tiefe * 1.5) +"\"" + "\n"\
                            + "y=\"" + str(self.svg_hoehe / 2) +"\"" + "\n"\
                            + "id=\"Deckl\"" + "\n"\
                            + ">oben/unten</text>" + "\n")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-anchor:middle;font-size:8px;font-family:Consolas;writing-mode:lr-tb;fill:#969696;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.breite / 2) +"\"" + "\n"\
                            + "y=\"" + str(self.svg_hoehe / 3 * 2) +"\"" + "\n"\
                            + "id=\"Materialbeschreibung\"" + "\n"\
                            + ">Material: " + str(self.material) + " mm</text>" + "\n")
            self.svg.close()


    def gruppe_anfang(self):
        ###Erstellt den Anfang einer Gruppe.###
        
        self.svg = open(self.name, "a")
        self.svg.write("<g \n\t id = \"Box\" >")
        self.svg.close()
        
    def gruppe_ende(self):
        ###Erstellt das Ende einer Gruppe.###
        
        self.svg = open(self.name, "a")
        self.svg.write("\n</g>")
        self.svg.close()
        
    def anzeigen(self):
        ###Öffnet über das Betriebssystem den hinterlegeten SVG-Viewer.###

        os.startfile(self.name)
        
class FENSTER:
    ###Stellt alle Einstellungen für die erste Ansicht zur Verfügung.###
   
    def  __init__(self):
        ###Iniziert das Fenster.###
        
        print("Fenster  initiert")
        self.breite = 300
        self.hoehe = 400
        self.anzeige = Frame(root, bg = "black")
        self.anzeige.place(x = 0, y = 0, width = self.breite, height = self.hoehe)
        self.text_name = Label(text = "Box Generator", font = ("Consolas", 20), fg = "green", bg = "black", anchor = "center")
        self.text_name.place(x = 0, y = 20, width = self.breite, height = 20)
        self.text_breite = Label(text = "Breite: ", fg = "green", bg = "black", anchor = "w")
        self.text_hoehe = Label(text = "Höhe: ", fg = "green", bg = "black", anchor = "w")
        self.text_tiefe = Label(text = "Tiefe: ", fg = "green", bg = "black", anchor = "w")
        self.text_material = Label(text = "Material: ", fg = "green", bg = "black", anchor = "w")
        self.text_zahnbreite = Label(text = "Zahnbreite: ", fg = "green", bg = "black", anchor = "w")
        self.text_breite.place(x = 40, y = 60, width = 60, height = 20)
        self.text_hoehe.place(x = 40, y = 80, width = 60, height = 20)
        self.text_tiefe.place(x = 40, y = 100, width = 120, height = 20)
        self.text_material.place(x = 40, y = 120, width = 60, height = 20)
        self.text_zahnbreite.place(x = 40, y = 140, width = 120, height = 20)
        self.input_breite = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_hoehe = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_tiefe = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_material = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_zahnbreite = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_breite.insert(0, 100)
        self.input_hoehe.insert(0, 200)        
        self.input_tiefe.insert(0, 300)
        self.input_material.insert(0, 3.6)        
        self.input_zahnbreite.insert(0, 15)
        self.input_breite.place(x = 160, y = 60)
        self.input_hoehe.place(x = 160, y = 80)
        self.input_tiefe.place(x = 160, y = 100)  
        self.input_material.place(x = 160, y = 120)
        self.input_zahnbreite.place(x = 160, y = 140) 
        self.bt_erstellen = Button(self.anzeige, text="Box erstellen", command = box_erstellen)
        self.bt_erstellen.place(x = 100, y = 180, width = 100, height = 20)
        self.bt_beenden = Button(self.anzeige, text="beenden" , width=25, command=root.destroy)
        self.bt_beenden.place(x =100, y = 200, width = 100, height = 20)
        self.text_info = Label(text = "  by \n mini revollo \n  member of the \n erfindergarden", font = "Consolas", fg = "green", bg = "black", anchor = "center")
        self.text_info.place(x = 0, y = 240, width = self.breite, height = 80)
        self.text_ausgabe = Label(self.anzeige, text = "die Box wurde gespeichert ", font = "Consolas", fg = "green", bg = "black", anchor = "center")
        
    def bestätigung(self, breite, hoehe, tiefe):
        ###Bestätigung der Boxspeicherung.###
        
        ausgabetext = "Die Box  wurde mit \n" + str(breite) + " x " + str(hoehe) + " x " + str(tiefe) + " \n  erstellt"
        self.text_ausgabe = Label(text = ausgabetext, font = "Consolas", fg = "green", bg = "black", anchor = "center")    
        self.text_ausgabe.place(x = 0, y = 220, width = self.breite, height = 80) 
        
        
def box_erstellen():
    ###.Erstellt die Box und speichert sie ab.###
    box = BOX(int(fenster.input_breite.get()),int(fenster.input_hoehe.get()),int(fenster.input_tiefe.get()),float(fenster.input_material.get()), int(fenster.input_zahnbreite.get()))
    box.schreiben_einleitung()
    box.gruppe_anfang()
    box.front_erstellen()
    box.seite_erstellen()
    box.deckel_erstellen()
    box.gruppe_ende()
    box.branding_erstellen()
    box.beschriftung_erstellen()
    box.schreiben_ende()
    box.anzeigen()
    fenster.bestätigung(box.breite, box.hoehe, box.tiefe)
                                                   
""" Setup """

root = Tk()         #ein Fenster erstellen
root.geometry("300x400")          #Größe zuordnen
root.title("           Box Generator by mini revollo            ")
 #Fenster mit einem Titel versehen 
   
###Hier läuft das Programm ab.###    
fenster = FENSTER()

#root.after(0, box_erstellen)    
root.mainloop()
 
       
        