dssv=[]
def nhapds():
        for i in range(u):
            print(f"Nhập sinh viên thứ {i+1} :")
            masv = input("Nhập mã sinh viên: ")
            ten = input("Nhập tên: ")
            toan = float(input("Nhập điểm toán: "))
            ly = float(input("Nhập điểm lý: "))
            hoa = float(input("Nhập điểm hóa: "))
            diemtb = (toan+ly+hoa) / 3
            if diemtb >= 8:
                hocluc = "Giỏi"
            elif diemtb >= 6.5:
                hocluc = "Khá"
            elif diemtb >= 5:
                hocluc = "Trung bình"
            else:
                hocluc = "Yếu"
            sv={"Mã sinh viên": masv,"Tên": ten,"Điểm toán": toan,
                "Điểm lý": ly,"Điểm hóa": hoa,"Điểm trung bình": diemtb,
                "Học lực": hocluc}
            dssv.append(sv)
def hienthi():
        for sv in dssv:
            print(sv["Mã sinh viên"],"--",
            sv["Tên"],"--",
            sv["Điểm toán"],"--",sv["Điểm lý"],"--",
            sv["Điểm hóa"],"--",sv["Điểm trung bình"],
            "--",sv["Học lực"])
def themsv():
    print("Nhập thông tin sinh viên cần thêm: ")
    masv = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên: ")
    toan = float(input("Nhập điểm toán: "))
    ly = float(input("Nhập điểm lý: "))
    hoa = float(input("Nhập điểm hóa: "))
    diemtb = (toan + ly + hoa) / 3
    if diemtb >= 8:
        hocluc = "Giỏi"
    elif diemtb >= 6.5:
        hocluc = "Khá"
    elif diemtb >= 5:
        hocluc = "Trung bình"
    else:
        hocluc = "Yếu"
    sv = {"Mã sinh viên": masv, "Tên": ten, "Điểm toán": toan,
          "Điểm lý": ly, "Điểm hóa": hoa, "Điểm trung bình": diemtb,
          "Học lực": hocluc}
    dssv.append(sv)
def capnhat(masv):
    for sv in dssv:
        if sv["Mã sinh viên"] == masv:
            sv["Tên"] = input("Nhập tên mới: ")
            sv["Điểm toán"] = float(input("Nhập điểm toán mới: "))
            sv["Điểm lý"] = float(input("Nhập điểm lý mới: "))
            sv["Điểm hóa"] = float(input("Nhập điểm hóa mới: "))
            diemtb = (sv["Điểm toán"] + sv["Điểm lý"] + sv["Điểm hóa"]) / 3
            sv["Điểm trung bình"] = diemtb
            if diemtb >= 8:
                sv["Học lực"] = "Giỏi"
            elif diemtb >= 6.5:
                sv["Học lực"] = "Khá"
            elif diemtb >= 5:
                sv["Học lực"] = "Trung bình"
            else:
                sv["Học lực"] = "Yếu"
            print("Đã cập nhật")
            return
    print("Không tìm thấy")

def xoasv(masv):
    for sv in dssv:
        if sv["Mã sinh viên"] == masv:
            dssv.remove(sv)
            print("Đã xóa!")
            return
    print("Không tìm thấy")
def timkiem(ten):
    for sv in dssv:
        if sv["Tên"] == ten:
            print(sv)
            return
    print("Không tìm thấy")
def sapxepdtb():
    dssv.sort(key=lambda sv: sv["Điểm trung bình"])
def sapxepten():
    dssv.sort(key=lambda sv: sv["Tên"])
def sapxepmasv():
    dssv.sort(key=lambda sv: sv["Mã sinh viên"])
def demsv(tencantim):
    dem = 0
    for sv in dssv:
        if sv["Tên"] == tencantim:
            dem += 1
    return dem

u = int(input("Nhập số lượng sinh viên: "))
nhapds()
print("Danh sách sinh viên ban đầu:")
hienthi()

themsv()
print("Danh sách sau khi thêm:")
hienthi()

masv = input("Nhập mã sinh viên cần cập nhật: ")
capnhat(masv)

print("Danh sách sau khi cập nhật:")
hienthi()

masv = input("Nhập mã sinh viên cần xóa: ")
xoasv(masv)
print("Danh sách sau khi xóa:")
hienthi()

ten = input("Nhập tên sinh viên cần tìm: ")
timkiem(ten)

print("Sắp xếp theo điểm trung bình:")
sapxepdtb()
hienthi()
print("Sắp xếp theo tên:")
sapxepten()
hienthi()
print("Sắp xếp theo mã sinh viên:")
sapxepmasv()
hienthi()

tencantim = input("Nhập tên cần tìm: ")
print("Số sinh viên có tên", tencantim,"là: ",demsv(tencantim))
