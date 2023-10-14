A = [0.0] * 3  
B = [0.0] * 3 
PScalaire = 0.0 


for i in range(3):
    A[i] = float(input(f"Entrez l'élément {i + 1} du premier vecteur : "))


for i in range(3):
    B[i] = float(input(f"Entrez l'élément {i + 1} du deuxième vecteur : "))


for i in range(3):
    PScalaire += A[i] * B[i]

print("Le produit scalaire des deux vecteurs est :", PScalaire)
