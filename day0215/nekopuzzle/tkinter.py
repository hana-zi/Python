import tkinter as tk
	
root=tk.Tk()
root.geometry('700x560')
root['bg']='lightgrey'
#画像用のキャンバス作成
canvas=tk.Canvas(width=640,height=426)
#キャンバスを設置(上下に20の余白)
canvas.pack(pady=20)
#画像を用意
photo1=tk.PhotoImage(file='cat1.png')
#画像を描画(中点x,中点y,画像)
canvas.create_image(320,213,image=photo1)
root.mainloop()
