import seaborn as sns
import random
import matplotlib.pyplot as plt

#Wichtig für Statistik ist die unterscheidung von Quantitative Merkmale und Qualitative Merkmale

species = "Adelie" #definiert eine Variable als String | ein string wird mit "" oder '' Defniniert. Species könnte genau so gut x heißen da es frei definierbar ist
anzahl = 17 #Integer ist immer eine Ganze zahl
gewicht = 4.880 #float zahl also zahl mit "Komma stellen" 

#Erfassung der Daten aller Zufälligen tiere einer Population nennt man Urliste / Protokoll 

random.random() #gibt eine zahl zwischen 0 und 1 zurück
random.randint(0,20)#gibt eine zufällige zahl zwischen 0 und 20 aus
random.sample(range(10),5) #gibt 5 zahlen als array zurück die zwischen 0 und 10 liegen 

#Seeding
 
random.seed(123)#gibt dem Random generator eine Anfangszahl / Buchstaben um die zufalls zahlen zu generieren. 
print(random.randint(1,100))
random.seed(123)
print(random.randint(1,100))#Wird die gleiche zahl wie der erste Print ausgeben da der seed wieder eingesetzt wurde

#df wird fast immer als variable für Data Frames genutzt. Dataframes sind nichts anderes als Excel tabellen / CSV dateien in python schön dargestellt.
df = sns.load_dataset("penguins") 
#print(df) #Einmal zur darstellung wie ein DataFrame aussieht

#Histogramm 
graph1 = sns.displot(df, x="flipper_length_mm")#Erstellt ein Balkendiagramm aus der Flipper Länge in mm die im DF liegt
plt.close() # um den graphen anzuzeigen einfach plt.show() die raute entfernen und bei plt.close() raute davor hinzufühen. wird plt.close() nicht auskommentiert wird der Graph nicht angezeigt. Ansonsten werden alle Graphen die in diesem Scrypt erstellt werden auf einmal angezeigt in verschiedenen fenstern. 
#plt.show() #Einfach die raute entfernen um den Plot anzuzeigen da es kein Jupiter notebbook ist. muss ich es anzeigen lass und die # wird dazu genutzt auszukommentieren das der code nicht ausgeführt wird.


sns.histplot(df , x="flipper_length_mm", bins= 20 ,binwidth= 2.5) # erstellt ein Balkendiagramm mit 20 unterscheidungen und ist 2.5 Weit
plt.close()
#plt.show() #Einfach die raute entfernen um den Plot anzuzeigen da es kein Jupiter notebbook ist.


sns.displot(df,col="island",x="species",hue="sex",multiple="stack") #Erstellt ein Diagramm das die Pinguine nach gefangenen Inseln sortiert und die Farb abspalltung mit hue in die Geschlächter auftrennt. 
plt.close()
#plt.show()


#mit sns.displot? wird ein String Ausgegeben der anzeigt welche eingabe möglichkeiten bestehen dies geht aber nur in JupiterNotebooks. In Visual studio code kann man einfach über die funktion hovern und bekommt auch den input angezeigt der genutzt werden kann. 
data = df["flipper_length_mm"] #zeigt alle daten aus dem DF an die in der spalte flipper_length_mm sind inklusive der daten typen und wie viele einträge dort gespeichert sind
#print(data)

data = df.loc[222]#gibt die spalte 222 aus
#print(data)

sns.displot(df,x="flipper_length_mm")#ist Bimodal / hat zwei maxima, mit warscheinlichkeit zwischen männlich und weiblich
#plt.show()
w=df[df.sex=="Female"] # == bedeutet so viel wie ist das geschlecht weiblich dann füge es der Variable w hinzu ansonsten nicht. 
#print(w)

sns.displot(w,x="flipper_length_mm")
plt.close()
#plt.show()


sns.displot(df,x="flipper_length_mm" ,col="species")#Zeigt die Langen nach Spezies in 3 Verschiedenplotts an
plt.close()
#plt.show()

"""
Vergleichs Operatoren : 
x = 1 weist x die 1 zu
1 == 1 heist das 1 wirklich 1 ist und gibt true zurück
1== 2 wäre false da es nicht korrekt ist

es gibt noch Ungleich 
1 != 2 das wäre auch wieder True

"""

sns.displot(df,x="flipper_length_mm",col="species",hue="sex",binwidth = 3,bins=15)
plt.close()
#plt.show()

data = df["species"].value_counts()
plt.close()
#plt.show()
data = df["species"].value_counts().plot.pie()
#plt.close()
plt.show()