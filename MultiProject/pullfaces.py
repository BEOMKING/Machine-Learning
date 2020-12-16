from PIL import Image
import face_recognition
import os

path_dir = 'C:/Image/Celebrity/'
categories = ["JangSungGyu", "KangDongWon", "LeeKookJu", "MaDongSuk", "OhDalSoo", "OrangUTan", "RyuJoonYeol"]
for categorie in categories:
    count = 0
    file_list = os.listdir(path_dir + categorie)

    picture_of_me = face_recognition.load_image_file("C:/Image/Celebrity/" + categorie + '/' + "{0}0.jpg".format(categorie))
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    # my_face_encoding은 이제 어느 얼굴과도 비교할 수 있는 내가 가진 얼굴 특징의 보편적인 인코딩을 포함하게 되었습니다.

    for file_name in file_list:
        image = face_recognition.load_image_file(path_dir + categorie + '/' + file_name)
        face_locations = face_recognition.face_locations(image)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            #pil_image.show()
            nowimage = 'C:/Image/Celebrity/Celebrityhead/' + categorie + 'head' + '/' + '{0}{1}.jpg'.format(categorie, count)
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
            # if results[0] == False:
            #     os.remove(nowimage)
            count += 1