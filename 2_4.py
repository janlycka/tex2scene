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
        # lasse spacy sein Magic machen, gewinne 'Noun phrases' und 'Verbs'
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




class Metalink:
    def __init__(self, objectID1, objectID2):
        self.objectID1 = objectID1
        self.objectID2 = objectID2

globalMetaLinks = [];

class Kante:
    def __init__(self, fromID, toID, klasse, text):
        self.klasse = klasse
        self.text = text
        self.fromID = fromID
        self.toID = toID

        # da die Kanten nur zum Zeichnen sind, muessen wir hierbei nicht untescheiden zu welchem ID sie je fuehren, solance dem ein dessen pendant vorliegt
        for vertex in vertices.contents:
            if fromID in vertex.ids:
                 #einfachkeitshalber nehme die erste ID
                self.fromID = vertex.ids[0];
            if toID in vertex.ids:
                self.toID = vertex.ids[0];

class Knoten:
    def __init__(self, id, klasse, text):
        self.klasse = klasse
        self.texts = [text]
        self.ids = [id]

class KnotenArray:
    def __init__(self):
        self.contents = [];

    def appendOrMerge(self, id, klasse, text):
        if self.contents == []:
            self.contents.append(Knoten(id, klasse, text));
        else:
            entered = 0
            i = 0
            for vertex in self.contents:
                if id in vertex.ids:
                    break
                else:
                    for metalnk in globalMetaLinks:
                        if (id == metalnk.objectID1 and (metalnk.objectID2 in vertex.ids)) or (id == metalnk.objectID2 and (metalnk.objectID1 in vertex.ids)):
                            print("Appending : " + id + ' + (' + metalnk.objectID1 + ' , ' + metalnk.objectID2 + ')' + ' -> ' + ''.join(self.contents[i].ids))
                            self.contents[i].ids.append(id)
                            print("Appending : " + text + ' -> ' + ''.join(self.contents[i].texts))
                            if text not in vertex.texts:
                                self.contents[i].texts.append(text)
                            entered = 1
                            break
                i+=1
                if entered:
                    break
            if entered == 0:
                self.contents.append(Knoten(id, klasse, text));

potentialVertices = []
edges = []
vertices = KnotenArray();

globalSpatialEntities = []
globalPlaces = []









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
srcs = ['RFC\\Bicycles.xml']#, 'ANC\\WhereToMadrid\\Highlights_of_the_Prado_Museum.xml']
#srcs = ['ANC\\WhereToMadrid\\Highlights_of_the_Prado_Museum.xml']
src = 'text2scene\\Training'
result = 'result.txt'
print('Reading XML Files in: ' + os.getcwd() + '\\' + src)

filenames = []
for file in srcs:
    filenames.append(src + '\\' + file)

filescount = len(filenames)
print(str(filescount) + ' XML files')

# lese und parse alle Dateien um individuelle Texte zu gewinnen
chapters = [];
masterText = ''
import xml.etree.ElementTree as ET

ind = 1;
for file in filenames:
#for file in [filenames[0], filenames[1]]:
    root = ET.parse(file).getroot()
    #extrahiere den Inhalt aus dem Tag
    for item in root.findall('TAGS/*'):
        print(str(ind) + ' / ' + str(filescount) + ' / 2    ', end='\r')

        # anazahle von S,P,M,S,Q,O
        #globalSPMSQO.appendOrRaiseByOne(item.tag)

        # Anzahl an jeweilige QSLINKs arten ermittlen
        if item.tag == 'QSLINK':
            #print(item.attrib['relType'])
            #relType = str(json.loads(str(item.attrib))['relType']) ????
            #globalQSLINKs.appendOrRaiseByOne(item.attrib['relType'])
            #globalLinks.append(MyLink(item.attrib['id'], item.attrib['trigger']))
            edges.append(Kante(item.attrib['fromID'], item.attrib['toID'], item.tag, item.attrib['relType']))

        if item.tag == 'OLINK':
            #globalLinks.append(MyLink(item.attrib['id'], item.attrib['trigger']))
            edges.append(Kante(item.attrib['fromID'], item.attrib['toID'], item.tag, item.attrib['relType']))

        if item.tag == 'SPATIAL_ENTITY' or item.tag == 'PLACE':
            potentialVertices.append(Knoten(item.attrib['id'], item.tag, item.attrib['text']))

        if item.tag == 'METALINK':
            if item.attrib['relType'] == 'COREFERENCE':
                globalMetaLinks.append(Metalink(item.attrib['objectID1'], item.attrib['objectID2']))

        ind+=1
        #print(item.tag)


# rm alle Spanischen Zeichen..
import re



import matplotlib.pyplot as plt
import numpy as np

import networkx as nx

#G = nx.complete_graph(5)
G=nx.Graph()

#from networkx.drawing.nx_agraph import graphviz_layout


# wenn es ein Metalink Knoten verbindet, verwurste die

for vertex in potentialVertices:
    vertices.appendOrMerge(vertex.ids[0], vertex.klasse, vertex.texts[0])

#vertices.contents = [Knoten('1','PLACE','KA'),Knoten('2','PLA5CE','KB'),Knoten('3','PLACE','KC'),Knoten('4','PLACE','KD')]

labeldict = {}
color_map = []

tt=1
for vertex in vertices.contents:
    label = ','.join(vertex.texts)
    print('vertex: ' + ','.join(vertex.ids) + ' - ids: ' + label)
    clr = 'blue' if vertex.klasse == 'PLACE' else 'red'
    print('adding v : ' + vertex.ids[0])
    G.add_node(vertex.ids[0])
    labeldict[vertex.ids[0]] = label
    color_map.append(clr)
    print(str(tt) + ' ' + str(len(G.nodes())))
    tt+=1

edge_labelsx = {};
#edges = [Kante('1','2','OLINK','A'),Kante('2','3','OLINK','B'),Kante('1','3','OLINK','C')];

for edge in edges:
    print('testing edge: (' + edge.fromID + ',' + edge.toID + ')')
    if edge.fromID in G.nodes() and edge.toID in G.nodes():
        edgeObj = (edge.fromID, edge.toID)
        print('edge: (' + edge.fromID + ',' + edge.toID + ')')
        G.add_edge(*edgeObj)
        edge_labelsx[(edge.fromID, edge.toID)] = re.sub('[^0-9a-zA-Z]+', '_', edge.text)

r=0
for index,node in enumerate(G):
    r+=1
#    if index < 10:
#        color_map.append('blue')
#    else: 
#        color_map.append('green')
#




pos = nx.spring_layout(G)
plt.figure()    



print(len(vertices.contents))
print(r)


print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#pos = graphviz_layout(G)
nx.draw(G,pos, node_color=color_map, labels=labeldict, with_labels = True,alpha=0.5)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labelsx,font_color='red')

plt.savefig("path_graph1.png")
plt.show()
