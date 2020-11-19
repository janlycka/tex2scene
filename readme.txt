Jan Lycka
S7481099, Matnr. 7066140
Fingeruebung 2020/21

PYTHON
besondere Libraries:
	import spacy
	import json
	import os
	from pathlib import Path
	import xml.etree.ElementTree
	import matplotlib.pyplot
	import numpy
	import io
	import re
	import networkx

BASE: C:\Users\Jan>

#Aufgabe 2.2
	Alle Teilaufgaben per ein Durchlauf auszugeben in der Console und Dateien
		python text2scene/2_4_i.py

#Aufgabe 2.2.i einlesen
	siehe linie 145-202 in reader.py

#Aufgabe 2.2.ii abspeichern
	siehe linie 300 in reader.py
	siehe result.txt

#Aufgabe 2.2.iii - ElementTree benutzen
	siehe linie 145-202 in reader.py

#Aufgabe 2.2.iv - SpaCy benutzen
	siehe linie 34-93,  in reader.py
---

#Aufgabe 2.3
	Alle Teilaufgaben per ein Durchlauf auszugeben in der Console und Dateien
		python text2scene/2_4_i.py

#Aufgabe 2.3.i
	PoS-Tags , frequency

	SPACE: 825,
	PROPN: 2095,
	AUX: 1035,
	DET: 3203,
	NOUN: 5030,
	ADP: 3005,
	PUNCT: 3501,
	ADV: 1326,
	ADJ: 1781,
	VERB: 2721,
	PRON: 1362,
	NUM: 683,
	CCONJ: 825,
	SCONJ: 431,
	PART: 491,
	X: 30,
	SYM: 28,
	INTJ: 10,

#Aufgabe 2.3.ii
	SPMSQO, #

	PLACE: 1852,
	PATH: 434,
	SPATIAL_ENTITY: 1417,
	NONMOTION_EVENT: 341,
	MOTION: 771,
	SPATIAL_SIGNAL: 714,
	MOTION_SIGNAL: 526,
	MEASURE: 170,
	QSLINK: 970,
	OLINK: 244,
	MOVELINK: 803,
	MEASURELINK: 93,
	METALINK: 1788,
	CP: 17,
	URL: 17,
	MLINK: 42,

#Aufgabe 2.3.iii
	LINKs, #

	NTPP: 42,
	IN: 586,
	EC: 196,
	TPP: 53,
	EQ: 35,
	PO: 12,
	OUT: 3,
	DC: 41,

#Aufgabe 2.3.iv
	siehe 2_3_iv.png

#Aufgabe 2.3.v

	QLINKs, OLINKs: getriggert von Praep.

	qsl3:
	houses, on, West of, in, connects, around, toward, south of...

	qsl4:
	in, east, on, to, where, of, behind, at...

	qsl6:
	in, with, Southeast of, on, into, on top of, at,...

	#Aufgabe 2.3.vi

		motion Verbs, #
		left: 29,
		found: 27,
		take: 24,
		visited: 24,
		biked: 22,

---

#Aufgabe 2.4
	Es wird eine Grafik generiert, man muss etwas daranzoomen um einzelte Kanten zu sehen

#Aufgabe 2.4.i
	python text2scene/2_4_i.py
	siehe 2_4_i.png

#Aufgabe 2.4.ii
	python text2scene/2_4_ii.py
	siehe 2_4_ii.png