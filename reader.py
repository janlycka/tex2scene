# Fingeruebung, Jan Lycka, S7481099, Matnr. 7066140
import spacy
nlp = spacy.load("en_core_web_sm")

# Klasse fuer FlaggenElement 2_5
class FlagElementO2_5:
    def __init__(self, flagValue, prepositon):
        self.flagValue = flagValue
        self.children = [prepositon]

# Klasse fuer FlaggenArray Aufgabe 2_5
class FlagArray2_5:
    def __init__(self):
        self.contents = []

    # wenn wir schon ein id einmal gezaehlt haben, ignoriere es, sonst leg's an
    def appendOrsubAppend(self, link, prepositon):
        if self.contents == []:
            self.contents.append(FlagElementO2_5(link, prepositon));
        else:
            entered = 0
            i = 0
            for flagType in self.contents:
                if flagType.flagValue == link:
                    if prepositon not in flagType.children:
                        self.contents[i].children.append(prepositon)
                    entered = 1
                    break
                i+=1
            if entered == 0:
                self.contents.append(FlagElementO2_5(link, prepositon));

# Klasse fuer FlaggenElement
class FlagElement:
    def __init__(self, flagValue):
        self.flagValue = flagValue
        self.repetitions = 1

# Klasse fuer FlaggenArray
class FlagArray:
    def __init__(self):
        self.contents = []

    # wenn es in diesem Chapter eine derlei Fragge bereits gibt, count++, sonst leg es an
    def appendOrRaiseByOne(self, entry):
        if self.contents == []:
            self.contents.append(FlagElement(entry));
        else:
            entered = 0
            i = 0
            for flagType in self.contents:
                if flagType.flagValue == entry:
                    self.contents[i].repetitions+=1
                    entered = 1
                    break
                i+=1
            if entered == 0:
                self.contents.append(FlagElement(entry));

# Klasse fuer Flaggen
class Flags:
    def __init__(self):
        self.pos_ = FlagArray()
        #self.tag_ = FlagArray()
        #self.dep_ = FlagArray()
        #self.shape_ = FlagArray()
        #self.is_alpha = FlagArray()
        #self.is_stop = FlagArray()

# Meine Klasse zum Speichern einer Datei, ich benenne es Chapter
class Chapter:
    def __init__(self, text, file):
        # Aufgabe 2.2.iii - lasse spacy sein Magic machen, gewinne 'Noun phrases' und 'Verbs'
        doc = nlp(text)
        self.file = file
        self.text = text
        self.words = text.split();
        self.nouns = [chunk.text for chunk in doc.noun_chunks];
        # print(str(len(self.nouns)) + ' nouns')
        self.verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        # print(str(len(self.verbs)) + ' verbs')

        # allgemeine beflagung der Woerter im Chapter
        self.flags = Flags();
        # Frequenz der Tags messen
        for token in doc:
            #print('x'+token.pos_+'x')
            self.flags.pos_.appendOrRaiseByOne(token.pos_)
            globalPos.appendOrRaiseByOne(token.pos_)

            #count the verb values
            if token.pos_ == "VERB":
                globalVerbs.appendOrRaiseByOne(token.text)
            #self.flags.tag_.appendOrRaiseByOne(token.tag_)
            #self.flags.dep_.appendOrRaiseByOne(token.dep_)
            #self.flags.shape_.appendOrRaiseByOne(token.shape_)
            #self.flags.is_alpha.appendOrRaiseByOne(token.is_alpha)
            #self.flags.is_stop.appendOrRaiseByOne(token.is_stop)

class MyLink:
    def __init__(self, id, trigger):
        # save id and text
        self.trigger = trigger
        self.id = id

class SpatialSignal:
    def __init__(self, id, text):
        # save id and text
        self.id = id
        self.text = text

# Behaerlter fuer Spacial Signals
globalSpatialSignals = []
globalLinks = []

def get_my_key(obj):
    return obj[1]

def fst(obj):
    return obj[0]

def snd(obj):
    return obj[1]

# Globaler Storage for PoS - also nicht per Datei sondern insgesamt
globalPos = FlagArray()
# Globaler Storage for [SpatialEntities, Places, Motions, Signals, QsLinks, OLinks]
globalSPMSQO = FlagArray()
globalQSLINKs = FlagArray()
globalSentences = FlagArray()
globalVerbs = FlagArray()

globalMotions = [];

# benoetigt zum Gewinnen des QLINKs Attributenwertes
import json

# daten einlesen, parsen (xml) und je in array speichern
import os
src = 'text2scene\\Training'
result = 'result.txt'
print('Reading XML Files in: ' + os.getcwd() + '\\' + src)

# hole rekursiv all die xml Dateien
filenames = []
filescount = 0;
from pathlib import Path
currentPath = Path(src)

for file in currentPath.glob('**/*.xml'):
     filenames.append(file)

filescount = len(filenames)
print(str(filescount) + ' XML files found')

# lese und parse alle Dateien um individuelle Texte zu gewinnen
chapters = [];
masterText = ''
import xml.etree.ElementTree as ET

