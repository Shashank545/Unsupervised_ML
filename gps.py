import serial
from math import radians, cos, sin, asin, sqrt

class Gps:
	def __init__(self,port):
		self.port = port
		self.arduino = serial.Serial(self.port,timeout=1,baudrate=9600)

	def getCoordinates(self):
		return(str(self.arduino.readline()))

	def getDistance(self,p1,p2):
		"""
	    Calculate the great circle distance between two points 
	    on the earth (specified in decimal degrees)
	    p1[0],p2[0] = lon1,lon2
	    p1[1],p2[1] = lat1,lat2
	    """
	    # convert decimal degrees to radians 
	    lon1, lat1, lon2, lat2 = map(radians, [p1[0], p1[1], p2[0], p2[1]])

	    # haversine formula 
	    dlon = lon2 - lon1 
	    dlat = lat2 - lat1 
	    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	    c = 2 * asin(sqrt(a)) 
	    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
	    return c * r


try:
	g = Gps("/dev/tty.usbmodem143401")
	# while(True):
	# 	print(g.getCoordinates())

except Exception as e:
	print(e)