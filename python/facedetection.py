from PIL import Image
import face_recoginition

# laod the jpg file into tmupy array
image = face_recoginition.load_image_file('office.jpg')

# 
face_locations = face_recoginition.face_locations(image)

for face_location in face_locations:

    top,right,bottom,left = face_location

    face_image = image[top:bottom, left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.show()