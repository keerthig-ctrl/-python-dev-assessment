def filter_and_sort_evens(numbers: list[int]) -> list[int]:
    """
    Return a sorted list of even numbers from the input list.

    filter_and_sort_evens({13,4,1,9,5,6,2})
    -> [2,4,6]
    """
    #1)pick only even numbers
    evens =[n for n in numbers if n% 2 == 0]

    #2)Sort them in ascending order
    return sorted(evens)

if __name__ == "__main__":
    print(filter_and_sort_evens([13,4,1,9,5,6,2]))