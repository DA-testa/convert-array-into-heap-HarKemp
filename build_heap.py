# python3

import math

def build_heap(data):
    swaps = []

    def swap(child,parent):
        if (data[parent] >= data[child]):
            temp = data[child]
            data[child] = data[parent]
            data[parent] = temp
            swaps.append((parent,child))

    rdata = reversed(data)
    for i in rdata:
        n = data.index(i)
        
        while n != 0:
            parent = math.floor((n-1)/2)
            swap(n,parent)

            n = parent

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputType = input()

    # input from keyboard
    if "I" in inputType:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
    # input from a file
    elif "F" in inputType:
        filename = input()
        if "a" in filename:
            return
        if "./tests/" not in filename:
            filename = "./tests/" + filename
        if "./tests/" in filename:
            try:
                with open(filename) as f:
                    n = int(f.readline())
                    data = list(map(int, f.readline().split()))
                    assert len(data) == n
                    swaps = build_heap(data)
            except FileNotFoundError:
                print("file not found")
                return
    else:
        print("Invalid input source")
        return

    # input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    # assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    # swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
