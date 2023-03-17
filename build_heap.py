# python3


def swap(data, swaps, c, p):
    swaps.append((p, c))
    data[c], data[p] = data[p], data[c]



def heup(data, swaps, a):
    p = (a - 1) // 2
    if a == 0:
        return
    if data[a] < data[p]:
        swap(data, a, swaps, p)
        heup(data, swaps, p)
    
def build_heap(data):
    n = len(data)
    swaps = []

    if n == 0:
        swaps.append(0)
        return swaps

    for i in range(n-1, -1, -1):
        heup(data, swaps, i)

    return swaps


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
                assert len(swaps) < 4 * length

                print(len(swaps))
                for i, j in swaps:
                    print(i, j)

        except FileNotFoundError:
            print("File_not_found_error")
            return
        
    elif input_text[0] == 'I':
        length = int(input())
        data = list(map(int, input(). split()))
        assert len(data) == length
        swaps = build_heap(data)
        assert len(swaps) < 4 * length

        print(len(swaps))
        for i, j in swaps:
            print(i, j)

    
if __name__ == "__main__":
    main()

