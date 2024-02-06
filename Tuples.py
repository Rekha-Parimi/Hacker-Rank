if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Create a tuple
    t = tuple(integer_list)

    # Print the result of hash(t)
    print(hash(t))
