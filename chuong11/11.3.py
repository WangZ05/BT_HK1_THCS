danh_sach_dv = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("list of animals:",danh_sach_dv)
print(f"danh sách có {len(danh_sach_dv)} con vật")
thu_can_tim = input("tôi muốn tìm: ")
vi_tri = danh_sach_dv.index(thu_can_tim)+1
if thu_can_tim in danh_sach_dv:
    print(f"{thu_can_tim} được tìm thấy và ở vị trí thứ {vi_tri} trong danh sách.")
else:
    print(f"{thu_can_tim} không được tìm thấy trong danh sách.")