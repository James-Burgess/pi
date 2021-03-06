import RPi.GPIO as g
from time import sleep
import os

g.setmode(g.BCM)
#Setup Pins
lightList = [4, 17, 18] 
#4 bed #17 bath #18 Lounge
for i in lightList: 
    g.setup(i, g.OUT) 
    g.output(i, g.HIGH)

def main():
	while True:
		try:
			bed_input_state = g.input(4)
			bath_input_state = g.input(17)
			beyond_input_state = g.input(18)

			if bed_input_state == False: bed_state = 'on'
			else: bed_state = 'off'
			if bath_input_state == False: bath_state = 'on'
			else: bath_state = 'off'
			if beyond_input_state == False: beyond_state = 'on'
			else: beyond_state = 'off'

			sleep(1)
			os.system('clear')
			print("bedroom: %s\nBathroom: %s\nBeyond: %s" %(bed_state, bath_state, beyond_state))


		except KeyboardInterrupt:
			print("Outies")
			break

if __name__ == "__main__":
	main()