import cv2 as cv
import numpy as np
from fun import seq_conv, seq_conv_ppm_to_flif, convert, compare_img, seq_conv_flif_to_ppm, compare_sequences, create_substracted_frames
from matplotlib import pyplot as plt


create_substracted_frames(r".\MOVIES\ppm_sequences\1093662_sequence")
create_substracted_frames(r".\MOVIES\ppm_sequences\1295231_sequence")
create_substracted_frames(r".\MOVIES\ppm_sequences\1550669_sequence")
create_substracted_frames(r".\MOVIES\ppm_sequences\1695733_sequence")
create_substracted_frames(r".\MOVIES\ppm_sequences\busy_city_sequence")
create_substracted_frames(r".\MOVIES\ppm_sequences\hiking_driving_seq")


seq_conv(r".\MOVIES\ppm_sequences\1093662_sequence_diff", ".ppm", ".png")
seq_conv(r".\MOVIES\ppm_sequences\1295231_sequence_diff", ".ppm", ".png")
seq_conv(r".\MOVIES\ppm_sequences\1550669_sequence_diff", ".ppm", ".png")
seq_conv(r".\MOVIES\ppm_sequences\1695733_sequence_diff", ".ppm", ".png")
seq_conv(r".\MOVIES\ppm_sequences\busy_city_sequence_diff", ".ppm", ".png")
seq_conv(r".\MOVIES\ppm_sequences\hiking_driving_seq_diff", ".ppm", ".png")


seq_conv(r".\MOVIES\ppm_sequences\1093662_sequence_diff", ".ppm", ".jp2")
seq_conv(r".\MOVIES\ppm_sequences\1295231_sequence_diff", ".ppm", ".jp2")
seq_conv(r".\MOVIES\ppm_sequences\1550669_sequence_diff", ".ppm", ".jp2")
seq_conv(r".\MOVIES\ppm_sequences\1695733_sequence_diff", ".ppm", ".jp2")
seq_conv(r".\MOVIES\ppm_sequences\busy_city_sequence_diff", ".ppm", ".jp2")
seq_conv(r".\MOVIES\ppm_sequences\hiking_driving_seq_diff", ".ppm", ".jp2")

seq_conv(r".\MOVIES\ppm_sequences\1093662_sequence_diff", ".ppm", ".webp")
seq_conv(r".\MOVIES\ppm_sequences\1295231_sequence_diff", ".ppm", ".webp")
seq_conv(r".\MOVIES\ppm_sequences\1550669_sequence_diff", ".ppm", ".webp")
seq_conv(r".\MOVIES\ppm_sequences\1695733_sequence_diff", ".ppm", ".webp")
seq_conv(r".\MOVIES\ppm_sequences\busy_city_sequence_diff", ".ppm", ".webp")
seq_conv(r".\MOVIES\ppm_sequences\hiking_driving_seq_diff", ".ppm", ".webp")

seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\1093662_sequence_diff")
seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\1295231_sequence_diff")
seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\1550669_sequence_diff")
seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\1695733_sequence_diff")
seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\busy_city_sequence_diff")
seq_conv_ppm_to_flif(r".\MOVIES\ppm_sequences\hiking_driving_seq_diff")

