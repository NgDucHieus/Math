# import cv2  

# # Đọc ảnh màu từ file  
# image = cv2.imread("original.jpg")  

# # Chuyển đổi sang grayscale  
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

# # Hiển thị ảnh grayscale  
# cv2.imshow("Grayscale Image", gray_image)  
# cv2.waitKey(0)  # Chờ nhấn phím để đóng cửa sổ  
# cv2.destroyAllWindows()  

# # Lưu ảnh grayscale  
# cv2.imwrite("gray_image.jpg", gray_image)  

# print(gray_image)

import numpy as np  
import matplotlib.pyplot as plt  

# Dữ liệu pixel  
pixel_data = [  
    [148, 123,  52, 107, 123, 162, 172, 123,  64,  89],  
    [147, 130,  92,  95,  98, 130, 171, 155, 169, 163],  
    [141, 118, 121, 148, 117, 107, 144, 137, 136, 134],  
    [ 82, 106,  93, 172, 149, 131, 138, 114, 113, 129],  
    [ 57, 101,  72,  54, 109, 111, 104, 135, 106, 125],  
    [138, 135, 114,  82, 121, 110,  34,  76, 101, 111],  
    [138, 102, 128, 159, 168, 147, 116, 129, 124, 117],  
    [113,  89,  89, 109, 106, 126, 114, 150, 164, 145],  
    [120, 121, 123,  87,  85,  70, 119,  64,  79, 127],  
    [145, 141, 143, 134, 111, 124, 117, 113,  64, 112]  
]  

# Tạo figure và axis  
fig, ax = plt.subplots(figsize=(12, 6))  
ax.axis('off')  # Ẩn trục  

# Vẽ bảng  
table = ax.table(  
    cellText=pixel_data,  
    loc="center",  
    cellLoc="center",  
    edges="open"  # Không hiển thị đường viền mặc định  
)  

# Định dạng bảng:  
# 1. Ẩn tất cả đường viền  
for key, cell in table.get_celld().items():  
    cell.set_linewidth(0)  

# 2. Vẽ viền bao quanh toàn bộ ma trận  
# Xác định số hàng và số cột  
num_rows = len(pixel_data)  
num_cols = len(pixel_data[0])  

# Vẽ viền cho các ô ở rìa:  
for row in range(num_rows):  
    for col in range(num_cols):  
        cell = table[row, col]  
        # Viền trên cùng  
        if row == 0:  
            cell.set_edgecolor('black')  
            cell.set_linewidth(1)  
        # Viền dưới cùng  
        if row == num_rows - 1:  
            cell.set_edgecolor('black')  
            cell.set_linewidth(1)  
        # Viền trái (cột đầu tiên)  
        if col == 0:  
            cell.set_edgecolor('black')  
            cell.set_linewidth(1)  
        # Viền phải (cột cuối cùng)  
        if col == num_cols - 1:  
            cell.set_edgecolor('black')  
            cell.set_linewidth(1)  

# Thêm tiêu đề  
plt.title("Ma trận pixel với viền bao quanh", pad=20, fontsize=14)  

# Hiển thị  
plt.show()      