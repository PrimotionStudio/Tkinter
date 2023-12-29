import tkinter as tk
import tkinter.messagebox as mb

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Message Box Example")

		self.labeltxt = tk.StringVar()
		self.labeltxt.set("Whats your name?")
		label = tk.Label(self, textvar=self.labeltxt)
		label.pack(fill=tk.BOTH, expand=True)

		self.namevar = tk.StringVar()
		nametextbox = tk.Entry(self, textvar=self.namevar)
		nametextbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

		hellobtn = tk.Button(self, text="Reveal Name", command=self.sayhello)
		hellobtn.pack(side=tk.LEFT, padx=(10, 1), pady=(10, 5))

		byebtn = tk.Button(self, text="Say Bye", command=self.saybye)
		byebtn.pack(side=tk.RIGHT, padx=(1, 10), pady=(10, 5))

	def sayhello(self):
		self.labeltxt.set("Hey, "+self.namevar.get())
		self.after(2000, self.labeltxt.set, "What's your name?")

	def saybye(self):
		self.labeltxt.set("Bye, "+self.namevar.get())
		self.after(2000, self.destroy)

if __name__ == "__main__":
	win = Window()
	win.mainloop()