import os
import cv2
import dlib
import shutil
import openface
from PIL import Image
import face_recognition
import os

print("Start program")

print("Model loading...")

# embedding을 해 주는 신경망이 저장된 경로
predictor_model = "C:/Users/student/~/openface/models/dlib/shape_predictor_68_face_landmarks.dat"

# dlib 내장 얼굴 인식용 Hog Face Detector
face_detector = dlib.get_frontal_face_detector()

# 얼굴의 자세를 인식하고 보정해줄 aligner
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

print("Model loading finished.\n")


# 주어진 이미지에서 얼굴을 추출해서 정렬한 후 반환함.
# img는 얼굴을 추출할 이미지, img_dim은 정렬된 이미지(정사각형)의 한 변의 길이.
def align_face(img, img_dim):
    # 이미지가 None이 아닌지 체크
    assert img is not None

    detected_faces = face_detector(img, 1)

    # 주어진 이미지에서 얼굴이 1개가 맞는지 체크
    assert len(detected_faces) is 1

    face_rect = detected_faces[0]

    # 얼굴의 포즈를 가져 와서 정렬함. 그런데 첫 번째의 534가 뭔지는 저도 잘 모르겠습니다.
    aligned_face = face_aligner.align(534, img, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    # 이미지를 사이즈에 맞게 바꿈.
    aligned_face = cv2.resize(aligned_face, (img_dim, img_dim))

    return aligned_face


# 주어진 디렉토리의 모든 이미지를 정렬하여 저장함.
def align_face_dir(dir, img_dim):
    # 저장할 디렉토리 경로를 생성함. 원래 폴더의 이름+aligned를 하여, 실행 파일이 포함된 경로에 저장.
    # 함수를 실행하면 자동으로 경로를 알려줌.
    print("Start the image alignment.")
    path = os.path.split(dir)
    save_path = path[0] + "/" + path[len(path) - 1] + "_aligned"
    print("Aligned image will be saved at", save_path)

    # 만약 이미 그런 경로가 존재할 경우, 경로를 싹 지워버리고 새로 만듬.
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    else:
        os.mkdir(save_path)

    # 전체 이미지 개수
    count_all = 0
    # 그 중에서 오류 없이 처리한 개수
    count_processed = 0

    for file in os.listdir(dir):
        count_all += 1
        image = cv2.imread(os.path.join(dir, file))
        try:
            aligned = align_face(image, img_dim)
            cv2.imwrite(os.path.join(save_path, file), aligned)
            count_processed += 1
        except AssertionError:
            print("Image processing error :", file)

    # 전체 몇 개 중에서 몇 개가 변환되었는지 출력함.
    print(count_processed, "out of", count_all, "image aligned.\n")