from nose.tools import assert_equals

from .. import datasets
from ..pca import PCA

iris = datasets.load_iris()

X = iris.data

def test_pca():
    """
    PCA
    """

    pca = PCA(k=2)
    X_r = pca.fit(X).transform(X)
    assert_equals(X_r.shape[1], 2)

    pca = PCA()
    pca.fit(X)
    assert_equals(pca.explained_variance_.sum(), 1.0)
