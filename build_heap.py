# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -`1, -1`):
        sift_down(i, data, swaps)
    return swaps


def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    left_child = 2 * i + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, data, swaps)

def main():
    input_text = input()

    if input_text[0] == 'F':
        input_file = input().strip()
        input_file = f"tests/{input_file}"
    
    if 'a' not in input_file:
        try:
            with open(input_file, "r") as f:
                length = int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == length
                swaps = build_heap(data)
                assert len(swaps) < 4 * lenght

                print(len(swaps))
                for i, j in swaps:
                    print(i, j)

        except FileNotFoundError:
            print("File_Not_Found")
            return
        
    elif input_text[0] == 'I':
        length = int(input())
        data = list(map(int, input(). split()))
        assert len(data) = length
        swaps = build_heap(data)
        assert len(swaps) = 4 * length

        print(len(swaps))
        for i, j in swaps:
            print(i, j)

    


if __name__ == "__main__":
    main()
