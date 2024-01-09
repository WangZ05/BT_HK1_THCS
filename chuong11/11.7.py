def elementwise_greater_than(L, threash):
    result = []
    for value in L:
        if value > threshold:
            result.append(True)
        else:
            result.append(False)
    return result
L = [float(x) for x in input("Nhập danh sách các phần tử, cách nhau bởi dấu cách: ").split()]
threshold = float(input("Nhập ngưỡng: "))
result_list = elementwise_greater_than(L, threshold)
print("Kết quả:", result_list)