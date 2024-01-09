list_chieu_cao = [74,74,72,72,73,69,69,71,76,71]

ba_chieu_cao_dau_tien = list_chieu_cao[0:3]
ba_chieu_cao_cuoi_cung = list_chieu_cao[-3:]
print(ba_chieu_cao_dau_tien,ba_chieu_cao_cuoi_cung)

ty_le_chuyen_doi = 0.0254
chieu_cao_met = [round(chieu_cao * ty_le_chuyen_doi, 2) for chieu_cao in list_chieu_cao]
print(chieu_cao_met)

tb = sum(chieu_cao_met)/len(chieu_cao_met)
print(tb)
print(max(chieu_cao_met))
print(min(chieu_cao_met))

chieu_cao_met.sort()
print(chieu_cao_met)

chieu_cao_met.sort()
chieu_cao_met.reverse()
print(chieu_cao_met)