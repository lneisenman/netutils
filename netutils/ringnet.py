# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)

from .netutils import BaseNet


class RingNet(BaseNet):
    ''' encapsulation of the serial version of the ring net from
    Hines et al 2008 '''

    def __init__(self, NCELL, make_cell_fcn):
        super().__init__(NCELL, make_cell_fcn)
        super().make_stim()
        self.connect_cells()

    def connect_cells(self):
        for i, cell in enumerate(self.cellList):
            target = (i + 1) % self.NCELL
            syn = self.cellList[target].synlist.object(0)
            nc = cell.connect2target(syn)
            nc.delay = 1
            nc.weight[0] = 0.01
            self.ncList.append(nc)
