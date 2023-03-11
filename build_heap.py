# python3

def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    i = n - 1
    i = int((i+1)/2)-1

    def swap(child,parent):
        if (data[parent] >= data[child]):
            temp = data[child]
            data[child] = data[parent]
            data[parent] = temp
            swaps.append((parent,child))
            return True
        return False
    
    while(True):
        sortedChild = False
        isProper = False
        leftChild = 2*i+1
        rightChild = 2*i+2
        parent = int((i+1)/2)-1
        if (rightChild <= n-1):
            sortedChild = swap(rightChild, i)
            if sortedChild == True:
                i = 2*i+2
                continue
        if (leftChild <= n-1):
            sortedChild = swap(leftChild, i)
            if sortedChild == True:
                i = 2*i+1
                continue
        if (parent >= 0):
            isProper = swap(i, parent)
        if isProper == False and sortedChild == False:
            if parent <= -1:
                break
            else:
                i = parent 
            
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputType = input()

    if "I" in inputType:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data, n)
    # input from a file
    elif "F" in inputType:
        filename = input()
        if "a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:
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
    print(int(len(swaps)/2))
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
