import os
import cv2
import dlib
import shutil
import openface
from PIL import Image
import face_recognition
import os

def classify_diff_picture(path_dir):
    count = 0
    # print(categorie)
    categorie = os.path.split(path_dir)[1]

    picture_of_me = face_recognition.load_image_file(path_dir + '_aligned' + '/' + "Basic.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    for file_name in os.listdir(path_dir + '_aligned'):
        image = face_recognition.load_image_file(path_dir + '_aligned' + '/' + file_name)
        face_locations = face_recognition.face_locations(image)
        print(face_locations)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            # pil_image.show()
            nowimage = path_dir + '_head' + '/' + '{0}_{1}.jpg'.format(categorie, count)
            pil_image.save(nowimage)
            unknown_picture = face_recognition.load_image_file(nowimage)
            try:
                unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
            except:
                os.remove(nowimage)
                continue
                # 이제 `compare_faces`를 통해 두 얼굴이 같은 얼굴인지 비교할 수 있습니다!
            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
            print(results)

            if results[0] == False:
                os.remove(nowimage)
            count += 1


path_dir = 'C:/Users/student/Desktop/Raw_data_2'

for categorie in os.listdir(path_dir):
    print(categorie)
    align_face_dir(path_dir + '/' + categorie, 96)
    os.mkdir(path_dir + '/' + categorie + '_head')
    classify_diff_picture(path_dir + '/' + categorie)