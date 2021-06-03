import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import seaborn as sns

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('tmdb_5000_movies.csv')
tfidf = TfidfVectorizer(stop_words="english")
tfidf.fit(df['Text'])

# scipy.sparse.csr.csr_matrix
X = tfidf.transform(df['Text'])

svd = TruncatedSVD(100)
svd.fit(X)

Sigma_mat = np.diag(svd.singular_values_)
Vt = svd.components_

term_space = tfidf.get_feature_names()
for i in range(10):
    print("Topic %s: " % i)
    best_terms = [(importance, term) for term, importance in zip(term_space, Vt[i])]
    best_terms.sort(reverse=True)
    for importance, term in best_terms[:10]:
        print("%s (%.2E)" % (term, importance))

B2 = X.dot(Vt[0:2].transpose())
B2_labeled = np.hstack([B2, df[['Score']].to_numpy()])
B2_df = pd.DataFrame(B2_labeled, columns=["x", "y", "score"])
sns.scatterplot(x="x", y="y", hue="score", legend="full", data=B2_df)
plt.show()

B3 = X.dot(Vt[0:3].transpose())
B3_labeled = np.hstack([B3, df[['Score']].to_numpy()])
B3_df = pd.DataFrame(B3_labeled, columns=["x", "y", "z", "score"])

fig = plt.figure()
ax = Axes3D(fig)
colors = ["b", "g", "r", "c", "m", "y", "k", "w"]
for i, cat in enumerate(list(set(B3_df['score']))):
    sub_B3_df = B3_df[B3_df['score'] == cat]
    ax.scatter(sub_B3_df['x'], 
               sub_B3_df['y'], 
               sub_B3_df['z'],
               c=colors[i])
plt.show()
import ipdb;ipdb.set_trace()

