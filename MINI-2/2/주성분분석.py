from sklearn.decomposition import PCA
pca = PCA()
x1=train.drop("label",axis=1)
x1=x1.drop(p,axis=1)
y1=train[["label"]]
pca.fit(x1)
pca_score = pca.transform(x1)
pca.components_

pca.explained_variance_

pca.explained_variance_ratio_

pca = PCA(n_components=1)
pc=pca.fit_transform(x1)
pc_y = np.c_[pc,y1]
principalDF = pd.DataFrame(pc_y,columns=["pc1","label"])
principalDF