import subprocess
import zmq
import requests
import urllib2



context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    #  Wait for next request from client
	message = socket.recv()
	print("Received request: %s" % message)
	message = message.split('#')
	ip = message[0]
	art = message[1]
	client = message[2]
	socket.send(b"Style style transfer will begin")
	artImage = urllib2.urlopen('http://'+art)
	clientImage = urllib2.urlopen('http://'+client)
	subprocess.call(["python", "../style-transfer/style.py" ,"-s", artImage, "-c", clientImage, "-m", "googlenet", "-g", "-1"])

    #  Do some 'work'
	#files = {'file': ('picture.jpg',open('/style-transfer/outputs/outputname.jpg', 'rb'))}
	subprocess.call(["ls", "../style-transfer/outputs"])
	#requests.post("http://"+ip+"/uploadimage", files=files)
    #  Send reply back to client


