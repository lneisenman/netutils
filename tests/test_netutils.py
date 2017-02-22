# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)

from neuron import h

from netutils import RingNet
import netutils as nu


def test_RingNet():
    h.load_file("stdrun.hoc")   # load the standard run libraries
    h.load_file("tests/cell.hoc")     # load the cell model

    net = RingNet(NCELL=20, make_cell_fcn=h.B_BallStick)
    recording = nu.SpikeRecorder(net.cell_list())

    sc = nu.SimulationController()
    sc.init_sim()
    sc.run(100)

    recording.print_spikes()
    last = len(recording.idvec) - 1
    assert abs(recording.tvec[last] - 99.65) < 0.001
    assert int(recording.idvec[last]) == 12
