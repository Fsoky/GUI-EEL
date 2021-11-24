import eel # pip install eel

eel.init("web")


@eel.expose
def recv_data(login, password):
	print(login, password)


eel.start("index.html", size=(500, 500))