import numpy as np
from my_naivebayes import NB_continues

# Exemple d'utilisation
X = np.array([[1.5, 2.3], [2.1, 3.3], [1.2, 0.8], [1.9, 2.8], [2.0, 1.9]])
Y = np.array([0, 0, 1, 1, 0])
x = np.array([1.6, 2.5])

predicted_class, probabilities = NB_continues(X, Y, x)
print("Classe prédite:", predicted_class)
print("Probabilités postérieures:", probabilities)