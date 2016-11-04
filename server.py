import subprocess
import zmq
import requests



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
	clientImage = message[2]
	socket.send(b"Style style transfer will begin")
	subprocess.call(["python", "../style-transfer/style.py" ,"-s", "http://"+art, "-c", "http://"+clientImage, "-m", "googlenet", "-g", "-1"])

    #  Do some 'work'
	#files = {'file': ('picture.jpg',open('/style-transfer/outputs/outputname.jpg', 'rb'))}
	subprocess.call(["ls", "../style-transfer/outputs"])
	#requests.post("http://"+ip+"/uploadimage", files=files)
    #  Send reply back to client


