import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_olivetti_faces
from sklearn.neighbors import NearestNeighbors

np.random.seed(1000)

if __name__ == '__main__':
    print('Starting')

faces = fetch_olivetti_faces()
X = faces['data']

knn = NearestNeighbors(n_neighbors=10, metric='minkowski', p=2, radius=20.0, algorithm='ball_tree')
knn.fit(X)

i = 20
test_face = X[i] + np.random.normal(0.0, 0.1, size=(X[0].shape[0]))
sns.set()

fiq, ax = plt.subplots(figsize=(5, 3))

distances, neighbors = knn.kneighbors(test_face.reshape(1, -1))
fig, ax = plt.subplots(1, 10, figsize=(18, 8))

for i in range(10):
    idx = neighbors[0][i]
    ax[i].imshow(X[idx].reshape((64, 64))* 255.0, cmap='gray')
    ax[i].grid(False)
    ax[i].set_xticks([])
    ax[i].set_yticks([])
    ax[i].set_xlabel('d={0:.2f}'.format(distances[0][i]))
plt.show()

distances, neighbors = knn.radius_neighbors(test_face.reshape(1, -1), radius=100.0)
sd, sd_arg = np.sort(distances[0]), np.argsort(distances[0])

fig, ax = plt.subplots(2, 10, figsize=(18, 4))

for i in range(2):
    for j in range(10):
        idx = neighbors[0][sd_arg[(i * 10) + j]]
        ax[i, j].imshow(X[idx].reshape((64, 64)) * 255.0, cmap='gray')
        ax[i, j].grid(False)
        ax[i, j].set_xticks([])
        ax[i, j].set_yticks([])
        ax[i, j].set_xlabel('d={0:.2f}'.format(sd[(i*10)+ j]))
plt.show()