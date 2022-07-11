from avalanche import benchmarks
from avalanche import evaluation
from avalanche import logging
from avalanche import models
from avalanche import training


__version__ = "0.2.0a"

_dataset_add = None


def _avdataset_radd(self, other, *args, **kwargs):
    from avalanche.benchmarks.utils import AvalancheClassificationDataset

    global _dataset_add
    if isinstance(other, AvalancheClassificationDataset):
        return NotImplemented

    return _dataset_add(self, other, *args, **kwargs)


def _avalanche_monkey_patches():
    from torch.utils.data.dataset import Dataset

    global _dataset_add
    _dataset_add = Dataset.__add__
    Dataset.__add__ = _avdataset_radd


_avalanche_monkey_patches()
