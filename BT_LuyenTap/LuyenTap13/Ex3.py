'''
- Viết một chương trình in ra tất cả các số lẻ từ 1 đến 30 dùng while
- Tính tổng của tất cả các số lẻ này, in ra màn hình
'''

num=30
tong=0
while num!=0:
    if num%2==0:
        num=num-1
    else:
        tong=tong+num
        print(num)
        num=num-1
print(f'Tổng của tất cả các số lẻ là: {tong}')