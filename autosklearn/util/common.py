# -*- encoding: utf-8 -*-

import os
import warnings

import numpy as np

__all__ = ["check_pid", "warn_if_not_float"]


def warn_if_not_float(X: np.ndarray, estimator: str = "This algorithm") -> bool:
    """Warning utility function to check that data type is floating point.
    Returns True if a warning was raised (i.e. the input is not float) and
    False otherwise, for easier input validation.
    """
    if not isinstance(estimator, str):
        estimator = estimator.__class__.__name__
    if X.dtype.kind != "f":
        warnings.warn(
            "%s assumes floating point values as input, "
            "got %s" % (estimator, X.dtype)
        )
        return True
    return False


def check_pid(pid: int) -> bool:
    """Check For the existence of a unix pid."""
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def check_true(p: str) -> bool:
    if p in ("True", "true", 1, True):
        return True
    return False


def check_false(p: str) -> bool:
    if p in ("False", "false", 0, False):
        return True
    return False


def check_none(p: str) -> bool:
    if p in ("None", "none", None):
        return True
    return False


def check_for_bool(p: str) -> bool:
    if check_false(p):
        return False
    elif check_true(p):
        return True
    else:
        raise ValueError("%s is not a bool" % str(p))
