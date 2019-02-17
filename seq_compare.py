import cv2 as cv
import numpy as np
from fun import seq_conv, seq_conv_ppm_to_flif, convert, compare_img, seq_conv_flif_to_ppm, compare_sequences
from matplotlib import pyplot as plt

# compare ppm to png
compare_sequences(r".\MOVIES\ppm_sequences\1093662_sequence", r".\MOVIES\png_sequences\1093662_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1295231_sequence", r".\MOVIES\png_sequences\1295231_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1550669_sequence", r".\MOVIES\png_sequences\1550669_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1695733_sequence", r".\MOVIES\png_sequences\1695733_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\busy_city_sequence", r".\MOVIES\png_sequences\busy_city_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\hiking_driving_seq", r".\MOVIES\png_sequences\hiking_driving_seq")

# compare ppm to jp2
compare_sequences(r".\MOVIES\ppm_sequences\1093662_sequence", r".\MOVIES\jp2_sequences\1093662_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1295231_sequence", r".\MOVIES\jp2_sequences\1295231_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1550669_sequence", r".\MOVIES\jp2_sequences\1550669_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1695733_sequence", r".\MOVIES\jp2_sequences\1695733_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\busy_city_sequence", r".\MOVIES\jp2_sequences\busy_city_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\hiking_driving_seq", r".\MOVIES\jp2_sequences\hiking_driving_seq")

# compare ppm to webp
compare_sequences(r".\MOVIES\ppm_sequences\1093662_sequence", r".\MOVIES\WebP_sequences\1093662_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1295231_sequence", r".\MOVIES\WebP_sequences\1295231_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1550669_sequence", r".\MOVIES\WebP_sequences\1550669_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1695733_sequence", r".\MOVIES\WebP_sequences\1695733_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\busy_city_sequence", r".\MOVIES\WebP_sequences\busy_city_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\hiking_driving_seq", r".\MOVIES\WebP_sequences\hiking_driving_seq")

#compare ppm to flif (using flif to ppm conversion)
compare_sequences(r".\MOVIES\ppm_sequences\1093662_sequence", r".\MOVIES\ppm_from_flif\1093662_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1295231_sequence", r".\MOVIES\ppm_from_flif\1295231_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1550669_sequence", r".\MOVIES\ppm_from_flif\1550669_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\1695733_sequence", r".\MOVIES\ppm_from_flif\1695733_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\busy_city_sequence", r".\MOVIES\ppm_from_flif\busy_city_sequence")
compare_sequences(r".\MOVIES\ppm_sequences\hiking_driving_seq", r".\MOVIES\ppm_from_flif\hiking_driving_seq")
