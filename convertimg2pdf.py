# Convert images to PDF
from PIL import Image
import glob
import os
from compressor_img import cpic



def convertimg():
    
    folder = str(input("\t folder : "))
    typefile = str(input("\t tipe gambar : "))
    #quality = int(input("\t kualitas pdf % (1-100) : "))
    output_pdf = os.path.join("output" , folder + ".pdf")
    
    path = folder + f"/*.{typefile}"
    #path2 = f"compress/{folder}_compress"
#    os.makedirs(path2)

    images = glob.glob(path)
    
    print(f"\t Jumlah Gambar: {len(images)}\n \t List Gambar: \n")
	
    for i in images:
    	print("\t - " , i, "\n")
    	
    konfirmasi = input("\t lanjutkan? (Y/n) \n \t")
    
    if konfirmasi == "Y" or "y":
    	print("\t...oke")
    elif konfirmasi == "N" or "n":
    	exit()
    else:
    	exit()
    	
    print("\t Memulai Mengkompres Gambar....")
    #for i in range(0, len(images)):
#    	cpic(images[i], f"{folder}_compress", i)
    
    print("\t Proses Mengkompres Gambar Selesai ✓")
    
    
    #images2 = glob.glob(path2  + f"/*.{typefile}")
    
    pil_images = []

    try:
        print(f"\t ...Membuat File {folder}.pdf")
        for image in images:
            pil_images.append(Image.open(image))

        convert_pil_images = []
        
        print("\t ...Mengkonversi gambar")

        for pil_image in pil_images:
            convert_pil_images.append(pil_image.convert('RGB'))

        image_list = convert_pil_images[1:] 
        
        print("\t ...Gambar Sukses di Convert ke PDF")
        
        print("\t .....")
        
        print("\t Menyimpan")
		
        convert_pil_images[0].save(output_pdf, save_all = True, append_images = image_list)
        print("\t Sukses")
        
        exit = input("Exit (Y/n) ? ")
        
        if exit == "Y" or exit == "y":
        	quit()
        elif exit == "n" or exit == "N":
        	return True
        else:
        	return True
        	
    except Exception as e:
        print('Error: {0}\nException message: {1}'.format(type(e).__name__, e))
        

if __name__ == "__main__":
	while True:
		convertimg()