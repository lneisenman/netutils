# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)

import csv

from neuron import h


class SpikeRecorder(object):
    ''' class for saving network firing times

    this class creates two hoc vectors (tvec and idvec) which record the
    time that each neuron in the network fires.

    Pass a list of the cells in the network when creating, e.g.::
        recorder = SpikeRecorder(net.cell_list())

    Based on Hines JNM 2008

    '''

    def __init__(self, cell_list):
        self.tvec = h.Vector()
        self.idvec = h.Vector()
        for i, cell in enumerate(cell_list):
            nc = cell.connect2target(None)
            nc.record(self.tvec, self.idvec, i)

    def print_spikes(self):
        ''' print firing times to the main console '''
        print("\ntime\tcell#")
        for t, idv in zip(self.tvec, self.idvec):
            print('{:.2f}\t{:d}'.format(t, int(idv)))

    def save_spikes(self, filename='output.csv'):
        ''' save firing times to an excel csv file

        ..parameter: filename - text

        '''
        with open(filename, 'w') as datafile:
            writer = csv.writer(datafile, dialect='excel')
            writer.writerow(['time', 'cell id'])
            for t, idv in zip(self.tvec, self.idvec):
                writer.writerow([t, int(idv)])
