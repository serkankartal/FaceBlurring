# FaceBlurring

- Set the folder path where you want to apply the face blur in the Folder4Blurring variable in main.
- Run the main file
- Output images will be saved in the file created with the "_blurred" extension in the same directory as the input folder.
- If necessary, the sensitivity of the face detection algorithm can be adjusted by changing the value of the tolerance variable in the face_recognition library.
- If you want to make the face area green instead of blurring it, set the value of the make_facearea_green parameter to 1 as in the example below.
- BlurFolder(Folder4Blurring,blurring_size=50,make_facearea_green=1)
