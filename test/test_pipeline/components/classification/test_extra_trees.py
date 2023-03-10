import sklearn.ensemble

from autosklearn.pipeline.components.classification.extra_trees import (
    ExtraTreesClassifier,
)

from .test_base import BaseClassificationComponentTest


class ExtraTreesComponentTest(BaseClassificationComponentTest):

    __test__ = True

    res = dict()
    res["default_iris"] = 0.96
    res["iris_n_calls"] = 9
    res["default_iris_iterative"] = res["default_iris"]
    res["default_iris_proba"] = 0.10053485167017469
    res["default_iris_sparse"] = 0.74
    res["default_digits"] = 0.9216757741347905
    res["digits_n_calls"] = 9
    res["default_digits_iterative"] = res["default_digits"]
    res["default_digits_iterative_places"] = 3
    res["default_digits_binary"] = 0.994535519125683
    res["default_digits_multilabel"] = 0.9983621593291405
    res["default_digits_multilabel_proba"] = 0.997710730679746

    sk_mod = sklearn.ensemble.ExtraTreesClassifier
    module = ExtraTreesClassifier
    step_hyperparameter = {
        "name": "n_estimators",
        "value": module.get_max_iter(),
    }
