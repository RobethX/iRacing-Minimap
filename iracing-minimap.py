import irsdk
from tkinter import *
import logging
import time
import sys
import threading
from queue import *

### INITIALIZING VARIABLES
carx = 0
cary = 0
carz = 0
carxvel = 0
caryvel = 0
carzvel = 0

debug = True
#logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
loghandler = logging.FileHandler('debug.log')
loghandler.setLevel(logging.INFO)
logformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loghandler.setFormatter(logformatter)
log.addHandler(loghandler)

ir = irsdk.IRSDK()
ir.startup()

root = Tk()
root.wm_title("iRacing Minimap by Rob Chiocchio")
root.attributes('-alpha', 0.3, '-topmost', 1)
root.protocol("WM_DELETE_WINDOW", sys.exit)
root.geometry("350x500")
#root.update() # initialize tkinter before the loop

class State:
	ir_connected = False
	last_car_setup_tick = -1

def check_iracing():
	if state.ir_connected and not (ir.is_initialized and ir.is_connected):
		state.ir_connected = False
		state.last_car_setup_tick = -1
		ir.shutdown()
		log.debug('IRSDK disconnected')
	elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
		state.ir_connected = True
		log.debug('IRSDK connected')

q = Queue(maxsize=0)
q.put(1)
		
def tk_loop():
	#log.debug("Starting Tkinter mainloop")
	root.update() # substitute for root.mainloop()
	#root.mainloop()
	# requeue

def irsdk_getdata():
	ir.freeze_var_buffer_latest()
	
	carontrack = ir[IsOnTrack]
	#carx = 
	#cary = 
	#carz = 
	carxvel = ir[VelocityX]
	caryvel = ir[VelocityY]
	carzvel = ir[VelocityZ]
	cargear = ir[Gear]
	carspeed = ir[Speed] # meters/second
	carthrottle = ir[Throttle] # percent 0-1
	carbrake = ir[Brake] # percent 0-1
	laptimelast = ir[LapLastLapTime]
	lapdist = ir[LapDistPct] # in percent
	
irsdk_loop_enabled = True
def irsdk_loop():
	while irsdk_loop_enabled:
			check_iracing()
			if state.ir_connected:
				irsdk_getdata()
			time.sleep(1)
	
other_loop_enabled = True
def other_loop():
	while other_loop:
		#print("test")
		carx = carx + carxvel
		cary = cary + caryval
		carz = carz + carzvel
		print("CarX: %s | CarY: %s | CarZ: %s", carx, cary, carz)

if __name__ == '__main__':
	ir = irsdk.IRSDK()
	state = State()

	try:
		irsdk_thread = threading.Thread(target=irsdk_loop)
		other_thread = threading.Thread(target=other_loop)
		#tk_thread = threading.Thread(target=)
		irsdk_thread.daemon = True
		other_thread.daemon = True
		#tk_thread.daemon = True
		irsdk_thread.start()
		other_thread.start()
	except KeyboardInterrupt:
		log.debug("Interrupted")
		pass

root.mainloop()
#q.join()
sys.exit()
