#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import argparse

from raspi_sensor.main import setup_default_args
from raspi_dht.dht import Dht


def setup_args():
    ap = argparse.ArgumentParser(prog='rpi-dht',
                                 description='RPi.DHT is Python implementation for Adafruit_DHT sensor for Raspberry '
                                             'Pi. For more info visit: https://github.com/ricco386/RPi')
    setup_default_args(ap)
    ap.add_argument('--temperature', action='store_true', help='Display temperature in *C.')
    ap.add_argument('--humidity', action='store_true', help='Display humidity in percent.')

    return ap.parse_args()


def main():
    params = setup_args()
    name = 'DHT'

    if hasattr(params, 'name') and params.name:
        name = params.name

    d = Dht(name=name, params=params)

    if hasattr(params, 'status') and params.status:
        d.sensor_read()
        print(d.output())
    elif hasattr(params, 'temperature') and params.temperature:
        d.sensor_read()
        print(d.output(temp=True, desc=False))
    elif hasattr(params, 'humidity') and params.humidity:
        d.sensor_read()
        print(d.output(hum=True, desc=False))
    else:
        d.sense()


if __name__ == "__main__":
    # execute only if run as a script
    main()