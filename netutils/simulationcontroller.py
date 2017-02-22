# -*- coding: utf-8 -*-

from __future__ import (print_function, absolute_import, unicode_literals,
                        division)

from neuron import h


class SimulationController(object):
    ''' class for controlling simulations

    This can accomodate multicore CPUs but not multiple CPUs
    '''

    def __init__(self):
        self.CV = h.CVode()
        self.CV.active(0)
        self.pc = h.ParallelContext()
        self.t = h.t
        self.set_fixed_dt()
        self.set_v_init()   # -60 mV
        self.set_celsius()  # 6.3 degrees

    def set_variable_dt(self):
        ''' turn on variable time step '''
        self.CV.active(1)
        self.set_max_dt()

    def set_max_dt(self, max_dt=10):
        ''' set the maximum time step when using a variable time step '''
        self.CV.maxstep(max_dt)

    def set_fixed_dt(self, dt=0.025):
        ''' turn off variable time step and use a fixed time step

        ..parameter: dt - float

        '''
        self.CV.active(0)
        self.dt = h.dt = dt
        h.steps_per_ms = 1.0/dt

    def set_celsius(self, temp=6.3):
        '''set h.celsius to temp '''
        self.celsius = h.celsius = temp

    def set_v_init(self, v_init=-65):
        ''' set h.v_init to v_init '''
        self.v_init = h.v_init = v_init

    def set_nthread(self, num):
        ''' allows use of multiple cores

        .. warning:: if there is a netcon with a delay of zero (or less that dt?)
            calling h.finitialize() (e.g. with init_sim()) will
            generate an unhelpful hoc error

        '''
        self.pc.nthread(num)

    def init_sim(self):
        ''' calls h.finitialize(self.v_init)

        Call immediately before calling run()
        '''
        h.finitialize(self.v_init)

    def run(self, tstop=100):
        ''' run the simulation up to time tstop '''
        runtime = h.startsw()
        h.tstop = tstop - h.dt/2.0
        if (self.CV.active() == 0):
            while (h.t < h.tstop):
                h.fadvance()
        else:
            self.CV.solve(h.tstop)
        runtime = h.startsw() - runtime
        print("simulation completed in", runtime, "seconds.")

    def stdrun(self,  tstop):
        ''' run the simulation using NEURON's standard run system

        .. warning:: this function assumes you have already imported NEURON's stdrun
            with h.load_file("stdrun.hoc")

        '''
        runtime = h.startsw()
        h.tstop = tstop
        h.run()
        runtime = h.startsw() - runtime
        print("simulation completed in", runtime, "seconds.")
