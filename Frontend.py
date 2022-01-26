import tkinter as tk

window = tk.Tk()

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 0, 0]
]

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=100)
    window.rowconfigure(i, weight=1, minsize=100)

    for j in range(0, 3):
        frame = tk.Button(master=window, relief=tk.RAISED, borderwidth=5)
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=nums[i][j])
        label.pack(padx=20, pady=15)


window.mainloop()