import cv2 as cv
import glob
import os



def convert(input, output):
    im_read = cv.imread(input)
    cv.imwrite(output, im_read)


def seq_conv(folder_path, input_format, output_format):
    filenames = glob.glob(folder_path + "\*")
    for i in range(0, len(filenames)):
        convert(filenames[i], filenames[i].strip(input_format) + output_format)


def seq_conv_ppm_to_flif(folder_path):
    filenames = glob.glob(folder_path + "\*")
    for i in range(0, len(filenames)):
        os.system(r".\FLIF-master\build\MSVC\flif.exe " + filenames[i] + " " + filenames[i].strip(".ppm") + ".flif")


def seq_conv_flif_to_ppm(folder_path):
    filenames = glob.glob(folder_path + "\*")
    for i in range(0, len(filenames)):
        os.system(r".\FLIF-master\build\MSVC\flif.exe " + filenames[i] + " " + filenames[i].strip(".flif") + ".ppm")


def compare_img(img1, img2):
    im1 = cv.imread(img1)
    im2 = cv.imread(img2)

    if im1.shape == im2.shape:
        #print("Same shape...")
        diff = cv.subtract(im1, im2)
        b, g, r = cv.split(diff)

        if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
            # print("equal")
            return True
        else:
            # print("not equal")
            return False
    else:
        # print("not equal")
        return False


def compare_sequences(folder_1, folder_2):
    filenames1 = glob.glob(folder_1 + "\*")
    filenames2 = glob.glob(folder_2 + "\*")
    status = True
    if len(filenames1) == len(filenames2):
        for i in range(0, len(filenames1)):
            status = status and compare_img(filenames1[i], filenames2[i])

        if status:
            print(folder_2 + ": SEQ_EQUAL")
        else:
            print(folder_2 + ": NOT_EQUAL!!!")
    else:
        print(folder_2 + ": NOT_EQUAL!!!")


def create_substracted_frames(folder_path):
    filenames = glob.glob(folder_path + "\*")

    print(filenames)

    for i in range(0, len(filenames)-1):
        diff = cv.subtract(cv.imread(filenames[i+1]), cv.imread(filenames[i]))
        cv.imwrite(folder_path + "\img_diff" + str(i) + ".ppm", diff)
