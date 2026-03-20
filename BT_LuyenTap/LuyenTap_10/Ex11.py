while True:
    print("\n=== MENU BÀI TẬP ===")
    print("1. Chạy Bài 1")
    print("2. Chạy Bài 2")
    print("3. Chạy Bài 3")
    print("4. Chạy Bài 4")
    print("5. Chạy Bài 5")
    print("6. Chạy Bài 6")
    print("7. Chạy Bài 7")
    print("8. Chạy Bài 8 (và 10)")
    print("9. Chạy Bài 9")
    print("11. Chạy Bài 11")
    print("0. Thoát chương trình")
    print("===========================")
    
    lua_chon = input("Nhập số thứ tự bài tập bạn muốn chạy: ")
    
    if lua_chon == "0":
        print("Chương trình đã kết thúc.")
        break
    elif lua_chon == "1":
        print("Đang chạy Bài 1...")

    elif lua_chon == "2":
        print("Đang chạy Bài 2...")

    elif lua_chon == "3":
        print("Đang chạy Bài 3...")

    elif lua_chon == "4":
        print("Đang chạy Bài 4...")

    elif lua_chon == "5":
        print("Đang chạy Bài 5...")

    elif lua_chon == "6":
        print("Đang chạy Bài 6...")

    elif lua_chon == "7":
        print("Đang chạy Bài 7...")

    elif lua_chon in ["8", "10"]:
        print("Đang chạy Bài 8 và 10...")

    elif lua_chon == "9":
        print("Đang chạy Bài 9...")

    elif lua_chon == "11":
        print("Đây chính là chương trình Menu (Bài 11) bạn đang chạy rồi!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!")