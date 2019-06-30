def binary_search(array, number, left, right):
    if right >= left:
        mid = (left + right) // 2
        if array[mid] == number:
            return True
        elif array[mid] < number:
            return binary_search(array, number, left, mid-1)
        else:
            return binary_search(array, number, mid+1, right)
    else:
        return False

if __name__ == '__main__':
    array = [1,5,2,3,9,4,6]
    array.sort()
    print(binary_search(array, 14, 0, len(array)-1))