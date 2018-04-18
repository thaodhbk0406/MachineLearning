from sklearn.cluster import KMeans
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(11)

file1= open("Deliver3GroupExample.ml", "r")
X1=file1.read()

ans=X1.splitlines()
del(ans[0])

X=[]
for i in ans:
	ans1=i.split()
	ansi=[]
	ansi.append(float(ans1[0]))
	ansi.append(float(ans1[1]))
	
	X.append(ansi)


X = np.array(X)
def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)

    plt.axis('equal')
    plt.plot()
    plt.show()

kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
print('Centers found by scikit-learn:')
print(kmeans.cluster_centers_)
pred_label = kmeans.predict(X)
print(X)
kmeans_display(X, pred_label)


