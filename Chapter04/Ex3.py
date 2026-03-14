'''
Viết chương trình kiểm tra một key có tồn tại trong dictionary hay không.
'''

def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
    
# Test
my_dict = {
    'Name': 'Alex',
    'Age': 18,
    'From': 'Vietnam'
}
ktr_key = 'Name'
tontai = check_key(my_dict, ktr_key)
if tontai:
    print(f'Key "{ktr_key}" có tồn tại trong dictionary')
else:
    print(f'Key "{ktr_key}" không tồn tại trong dictionary')