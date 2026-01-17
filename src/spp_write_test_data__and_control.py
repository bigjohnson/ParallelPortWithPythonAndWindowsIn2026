# Example using ctypes directly (from psychopy source)
from ctypes import windll
import parallel64
import time

pippo = parallel64.StandardPort(0xEFF8)
pluto = 1
while True:
    pippo.write_data_register(pluto)
    pippo.write_control_register(0)
    time.sleep(.05)
    pippo.write_control_register(255)
    time.sleep(.05)
    pluto = pluto << 1
    if pluto > 128:
        pluto = 1
#pippo.write_spp_data(255)

