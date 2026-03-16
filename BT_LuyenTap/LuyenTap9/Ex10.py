'''
Tạo class SinhVien có thuộc tính điểm
Nạp chồng toán tử `==` để so sánh hai sinh viên theo điểm.
Chạy thử.
'''

class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return NotImplemented

def main():
    sv1 = SinhVien(9.0)
    sv2 = SinhVien(7.5)
    sv3 = SinhVien(7.5)

    print(f'SV1 == SV2: {sv1 == sv2}')
    print(f'SV2 == SV3: {sv2 == sv3}')
    print(f'SV1 == SV3: {sv1 == sv3}')

if __name__ == "__main__":
    main()