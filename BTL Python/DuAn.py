# Nhập mô-đun os
# Mô-đun os cung cấp một cách để tương tác với hệ điều hành.
# Nó cho phép bạn thực hiện nhiều hoạt động khác nhau như thao tác tệp và thư mục, quản lý quy trình, v.v.
# Trong trường hợp này, mô-đun os đang được nhập để sử dụng các chức năng của nó cho các hoạt động liên quan đến tệp.
# Không có mã nào khác trong phần lựa chọn được cung cấp.
# Ở trong bài này thì mình dùng để xoá một dự án theo tên file.
import os

class DuAn:
    def __init__(self, maDuAn, tenDuAn, nguonVon):
        # init Khởi tạo một đối tượng đại diện cho một dự án.
        #self được sử dụng để truy cập vào tên, tuổi và lớp của đối tượng
        self.maDuAn = maDuAn  # Mã duy nhất của dự án
        self.tenDuAn = tenDuAn  # Tên của dự án
        self.nguonVon = nguonVon  # Nguồn vốn cho dự án
        self.next = None # Khởi tạo con trỏ next bằng None, cho biết dự án này chưa có dự án kế tiếp
    
class QuanLyDuAn:
    def __init__(self):
        self.head = None

    def hienThiDanhSach(self):
        temp = self.head
        while temp:
            print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def xoaTheoTenFile(self, filename):
        temp = self.head
        prev = None

        while temp:
            if temp.tenDuAn == filename:
                if not prev:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                toDelete = temp
                temp = temp.next
                del toDelete
            try:
                os.remove(filename)
                print("File", filename, "Da bi xoa.")
            except FileNotFoundError:
                print("File", filename, "Khong tim thay.")
            return
        else:
            prev = temp
            temp = temp.next

        print("Khong thay tep nao ten nhu vay", filename, "Tao.")

    def taoMoiFileData(self, filename):
        with open(filename, "w") as outFile:
            outFile.write("")

    def themVaoDau(self, duAn):
        duAn.next = self.head
        self.head = duAn

    def themVaoCuoi(self, duAn):
        if not self.head:
            self.head = duAn
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = duAn

    def xoaTheoMa(self, maDuAn):
        temp = self.head
        prev = None

        while temp and temp.maDuAn != maDuAn:
            prev = temp
            temp = temp.next

        if not temp:
            return

        if not prev:
            self.head = temp.next
        else:
            prev.next = temp.next

    def xoaTheoTen(self, tenDuAn):
        temp = self.head
        prev = None

        while temp and temp.tenDuAn != tenDuAn:
            prev = temp
            temp = temp.next

        if not temp:
            return

        if not prev:
            self.head = temp.next
        else:
            prev.next = temp.next

    def xoaTheoVon(self, nguonVon):
        temp = self.head
        prev = None

        while temp: 
            if temp.nguonVon < nguonVon:
                if not prev:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                toDelete = temp
                temp = temp.next
                del toDelete
            else:
                prev = temp
                temp = temp.next

    def demDuAn(self, nguonVon):
        count = 0
        temp = self.head
        while temp:
            if temp.nguonVon < nguonVon:
                count += 1
            temp = temp.next
        return count

    def timKiemTheoMa(self, maDuAn):
        temp = self.head
        while temp:
            if temp.maDuAn == maDuAn:
                return temp
            temp = temp.next
        return None

    def timKiemTheoTen(self, tenDuAn):
        temp = self.head
        while temp:
            if temp.tenDuAn == tenDuAn:
                return temp
            temp = temp.next
        return None

    def timKiemTheoVon(self, nguonVon):
        temp = self.head
        while temp:
            if temp.nguonVon == nguonVon:
                return temp
            temp = temp.next
        return None

    def hienThiTheoKhoangVon(self, minVon, maxVon):
        temp = self.head
        while temp:
            if temp.nguonVon >= minVon and temp.nguonVon <= maxVon:
                print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def duAnCoVonLonNhat(self):
        if not self.head:
            return None

        maxDuAn = self.head
        temp = self.head.next

        while temp:
            if temp.nguonVon > maxDuAn.nguonVon:
                maxDuAn = temp
            temp = temp.next

        return maxDuAn

    def duAnCoVonNhoNhat(self):
        if not self.head:
            return None

        minDuAn = self.head
        temp = self.head.next

        while temp:
            if temp.nguonVon < minDuAn.nguonVon:
                minDuAn = temp
            temp = temp.next

        return minDuAn

    def hienThiMaDuAnLe(self):
        temp = self.head
        while temp:
            if temp.maDuAn % 2 != 0:
                print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def hienThiMaDuAnChan(self):
        temp = self.head
        while temp:
            if temp.maDuAn % 2 == 0:
                print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def hienThiVonLe(self):
        temp = self.head
        while temp:
            if int(temp.nguonVon) % 2 != 0:
                print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def hienThiVonChan(self):
        temp = self.head
        while temp:
            if int(temp.nguonVon) % 2 == 0:
                print("Ma du an:", temp.maDuAn, ", Ten du an:", temp.tenDuAn, ", Nguon von:", temp.nguonVon)
            temp = temp.next

    def ghiDanhSachVaoTep(self, filename):
        with open(filename, "w") as outFile:
            temp = self.head
            while temp:
                outFile.write(str(temp.maDuAn) + "\n")
                outFile.write(temp.tenDuAn + "\n")
                outFile.write(str(temp.nguonVon) + "\n")
                temp = temp.next

    def tinhVonTrungBinh(self):
        if not self.head:
            return 0.0

        tongVon = 0.0
        soLuong = 0
        temp = self.head

        while temp:
            tongVon += temp.nguonVon
            soLuong += 1
            temp = temp.next

        return tongVon / soLuong

    def sapXepTangDan(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.nguonVon > temp.next.nguonVon:
                    temp.maDuAn, temp.next.maDuAn = temp.next.maDuAn, temp.maDuAn
                    temp.tenDuAn, temp.next.tenDuAn = temp.next.tenDuAn, temp.tenDuAn
                    temp.nguonVon, temp.next.nguonVon = temp.next.nguonVon, temp.nguonVon
                    swapped = True
                temp = temp.next

    def sapXepGiamDan(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.nguonVon < temp.next.nguonVon:
                    temp.maDuAn, temp.next.maDuAn = temp.next.maDuAn, temp.maDuAn
                    temp.tenDuAn, temp.next.tenDuAn = temp.next.tenDuAn, temp.tenDuAn
                    temp.nguonVon, temp.next.nguonVon = temp.next.nguonVon, temp.nguonVon
                    swapped = True
                temp = temp.next

def docDuLieuTuFile(ql, filename):
    with open(filename, "r") as inFile:
        lines = inFile.readlines()
        for i in range(0, len(lines), 3):
            maDuAn = int(lines[i].strip())
            tenDuAn = lines[i+1].strip()
            nguonVon = float(lines[i+2].strip())
            duAn = DuAn(maDuAn, tenDuAn, nguonVon)
            ql.themVaoCuoi(duAn)

ql = QuanLyDuAn()
docDuLieuTuFile(ql, "duan.txt")

choice = -1
while choice != 0:
    print("------------------------------------------------")
    print("---------CAC CHUC NANG CUA CHUONG TRINH---------")
    print("1. Hien thi danh sach")
    print("2. Them du an")
    print("3. Xoa du an")
    print("4. Tim kiem du an")
    print("5. Sap xep du an")
    print("6. Thong ke du an")
    print("7. Xoa file du an theo ten file")
    print("8. Tao moi file luu tru data")
    print("0. Thoat chuong trinh")

    choice = int(input("Nhap lua chon cua ban (0 de thoat): "))

    if choice == 1:
        ql.hienThiDanhSach()
    elif choice == 2:
        sub_choice = -1
        while sub_choice != 0:
            print("1. Them vao dau du an")
            print("2. Them vao cuoi du an")
            print("0. Quay lai")

            sub_choice = int(input("Nhap lua chon cua ban (0 de quay lai): "))

            if sub_choice == 1:
                maDuAn = int(input("Nhap ma du an: "))
                tenDuAn = input("Nhap ten du an: ")
                nguonVon = float(input("Nhap nguon von: "))
                duAn = DuAn(maDuAn, tenDuAn, nguonVon)
                ql.themVaoDau(duAn)
            elif sub_choice == 2:
                maDuAn = int(input("Nhap ma du an: "))
                tenDuAn = input("Nhap ten du an: ")
                nguonVon = float(input("Nhap nguon von: "))
                duAn = DuAn(maDuAn, tenDuAn, nguonVon)
                ql.themVaoCuoi(duAn)
            elif sub_choice == 0:
                print("Quay lai menu chinh.")
            else:
                print("Lua chon khong hop le. Vui long nhap lai.")
    elif choice == 3:
        sub_choice = -1
        while sub_choice != 0:
            print("1. Xoa du an theo ma du an")
            print("2. Xoa du an theo ten du an")
            print("3. Xoa du an theo nguon von")
            print("0. Quay lai")

            sub_choice = int(input("Nhap lua chon cua ban (0 de quay lai): "))

            if sub_choice == 1:
                maDuAn = int(input("Nhap ma du an can xoa: "))
                ql.xoaTheoMa(maDuAn)
            elif sub_choice == 2:
                tenDuAn = input("Nhap ten du an can xoa: ")
                ql.xoaTheoTen(tenDuAn)
            elif sub_choice == 3:
                nguonVon = float(input("Nhap nguon von can xoa: "))
                ql.xoaTheoVon(nguonVon)
            elif sub_choice == 0:
                print("Quay lai menu chinh.")
            else:
                print("Lua chon khong hop le. Vui long nhap lai.")
    elif choice == 4:
        sub_choice = -1
        while sub_choice != 0:
            print("1. Tim kiem du an theo ma du an")
            print("2. Tim kiem du an theo ten du an")
            print("3. Tim kiem du an theo nguon von")

            print("0. Quay lai")

            sub_choice = int(input("Nhap lua chon cua ban (0 de quay lai): "))

            if sub_choice == 1:
                maDuAn = int(input("Nhap ma du an can tim kiem: "))
                duAn = ql.timKiemTheoMa(maDuAn)
                if duAn:
                    print("Ma du an:", duAn.maDuAn, ", Ten du an:", duAn.tenDuAn, ", Nguon von:", duAn.nguonVon)
                else:
                    print("Khong tim thay du an co ma du an", maDuAn)
            elif sub_choice == 2:
                tenDuAn = input("Nhap ten du an can tim kiem: ")
                duAn = ql.timKiemTheoTen(tenDuAn)
                if duAn:
                    print("Ma du an:", duAn.maDuAn, ", Ten du an:", duAn.tenDuAn, ", Nguon von:", duAn.nguonVon)
                else:
                    print("Khong tim thay du an co ten du an", tenDuAn)
            elif sub_choice == 3:
                nguonVon = float(input("Nhap nguon von can tim kiem: "))
                duAn = ql.timKiemTheoVon(nguonVon)
                if duAn:
                    print("Ma du an:", duAn.maDuAn, ", Ten du an:", duAn.tenDuAn, ", Nguon von:", duAn.nguonVon)
                else:
                    print("Khong tim thay du an co nguon von", nguonVon)

            elif sub_choice == 0:
                print("Quay lai menu chinh.")
            else:
                print("Lua chon khong hop le. Vui long nhap lai.")
    elif choice == 5:
        sub_choice = -1
        while sub_choice != 0:
            print("1. Sap xep tang dan")
            print("2. Sap xep giam dan")
            print("0. Quay lai")

            sub_choice = int(input("Nhap lua chon cua ban (0 de quay lai): "))

            if sub_choice == 1:
                ql.sapXepTangDan()
                print("Danh sach sau khi sap xep tang dan:")
                ql.hienThiDanhSach()
            elif sub_choice == 2:
                ql.sapXepGiamDan()
                print("Danh sach sau khi sap xep giam dan:")
                ql.hienThiDanhSach()
            elif sub_choice == 0:
                print("Quay lai menu chinh.")
            else:
                print("Lua chon khong hop le. Vui long nhap lai.")
    elif choice == 6:
        sub_choice = -1
        while sub_choice != 0:
            print("1. Dem du an theo nguon von")
            print("2. Tim du an co nguon von lon nhat")
            print("3. Tim du an co nguon von nho nhat")
            print("4. Hien thi ma du an le")
            print("5. Hien thi ma du an chan")
            print("6. Hien thi nguon von le")
            print("7. Hien thi nguon von chan")
            print("8. Tinh nguon von trung binh")
            print("0. Quay lai")

            sub_choice = int(input("Nhap lua chon cua ban (0 de quay lai): "))

            if sub_choice == 1:
                nguonVon = float(input("Nhap nguon von: "))
                count = ql.demDuAn(nguonVon)
                print("So luong du an co nguon von nho hon", nguonVon, "la:", count)
            elif sub_choice == 2:
                duAn = ql.duAnCoVonLonNhat()
                if duAn:
                    print("Ma du an:", duAn.maDuAn, ", Ten du an:", duAn.tenDuAn, ", Nguon von:", duAn.nguonVon)
                else:
                    print("Khong co du an nao co nguon von lon nhat")
            elif sub_choice == 3:
                duAn = ql.duAnCoVonNhoNhat()
                if duAn:
                    print("Ma du an:", duAn.maDuAn, ", Ten du an:", duAn.tenDuAn, ", Nguon von:", duAn.nguonVon)
                else:
                    print("Khong co du an nao co nguon von nho nhat")
            elif sub_choice == 4:
                ql.hienThiMaDuAnLe()
            elif sub_choice == 5:
                ql.hienThiMaDuAnChan()
            elif sub_choice == 6:
                ql.hienThiVonLe()
            elif sub_choice == 7:
                ql.hienThiVonChan()
            elif sub_choice == 8:
                print("Von trung binh cua danh sach la:", ql.tinhVonTrungBinh())
            elif sub_choice == 0:
                print("Quay lai menu chinh.")
            else:
                print("Lua chon khong hop le. Vui long nhap lai.")
    elif choice == 7:
        filename = input("Nhap ten file can xoa: ")
        ql.xoaTheoTenFile(filename)
        print("Da xoa du an co ten file", filename)
    elif choice == 8:
        filename = input("Nhap ten file moi: ")
        ql.taoMoiFileData(filename)
        print("Da tao moi file luu tru data.")

    elif choice == 0:
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le. Vui long nhap lai.")
