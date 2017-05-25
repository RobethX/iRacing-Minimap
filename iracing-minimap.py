import irsdk
from tkinter import *
import logging

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
root.attributes('-alpha', 0.3)
root.mainloop()

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

def loop():
	ir.freeze_var_buffer_latest()

if __name__ == '__main__':
	ir = irsdk.IRSDK()
	state = State()

	try:
		while True:
			check_iracing()
			if state.ir_connected:
				loop()
			time.sleep(1)
	except KeyboardInterrupt:
		log.debug("Interrupted")
		pass

# exit quit etc. commands needed?
