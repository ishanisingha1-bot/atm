from tkinter import *
root = Tk()
root.title("ATM Pin Interface")
root.geometry("250x350")
display = Label(root, text="", font=("Arial", 16))
display.grid(row=0, column=0, columnspan=3, pady=5)
def press():
  display.config(text=display.cget("text") + "*")
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]
for i in range(4):
  root.columnconfigure(i, weight=1, minsize=75)
  root.rowconfigure(i + 1, weight=1, minsize=50)
  for j in range(0, 3):
    frame = Frame(master=root, relief=SUNKEN, borderwidth=1)
    frame.grid(row=i + 1, column=j)
    btn = Button(master=frame, text=nums[i][j], bg="#d0efff", command=press)
    btn.pack(padx=3, pady=3)

root.mainloop()