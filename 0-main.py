import tkinter as tk

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Hello, TK")
		self.labeltxt = tk.StringVar()
		self.labeltxt.set("Click my buttons")
		label = tk.Label(self, textvariable=self.labeltxt)
		label.pack(fill=tk.BOTH, expand=True, padx=100, pady=50)

		hellobtn = tk.Button(self, text="Say Hello", command=self.sayhello)
		hellobtn.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

		byebtn = tk.Button(self, text="Say Bye", command=self.saybye)
		byebtn.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

	def sayhello(self):
		self.labeltxt.set("You clicked Hello")
		print(self.labeltxt.get())
		self.after(2000, self.labeltxt.set, "Click my buttons")
		# self.after(2000, self.labeltxt.set("Click my buttons"))

	def saybye(self):
		self.labeltxt.set("Closing in 2 seconds")
		print(self.labeltxt.get())
		self.after(2000, self.destroy)

if __name__ == "__main__":
	win = Window()
	win.mainloop()
# class Window(tk.Tk):
# 	def __init__(self):
# 		super().__init__()
# 		self.title("Hello Tkinter")
# 		self.label_text = "Choose One"
# 		self.label = tk.Label(self, text=self.label_text)
# 		self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)
# 		hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
# 		hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
# 		goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
# 		goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
# 	def say_hello(self):
# 		self.label_text = "Hello World"
# 	def say_goodbye(self):
# 		self.label_text="Goodbye! \n (Closing in 2 seconds)"
# 		self.after(2000, self.destroy)
# if __name__ == "__main__":
# 	window = Window()
# 	window.mainloop()