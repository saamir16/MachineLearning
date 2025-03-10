

def __init__(self,k=2,max_iterations=500):
    self.k = k
    self.max_iterations = max_iterations

def __init__random_centroids(self,X):
    "" Initialize the centroids as k random sample""
    n_samples, n_features  np.shape(X):
    centroids = np.zeros(self.k, n_features) 
   