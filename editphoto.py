from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter

root = Tk()
root.title("Simple Image Editor")

# Fungsi untuk memuat citra
def open_image():
    global image_pil
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if path:
        image_pil = Image.open(path)
        image_pil.thumbnail((350, 350))
        photo = ImageTk.PhotoImage(image_pil)
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo  # Simpan referensi objek PhotoImage

# Fungsi untuk menerapkan efek filter pada citra
def apply_filter():
    global image_pil
    if image_pil:
        selected_filter = filter_var.get()  # Mendapatkan filter yang dipilih oleh pengguna
        filtered_image = apply_selected_filter(image_pil, selected_filter)
        photo = ImageTk.PhotoImage(filtered_image)
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo  # Simpan referensi objek PhotoImage yang sudah difilter

# Fungsi untuk menerapkan filter yang dipilih
def apply_selected_filter(image, selected_filter):
    if selected_filter == "Blur":
        return image.filter(ImageFilter.BLUR)
    elif selected_filter == "Sharpen":
        return image.filter(ImageFilter.SHARPEN)
    elif selected_filter == "Edge Enhance":
        return image.filter(ImageFilter.EDGE_ENHANCE)
    elif selected_filter == "Emboss":
        return image.filter(ImageFilter.EMBOSS)
    elif selected_filter == "Grayscale":
        return image.convert("L")
    else:
        return image

# Fungsi untuk menyimpan citra yang sudah dimanipulasi
def save_image():
    global image_pil
    if image_pil:
        filtered_image = apply_selected_filter(image_pil, filter_var.get())
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if path:
            filtered_image.save(path)

# Fungsi untuk menyesuaikan ukuran citra
def adjust_resize():
    global image_pil
    if image_pil:
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            image_pil = image_pil.resize((width, height))
            image_pil.thumbnail((350, 350))
            photo = ImageTk.PhotoImage(image_pil)
            canvas.create_image(0, 0, anchor="nw", image=photo)
            canvas.image = photo  # Simpan referensi objek PhotoImage yang sudah diresize
            apply_filter()  # Terapkan filter yang dipilih pada citra yang diresize
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka pada kolom Width dan Height.")

# Fungsi untuk membalik citra
def flip_image():
    global image_pil
    if image_pil:
        image_pil = image_pil.transpose(Image.FLIP_LEFT_RIGHT)
        image_pil.thumbnail((350, 350))
        photo = ImageTk.PhotoImage(image_pil)
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo  # Simpan referensi objek PhotoImage yang sudah dibalik
        apply_filter()  # Terapkan filter yang dipilih pada citra yang dibalik

# Fungsi untuk memutar citra
def rotate_image():
    global image_pil
    if image_pil:
        try:
            rotasi = int(rotasi_entry.get())
            image_pil = image_pil.rotate(rotasi)
            image_pil.thumbnail((350, 350))
            photo = ImageTk.PhotoImage(image_pil)
            canvas.create_image(0, 0, anchor="nw", image=photo)
            canvas.image = photo  # Simpan referensi objek PhotoImage yang sudah dirotasi
            apply_filter()  # Terapkan filter yang dipilih pada citra yang dirotasi
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka pada kolom Rotasi.")

# Membuat tombol dan canvas
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

# Tambahkan filter yang tersedia dalam list
filters = ["None", "Blur", "Sharpen", "Edge Enhance", "Emboss", "Grayscale"]
filter_var = StringVar()
filter_var.set(filters[0])  # Set filter awal menjadi "None"

filter_label = Label(root, text="Filter:")
filter_label.pack()

filter_menu = OptionMenu(root, filter_var, *filters)
filter_menu.pack()

apply_button = Button(root, text="Apply Filter", command=apply_filter)
apply_button.pack()

# Tambahkan widget dan tombol untuk adjust resize
resize_frame = Frame(root)
resize_frame.pack(pady=10)

width_label = Label(resize_frame, text="Width:")
width_label.pack(side=LEFT)

width_entry = Entry(resize_frame)
width_entry.pack(side=LEFT)

height_label = Label(resize_frame, text="Height:")
height_label.pack(side=LEFT)

height_entry = Entry(resize_frame)
height_entry.pack(side=LEFT)

resize_button = Button(resize_frame, text="Resize", command=adjust_resize)
resize_button.pack(side=LEFT)

# Tambahkan tombol untuk flip
flip_button = Button(root, text="Flip", command=flip_image)
flip_button.pack()

# Tambahkan tombol dan widget untuk rotate
rotate_frame = Frame(root)
rotate_frame.pack(pady=10)

rotasi_label = Label(rotate_frame, text="Rotasi:")
rotasi_label.pack(side=LEFT)

rotasi_entry = Entry(rotate_frame)
rotasi_entry.pack(side=LEFT)

rotate_button = Button(rotate_frame, text="Rotate", command=rotate_image)
rotate_button.pack(side=LEFT)

# Tambahkan tombol untuk menyimpan citra
save_button = Button(root, text="Save Image", command=save_image)
save_button.pack()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()
