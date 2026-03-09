# Xây dựng một chương trình menu chạy console cho phép người dùng chọn chương trình chạy từ Ex1 - Ex4 và thoát

def menu():
    
    while True:
        print('=== VUI LÒNG CHỌN BÀI BẠN MUỐN CHẠY ===')
        print('Câu 1')
        print('Câu 2')
        print('Câu 3')
        print('Câu 4')
        print('Thoát')

        choice = input('Vui lòng chọn một chương trình (1-5): ')

        if choice == '1':
            import Ex1
        elif choice == '2':
            import Ex2
        elif choice == '3':
            import Ex3
        elif choice == '4':
            import Ex4
        elif choice == '5':
            print('Cảm ơn bạn đã sử dụng chương trình!')
            break
        else:
            print('Bạn vừa nhập số lựa chọn không hợp lệ')