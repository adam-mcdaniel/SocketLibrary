from client import *

class GameClient(Client):
	def run(self, worker):
		while True:
			if worker == 0:
				data, _ = self.receive()
				new_data = diff(data, new_data)

				for i in self.new_data.values():
					print(str(i[0]))

				new_data = data

			if worker == 1:
				self.send(("{}".format(input()), time.time()))

			print(worker)

c = GameClient("127.0.0.1", 7005)
# c = Client("127.0.0.1", 7005)