ind = 1;
for file in filenames:
#for file in [filenames[0], filenames[1]]:
    root = ET.parse(file).getroot()
    #extrahiere den Inhalt aus dem Tag TEXT
    for item in root.findall('TEXT'):
        print(str(ind) + ' / ' + str(filescount) + ' / 1    ', end='\r')
        ind+=1
        # print(item.text)
        masterText += ' ' + item.text
        #count the sentences
        sentences = item.text.split('.')
        for sentence in sentences:
            wordsInSen = sentence.split(' ')
            globalSentences.appendOrRaiseByOne(str(len(wordsInSen)))
        # erzeuge ein Kapitel
        chapters.append(Chapter(item.text, file))
    #extrahiere den Inhalt aus dem Koerper des Tags TAGS
    #ind = 1;
    for item in root.findall('TAGS/*'):
        #print(str(ind) + ' / ' + str(filescount) + ' / 2    ', end='\r')

        # anazahle von S,P,M,S,Q,O
        globalSPMSQO.appendOrRaiseByOne(item.tag)

        # Anzahl an jeweilige QSLINKs arten ermittlen
        if item.tag == 'QSLINK':
            #print(item.attrib['relType'])
            #relType = str(json.loads(str(item.attrib))['relType'])
            globalQSLINKs.appendOrRaiseByOne(item.attrib['relType'])

            if len(item.attrib['trigger'])>0:
                globalLinks.append(MyLink(item.attrib['id'], item.attrib['trigger']))

        if item.tag == 'OLINK' and len(item.attrib['trigger'])>0:
            globalLinks.append(MyLink(item.attrib['id'], item.attrib['trigger']))

        if item.tag == 'SPATIAL_SIGNAL':
            globalSpatialSignals.append(SpatialSignal(item.attrib['id'], item.attrib['text']))

        if item.tag == 'MOTION':
            globalMotions.append(item.attrib['text'])

        #ind+=1
        #print(item.tag)

# gewinne einzelne woerter
allWords = masterText.split()
print(str(len(allWords)) + ' words in total')

#output global PoS
print('\n\n\n\n\n\n\n\n2.3.i \n PoS-Tags , frequency\n')
for pos in globalPos.contents:
    print( str(pos.flagValue) + ': ' + str(pos.repetitions) + ', ')




print('\n\n\n\n\n\n\n\n2.3.ii - wie viele gibt es jeweils [SpatialEntities, Places, Motions, Signals, QsLinks, OLinks]n')
#output globalSPMSQO
print('\n\nglobalSPMSQO, #\n')
for entry in globalSPMSQO.contents:
    print( str(entry.flagValue) + ': ' + str(entry.repetitions) + ', ')




print('\n\n\n\n\n\n\n\n2.3.iii - QsLinktypes, frequency\n')
#output globalSPMSQO
print('\n\nglobalQSLINKs, #\n')
for entry in globalQSLINKs.contents:
    print( str(entry.flagValue) + ': ' + str(entry.repetitions) + ', ')



import matplotlib.pyplot as plt
import numpy as np

#2.4 erzeuge Grafik: Satzlaenge
lst = [];
for sentence in globalSentences.contents:
    lst.append((int(sentence.flagValue),int(sentence.repetitions)))
    
lst.sort(key=fst)
#print(lst)#
xAxis = [];
yAxis = [];
for sentence in lst:
    xAxis.append(fst(sentence))
    yAxis.append(snd(sentence))

print('\n\n\n\n\n\n\n\n2.3.iv - Sentences\' length, Sentences\' frequency\n')

b = (xAxis,yAxis)

plt.bar(*b)

plt.ylabel('Haeufigkeit')
plt.xlabel('Satzlaenge');

print("see chart")
#plt.show();

#2.5
globalLinksAndTheirPrepositons = FlagArray2_5();
#globalLinksAndTheirPrepositons = 
for link in globalLinks:
    for prepositon in globalSpatialSignals:
        if link.trigger == prepositon.id:
            globalLinksAndTheirPrepositons.appendOrsubAppend(link.id, prepositon.text)


print("\n\n\n\n\n\n\n\nAUFGABE 2.4.v - Links ids: wovon getriggert")
for link in globalLinksAndTheirPrepositons.contents:
    print('\n\n' + link.flagValue + ': ')
    for child in link.children:
        print(child + ', ', end='')

#2.6
#output global motion verbs
lst2 = [];
for verb in globalVerbs.contents:
    lst2.append((verb.flagValue,int(verb.repetitions)))
    
lst2.sort(key=snd, reverse=True)

print('\n\n\n\n\n\n\n\nAUFGABE 2.4.vi - top 5 motion Verbs, #\n')
for index, entry in enumerate(lst2):
    if fst(entry) in globalMotions:
        print( fst(entry) + ': ' + str(snd(entry)) + ', ')
    if index == 10:
        break



print('\n\n\n\n\n\n\n\n2.2.ii \n siehe result.txt\n')
# print(str(len(chapters[0].words)) + ' words in chapter')

# schreibe den Text in ne Datei
import io
with io.open(result, "w", encoding="utf-8") as of:
    # of.write(masterText)
    for chapter in chapters:
        of.write(str(chapter.file) + '\n')
        of.write('nouns: ' + str(len(chapter.nouns)) + '\n')
        of.write('verbs: ' + str(len(chapter.verbs)) + '\n')

        #PoS and their counts
        of.write('PoS, #\n')
        for pos in chapter.flags.pos_.contents:
            of.write( str(pos.flagValue) + ': ' + str(pos.repetitions) + ', ')
        of.write('\n')
of.close()

plt.show();