numbers = [3, 9, 4, 6, 5, 0, 1, 6, 8, 2]

def quick_sort(numbers):
    N = len(numbers)
    if N <= 1:
        return numbers
    else:
        pivot = numbers[0]
        left, right = [], []

        for idx in range(1, N):
            if numbers[idx] > pivot:
                right.append(numbers[idx])
            else:
                left.append(numbers[idx])
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return [*sorted_left, pivot, *sorted_right]

# 피보팅을 선택하는 코드를 함수로 뺀 2번째 방법

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 피봇을 확정해주는
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort2(arr, start, pivot -1)
        quick_sort2(arr, pivot+1, end)
    return arr



print(numbers)
# print(quick_sort(numbers))
print(quick_sort2(numbers, 0, len(numbers)-1))