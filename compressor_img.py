from PIL import Image


def cpic(file, outname, i='only'):
	try:
		foo = Image.open(file)  # My image is a 200x374 jpeg that is 102kb large
	 
		if i == 'only':
	 		foo.save(f"compress/{outname}/img_press.jpg", quality=95, optimize=True)  # The saved downsized image size is 24.8kb
		else:
	 		foo.save(f"compress/{outname}/img_{i}_press.jpg", quality=70, optimize=True)
	 	
	finally:
		foo.close()