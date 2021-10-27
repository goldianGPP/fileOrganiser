import tkinter as tk
from tkinter import filedialog, Text
import os
import shutil
from os import listdir
from os.path import isfile, join
from timeit import default_timer as timer
from datetime import timedelta

start = None
log = None
h = None
v = None
# D:\project\PYTHON\fileOrganizer

def mk_dir(path,dir_name):
	if not os.path.exists(path+"/"+dir_name):
		os.mkdir(path+"/"+dir_name)
		print_log(str(timedelta(seconds=timer()-start))+" directory : "+path+"/"+dir_name+" created")
	else:
		print_log(str(timedelta(seconds=timer()-start))+" directory : "+path+"/"+dir_name+" existed")

def f_move(path,dir_name,name):
	shutil.move(path+"/"+name, path+"/"+dir_name+"/"+name)
	print_log(str(timedelta(seconds=timer()-start))+" file : "+path+"/"+name+" moved to "+path+"/"+dir_name+"/"+name)

def file_ext(f_name):
	if f_name.lower().endswith(('.png','.jpg','.jpeg')):
		return "Image"
	elif f_name.lower().endswith(('.mp3')):
		return "Music"
	elif f_name.lower().endswith(('.mp4','.webm')):
		return "Video"
	elif f_name.lower().endswith(('.7z','.rar','.zip')):
		return "Compressed"
	elif f_name.lower().endswith(('.pdf','.csv','.xls','.xlsx','.doc','.docx')):
		return "Document"
	elif f_name.lower().endswith(('.txt')):
		return "Text"
	else:
		return "Other"

def organize():
	for widget in fr_log.winfo_children():
		widget.destroy()

	create_log()
	global start
	start = timer()
	path = entry.get()
	print_log(str(timedelta(seconds=timer()-start))+" scanning : "+path)
	onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
	print_log(str(timedelta(seconds=timer()-start))+" files : tracked")

	for f_name in onlyfiles:
		dir_name = file_ext(f_name)
		mk_dir(path,dir_name)
		f_move(path,dir_name,f_name)
	print_log("successed in time : "+str(timedelta(seconds=timer()-start)))
	log.pack(side=tk.TOP, fill=tk.X)
	h.config(command=log.xview)
	v.config(command=log.yview)

def print_log(txt_log):
	log.insert(tk.END,txt_log+"\n")

def create_log():
	global log, h, v
	h = tk.Scrollbar(fr_log, orient = 'horizontal')
	h.pack(side=tk.BOTTOM, fill=tk.X)
	v = tk.Scrollbar(fr_log)
	v.pack(side=tk.RIGHT, fill=tk.Y)

	log = tk.Text(
		fr_log, width=600, wrap=tk.NONE,
		xscrollcommand=h.set, yscrollcommand=v.set
	)

root = tk.Tk()
canvas = tk.Canvas(root, height=300, width=700, bg="#000000");
canvas.pack();

frame = tk.Frame(canvas, bg="#4d4d4d")
frame.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.1)

fr_log = tk.Frame(canvas, bg="#d9d9d9")
fr_log.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.53)

title = tk.Label(frame, text="Welcome to fileOrganizer", bg="#636363", width=700)
title.place(relwidth=1)

label = tk.Label(frame, text="puth dir path down her e.i C:/myfolder", bg="#757575", width=700)
label.place(relwidth=0.8, relx=0.1, rely=0.3)

entry = tk.Entry(frame, width=700) 
entry.place(relwidth=0.8, relx=0.1, rely=0.5)

exe = tk.Button(
	frame, text="execute", 
	padx=10, pady=5, 
	fg="white", bg="#333333",
	command=organize
)
exe.place(relwidth=0.1, relx=0.45, rely=0.7)

root.mainloop();






