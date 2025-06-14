import os
import numpy as np
from tqdm import tqdm


if not os.path.exists("product"):
    os.makedirs("product")
folder="E:\\Personal Projects\\Digikala_img_Crawler\\img"
for filename in tqdm(os.listdir(folder)):
    with open(folder+"\\"+filename,'rb') as f:
        file_byte=f.read()
        file_size=len(file_byte)//1024
        if file_size>70 and file_size<90:
            with open(f"product/{filename}",'wb') as fw:
                fw.write(file_byte)
