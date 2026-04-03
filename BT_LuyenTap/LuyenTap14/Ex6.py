layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer 31": 43
        }
    },
    "layer-12": 35
}

print(f'Giá trị của lớp layer 12 là: {layers["layer-12"]}')
print(f'Giá trị của lớp layer 31 là: {layers["layer-11"]["layer-22"]["layer 31"]}')