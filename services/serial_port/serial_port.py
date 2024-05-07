#!/usr/bin/python

import time

from pysbus.sbus import SBUS
from pysbus.constants import SBUSConsts
from pysbus.serial_parser import SerialParser


if __name__ == "__main__":
    receiver = SBUS(SerialParser('/dev/ttyTHS0', 100000))
    print("Opened serial port")
    receiver.begin()

    channels = [0] * SBUSConsts.NUM_CHANNELS

    try:
        while True:
            print("Waiting for incoming communication.")
            payload_ready, failsafe, lost_frame = receiver.read(channels)
            time.sleep(1)
    except:
        raise()
    finally:
        print("Closing serial port")
        receiver.close()

    receiver.close()
