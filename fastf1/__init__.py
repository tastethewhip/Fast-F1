"""
Introduction
============

This package features two main online sources of data:
    - The official f1 data stream ->
      `link <https://www.formula1.com/en/f1-live.html>`_
    - Ergast web api -> `link <http://ergast.com/mrd/>`_

Car position, speed traces, tyres, timings and weekend history are some
of the many available resources. No formula1 account is needed.

The library is designed to be interfaced with matplotlib (although you
can use whatever you want) but there is a neat :mod:`plots` module which
you can import and gives some color to your graphs. 

Modules handle big chunks of data (~30mb per session) so most of the
information is stored locally as cached requests (be aware).

Have fun!

Getting started
===============

Setting up a running snippet is straightforward::

    import fastf1 as ff1

    monza_quali = ff1.get_session(2019, 14, 'Q')
    monza_quali = monza_quali.init()

    vettel = monza_quali.get_driver('VET')
    print(f"Pronto {vettel.name}?")
    # Pronto Se🅱️astian?

For some more advanced stuff, just a few more steps::

    from matplotlib import pyplot as plt
    from fastf1 import plots

    laps = monza_quali.load_laps().laps
    leclerc_lap = laps[laps['Driver'] == 'LEC'].iloc[4]
    t = leclerc_lap.telemetry['Time']
    vCar = leclerc_lap.telemetry['Speed']

    # The rest is just plotting
    fig, ax = plt.subplots()
    ax.plot(t, vCar, label='Fast')
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed [Km/h]')
    ax.set_title('Leclerc is')
    ax.legend()
    plt.show()

.. image:: _static/gettingstarted.svg
    :target: _static/gettingstarted.svg

"""
from fastf1.core import get_session
