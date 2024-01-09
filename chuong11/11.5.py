danh_sach=[]
while True:
    x=int(input("nhập giá trị x: "))
    danh_sach.append(x)
    tiep_tuc= input("tiếp tục nhập giá trị x? (1:có , 2:không) \n")
    if tiep_tuc == '1':
        continue
    elif tiep_tuc == '2':
        break
print("list:", danh_sach)

def la_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
so_nguyen_to = [so for so in danh_sach if la_so_nguyen_to(so)]
print(f"Các số nguyên tố trong danh sách là: {so_nguyen_to}")

so_am = [so for so in danh_sach if so < 0]
trung_binh_so_am = sum(so_am) / len(so_am) if so_am else 0
print(f"trung bình cộng các phần tử âm: {trung_binh_so_am}")

so_duong = [so for so in danh_sach if so >= 0]
trung_binh_so_duong = sum(so_duong) / len(so_duong) if so_duong else 0
print(f"trung bình cộng các phần tử dương: {trung_binh_so_duong}")

lon_nhat = max(danh_sach)
print("giá trị max trong list là:", lon_nhat)
nho_nhat = min(danh_sach)
print("giá trị min trong list là:", nho_nhat)

sap_xep=sorted(danh_sach )
print("thứ tự tăng dần trong list là:",sap_xep)