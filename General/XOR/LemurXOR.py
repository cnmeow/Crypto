import cv2
img1 = cv2.imread('/content/flag_7ae18c704272532658c10b5faad06d74.png', cv2.IMREAD_UNCHANGED) # Ảnh 1
img2 = cv2.imread('/content/lemur_ed66878c338e662d3473f0d98eedbd0d.png', cv2.IMREAD_UNCHANGED) # Ảnh 2
xorImg = cv2.bitwise_xor(img1, img2) # XOR 2 ảnh
cv2_imshow(xorImg) # Show ảnh đã XOR
