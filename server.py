import subprocess
import zmq
import requests
import os


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
	subprocess.call(["python", "../style-transfer/style.py" ,"-s", "http://"+art, "-c", "http://"+ip+ "/contentuploads/" +clientImage, "-m", "googlenet", "-g", "-1"])

    #  Do some 'work'
	list = os.listdir("../style-transfer/outputs/")
	files = {'file': (clientImage+'.jpg',open('../style-transfer/outputs/'+list[0], 'rb'))}
	requests.post("http://"+ip+"/uploadresult", files=files)
	os.remove('../style-transfer/outputs/'+list[0])
    #  Send reply back to client


