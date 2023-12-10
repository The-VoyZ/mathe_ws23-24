import random 
import seaborn as sns

#Aufgabe 1
random.seed(4327) #seed ein Tragen
print(random.randint(75,958)) #Range Eintragen

#Aufgabe 2
random.seed(4327)
i = 1
while i <= 2 :
    print(random.randint(75,958))
    i += 1

#Aufgabe 3
random.seed(2949)
x = random.random()
print(f"{x:.5}")#gibt die antwort auf 5 nachkommerstellen gerundet an 

#Aufgabe 4
random.seed(6702)
print(random.sample(range(15),4))

#Aufgabe 5-7
df = sns.load_dataset("penguins")
print(df.loc[133])

#Aufgabe 8
print(df["island"].value_counts())

