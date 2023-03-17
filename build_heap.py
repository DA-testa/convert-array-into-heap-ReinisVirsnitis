# python3


def swap(data, swaps, c, p):
    swaps.append((p, c))
    data[c], data[p] = data[p], data[c]



def heup(data, swaps, a):
    p = (a - 1) // 2
    if a == 0:
        return
    if data[a] < data[p]:
        swap(data, swaps, a, p)
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
    if 'F' in input_text:
        input_file = input()
        input_file = "tests/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    n = int(f.readline())          
                    data = list(map(int, f.readline().split()))

                    # checks if length of data is the same as the said length
                    assert len(data) == n

                    swaps = build_heap(data)

              
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        assert len(data) == n

        swaps = build_heap(data)

        print(len(swaps))
        for i, j in swaps:
            print(i, j)



    
if __name__ == "__main__":
    main()

