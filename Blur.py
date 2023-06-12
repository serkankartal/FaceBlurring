import cv2
import os
import face_recognition

def BlurFolder(folder_path):
    # output_file="./Data/blurred_"+folder_path.split("/")[-1]
    output_file=folder_path+"_blurred"
    if not os.path.exists(output_file):
        os.makedirs(output_file)
    filelist=os.listdir(folder_path)

    for img_name in filelist:
        # image = cv2.imread(folder_fath+'/'+img_name)
        image = face_recognition.load_image_file(folder_path+'/'+img_name)
        face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=1, model="cnn")


        # define haar cascade for face detection
        # face_cascade = cv2.CascadeClassifier('./Data/haarcascade_frontalface_alt2.xml')
        # faces = face_cascade.detectMultiScale(image, 1.3, 5)

        # Loop over all the detected faces in the image
        for (top, right, bottom, left) in face_locations:
            roi = image[top:bottom, left:right]

            # apply gaussian blur to face rectangle
            roi = cv2.GaussianBlur(roi, (17, 17), 30)

            # add blurred face on original image to get final image
            image[top:top + roi.shape[0], left:left + roi.shape[1]] = roi

        # for (x, y, w, h) in faces:
        #     roi = image[y:y + h, x:x + w]
        #
        #     # apply gaussian blur to face rectangle
        #     roi = cv2.GaussianBlur(roi, (17, 17), 30)
        #
        #     # add blurred face on original image to get final image
        #     image[y:y + roi.shape[0], x:x + roi.shape[1]] = roi
        # Display the output
        cv2.imwrite(output_file+'/'+img_name, image)

if __name__ == '__main__':
    BlurFolder("./Data/images/")
