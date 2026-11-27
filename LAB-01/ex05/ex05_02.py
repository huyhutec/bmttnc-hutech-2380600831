import re

def tinh_tong_so_nguyen(chuoi):
    # Trích xuất tất cả số nguyên (bao gồm cả số âm có dấu '-' đứng liền trước)
    cac_so = [int(x) for x in re.findall(r'-?\d+', chuoi)]
    tong_duong = sum(x for x in cac_so if x > 0)
    tong_am = sum(x for x in cac_so if x < 0)
    return tong_duong, tong_am

chuoi_nhap = input("Nhập chuỗi: ")
tong_duong, tong_am = tinh_tong_so_nguyen(chuoi_nhap)
print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")