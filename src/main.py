import rovio
import time

r = rovio.Rovio( '192.168.1.139' ) # ip addess of rovio

# start at the rover's home
r.head_up()
time.sleep(0.3)
r.head_middle()
time.sleep(0.3)
r.head_up()
time.sleep(0.3)
r.head_middle()