import cv2 as cv
import numpy as np
from fun import seq_conv, seq_conv_ppm_to_flif, convert, compare_img, seq_conv_flif_to_ppm, compare_sequences
from matplotlib import pyplot as plt
import time

# ppm to webp
t1 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\1093662_sequence", ".ppm", ".webp")
t2 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\1295231_sequence", ".ppm", ".webp")
t3 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\1550669_sequence", ".ppm", ".webp")
t4 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\1695733_sequence", ".ppm", ".webp")
t5 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\busy_city_sequence", ".ppm", ".webp")
t6 = time.time()
seq_conv(r".\MOVIES\ppm_sequences\hiking_driving_seq", ".ppm", ".webp")
t7 = time.time()

print("compression times[s]:")
print("1093662: ", t2-t1)
print("1295231: ", t3-t2)
print("1550669: ", t4-t3)
print("1695733: ", t5-t4)
print("busy_city: ", t6-t5)
print("hiking_driving: ", t7-t6)
