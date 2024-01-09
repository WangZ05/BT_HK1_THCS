danh_sach=[]
while True:
    x=int(input("nhập giá trị x: "))
    danh_sach.append(x)
    tiep_tuc= input("tiếp tục nhập giá trị x? (1:có , 2:không) \n")
    if tiep_tuc == '1':
        continue
    elif tiep_tuc == '2':
        break
s=sum(danh_sach) 
print("tổng các giá trị trong danh sách là: ", s)
gia_tri_muon_tim = int(input("nhập giá trị cần tìm: " ))
print("cho đến hiện tại danh sách gồm: \n", danh_sach)
if gia_tri_muon_tim in danh_sach:
    vi_tri=danh_sach.count(gia_tri_muon_tim)
    print(f"{gia_tri_muon_tim} xuất hiện {vi_tri} lần trong danh sách")
else:
    print(f"{gia_tri_muon_tim} không nằm trong danh sách bạn nhập.")
num_max= max(danh_sach)
if num_max != gia_tri_muon_tim:
    print(f"{gia_tri_muon_tim} không phải số lớn nhất")  
    print(f"các số lớn hơn {gia_tri_muon_tim} là: {[so for so in danh_sach if so > gia_tri_muon_tim]}")  
else:
    print(f"{gia_tri_muon_tim} là số lớn nhất.")