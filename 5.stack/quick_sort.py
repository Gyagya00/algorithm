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

        