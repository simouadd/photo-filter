import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageTk

def ouvrir_image():
    """Permet à l'utilisateur de sélectionner une image et l'affiche."""
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    global img_original
    img_original = Image.open(filepath)
    img_tk = ImageTk.PhotoImage(img_original)
    canvas.config(width=img_tk.width(), height=img_tk.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # Garder une référence.


def appliquer_filtre():
    """Applique le filtre sélectionné à l'image."""
    if img_original is None:
        return
    filtre = combo_filtres.get()
    if filtre == 'Noir et Blanc':
        img_filtree = img_original.convert('L')
    elif filtre == 'Flou':
        img_filtree = img_original.filter(ImageFilter.BLUR)
    elif filtre == 'Contour':
        img_filtree = img_original.filter(ImageFilter.CONTOUR)
    elif filtre == 'Emboss':
        img_filtree = img_original.filter(ImageFilter.EMBOSS)
    elif filtre == 'Sharpen':
        img_filtree = img_original.filter(ImageFilter.SHARPEN)
    elif filtre == 'Smooth':
        img_filtree = img_original.filter(ImageFilter.SMOOTH)
    elif filtre == 'Edge Enhance':
        img_filtree = img_original.filter(ImageFilter.EDGE_ENHANCE)
    elif filtre == 'Edge Enhance More':
        img_filtree = img_original.filter(ImageFilter.EDGE_ENHANCE_MORE)
    else:
        img_filtree = img_original

    img_tk = ImageTk.PhotoImage(img_filtree)
    canvas.config(width=img_tk.width(), height=img_tk.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # Garder une référence.


# Initialisation de l'interface graphique
root = tk.Tk()
root.title("Application de Filtres d'Image")

# Widgets
btn_ouvrir = tk.Button(root, text="Ouvrir une image", command=ouvrir_image)
btn_ouvrir.pack()

options_filtres = ['Noir et Blanc', 'Flou', 'Contour', 'Emboss', 'Sharpen', 'Smooth', 'Edge Enhance', 'Edge Enhance More']
combo_filtres = tk.StringVar(root)
combo_filtres.set(options_filtres[0])
dropdown = tk.OptionMenu(root, combo_filtres, *options_filtres)
dropdown.pack()

btn_appliquer = tk.Button(root, text="Appliquer le filtre", command=appliquer_filtre)
btn_appliquer.pack()

canvas = tk.Canvas(root)
canvas.pack()

img_original = None

root.mainloop()

