from PIL import Image


def cpic(file, outname, i='only'):
	try:
		foo = Image.open(file)  # Gambar yg asalnya 200x374 jpeg dengan ukuran 102kb, gede cuy
	 
		if i == 'only':
	 		foo.save(f"compress/{outname}/img_press.jpg", quality=95, optimize=True)  # Jadi 24.8kb
		else:
	 		foo.save(f"compress/{outname}/img_{i}_press.jpg", quality=70, optimize=True)
	 	
	finally:
		foo.close()