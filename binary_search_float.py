def binary_search_float(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    top_boundary = None

    while low <= high:
        iterations += 1  # Count the iteration
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            top_boundary = arr[mid]  # Update top_boundary to current mid
        # інакше x присутній на позиції і повертаємо його
        else:
            return (iterations, arr[mid])

    # Якщо x не знайдено, то верхня межа буде значенням low, якщо воно існує
    if low < len(arr):
        top_boundary = arr[low]

    return (iterations, top_boundary)


if __name__ == '__main__':
    test = [0, 2.11, 2.12, 2.13, 3.0, 3.1, 5.0]
    x = 2.13
    result = binary_search_float(test, x)
    print(f"Result: {result}")
