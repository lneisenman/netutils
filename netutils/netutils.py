# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)

from neuron import h


class BaseNet(object):
    ''' basic class for a network model

    subclass to build a particular network

    :param NCELL: number of cells in the network
    :param make_cell_fcn: function that returns a cell model.
        The model is assumed to have been created with the NEURON GUI tools
    :type make_cell_fcn: function

    Typical usage is a follows

    .. code-block:: python3

        class NewNet(BaseNet)

            def __init__(self, NCELL, make_cell_fcn):
                BaseNet.__init__(self, NCELL, make_cell_fcn)
                self.connect_cells()
                self.make_stim()

    '''

    def __init__(self, NCELL, make_cell_fcn):
        ''' create the network '''
        self.NCELL = NCELL
        self.cellList = list()  # will be Lists that hold all network cell
        self.ncList = list()    # and NetCon instances, respectively
        self.make_cells(make_cell_fcn)

    def make_cells(self, make_cell_fcn):
        ''' creates the cells and appends them to a List called cellList
        argument is the function for creating cells '''
        for i in range(int(self.NCELL)):
            cell = make_cell_fcn()
            self.cellList.append(cell)

    def make_stim(self, delay=0):
        ''' attach a stimulus to the first cell '''
        self.stim = h.NetStim()
        self.stim.number = 1
        self.stim.start = 0
        self.ncstim = h.NetCon(self.stim, self.cellList[0].synlist.object(0))
        self.ncstim.delay = delay
        self.ncstim.weight[0] = 0.01

    def connect_cells(self):
        ''' connect the cells in the network

        You must redefine in your subclass as this version throws an exception
        '''
        raise NotImplementedError(
            "Dude, you need to write a connect_cells method")

    def cell_list(self):
        ''' return a list of the cells in the network '''
        return self.cellList
