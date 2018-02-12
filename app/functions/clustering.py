import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA

def kmeans_quick(X, num_clusters, pca=False):
    #TODO: Create storage of summary statistics for clusters
    # So, like what the things have in common and such as an output
    orig_num_features = X.shape[1]
    orig_data = X.copy()

    #Don't need to call this function here, but might be useful elsewhere
    '''
    if title == "":
        title = 'KMeans Clustering with '+str(num_clusters)+' Clusters'
    else:
        title = title + ' - Kmeans Clustering with '+str(num_clusters)+' Clusters'
    
    if pca == True:
        pca = PCA(n_components=2)
        X = pca.fit_transform(X)
        X = pd.DataFrame(X)
        title = title + ' / PCA'
        importance_df = get_pca_feature_importance(pca, orig_data)
        print("\nP1 most important \n", importance_df[
            importance_df.columns[0]].apply(lambda x: abs(x)).sort_values(ascending=False).head())
        print("\nP2 most important \n", importance_df[
            importance_df.columns[1]].apply(lambda x: abs(x)).sort_values(ascending=False).head())
        
    title = title + ' - from '+ str(orig_num_features) + ' features'
    '''

    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    orig_data['labels'] = labels
    
    
    '''
    X['labels'] = labels

    cmap = plt.cm.get_cmap('jet')
    for i, cluster in X.groupby('labels'):
        plt.scatter(cluster.iloc[:,0], cluster.iloc[:,1], c=cmap(i/num_clusters), label=i)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", c = 'black',s=300, linewidths=400)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    plt.close()
    '''
    return orig_data

# k means determine k
def get_opt_clusters(X, pca=False, title=""):
    if title=="":
        title = 'Optimal k for '+str(X.shape[1])+" clusters"
    if pca == True:
        pca = PCA(n_components=2)
        #z_data = z_scaler.fit_transform(X)
        X = pca.fit_transform(X)
        X = pd.DataFrame(X)
        title = title + ' / PCA'
    distortions = []
    K = range(1,10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        distortions.append(sum(np.min(cdist(
            X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
 
    # Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title(title)
    plt.show()

def spectral_quick(X, num_clusters, max_row_sample=0, x_label="", y_label = "", title="", pca=False):
    orig_num_features = X.shape[1]
    if max_row_sample == 0:
        max_row_sample = len(X)
    X = X[:max_row_sample]
    if title == "":
        title = 'Spectral Clustering with '+str(num_clusters)+' Clusters'
    else:
        title = title + ' - Spectral Clustering with '+str(num_clusters)+' Clusters'
    
    if pca == True:
        pca = PCA(n_components=2)
        X = pca.fit_transform(X)
        X = pd.DataFrame(X)
        title = title + ' / PCA'
    
    title = title + ' - from '+ str(orig_num_features) + ' features'
    
    spec = SpectralClustering(n_clusters=num_clusters)
    labels = spec.fit_predict(X)

    X['labels'] = labels
    
    cmap = plt.cm.get_cmap('jet')
    for i, cluster in X.groupby('labels'):
        plt.scatter(cluster.iloc[:,0], cluster.iloc[:,1], c=cmap(i/num_clusters), label=i)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    #plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", c = 'black',s=300, linewidths=400)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    return X

def get_pca_feature_importance(pca, orig_data):
    i = np.identity(orig_data.shape[1])
    coef = pca.transform(i)
    feature_importance = pd.DataFrame(coef, columns=['PC-1', 'PC-2'], index=orig_data.columns)
    return feature_importance