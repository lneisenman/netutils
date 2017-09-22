# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)


def draw_raster_plot(recording, start_time=0, end_time=None,
                     start_contact=None, end_contact=None, color='black',
                     display=False):
    ''' Make a rasterplot with Numpy and Matplotlib '''
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except:
        raise ImportError("No can do, Bloss. I need numpy and matplotlib")

    plt.style.use({'axes.spines.top': False, 'axes.spines.right': False})

    tvec = np.asarray(recording.tvec)
    idvec = np.asarray(recording.idvec)

    if len(tvec) == 0:
        print('no spikes so no raster')
        return

    if end_time is None:
        last_time = tvec[-1]
    else:
        last_time = end_time

    if start_contact is None:
        first_contact = np.min(idvec)
    else:
        first_contact = start_contact

    if end_contact is None:
        last_contact = np.max(idvec)
    else:
        last_contact = end_contact

    index = np.greater_equal(tvec, start_time) & \
        np.less_equal(tvec, last_time) & \
        np.greater_equal(idvec, first_contact) & \
        np.less_equal(idvec, last_contact)

    plt.figure()
    raster_plot = plt.plot(tvec[index], idvec[index], '|', c=color)
    if display is True:
        plt.show()

    return raster_plot
