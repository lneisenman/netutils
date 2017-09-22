# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)


def separate_cells(recording):
    ''' separate spike times for each cell in the recording and return dict '''
    try:
        import numpy as np
    except:
        raise ImportError('No can do, Bloss. I need numpy')

    times = recording.tvec.as_numpy()
    ids = np.asarray(recording.idvec, dtype=np.int)     # float from neuron
    cells = np.unique(ids)
    data = dict()
    for cell in cells:
        index = np.where(ids == cell)
        data[cell] = times[index].copy()

    return data
