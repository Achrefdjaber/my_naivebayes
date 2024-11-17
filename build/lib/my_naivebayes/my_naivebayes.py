import numpy as np
def px(x, u, s):
    s = np.where(s == 0, 10**-15, s)
    A = (1 / (s * (2 * np.pi) ** 0.5)) 
    B = np.e ** (-(1/2) * (x - u) ** 2 / (s**2))
    return A * B

def NB_continues(X, Y,x):
    classes_probas = np.bincount(Y) / len(Y)
    U_per_attr_per_class = np.array([X[Y == c].mean(axis=0) for c in np.unique(Y)])
    S_per_attr_per_class = np.array([X[Y == c].std(axis=0) for c in np.unique(Y)])
    px_ = np.array([px(x, U_per_attr_per_class[i], S_per_attr_per_class[i]) for i in range(len(U_per_attr_per_class))])
    px_ = px_.prod(axis=1)
    res = classes_probas * px_
    return np.argmax(res),res