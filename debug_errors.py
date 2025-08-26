def calculate_average(numbers):
    """
    Calculate average of a sequence of numbers.
    Returns:
    - float average for non-empty list-like inputs
    - None if the list is empty or input is invalid
    Behaviour:
    - Handles ZeroDivisionError(empty list) and TypeError
    (bad input)gracefully.
    """
    total = 0
    try:
        for i in range(len(numbers)):
            total += numbers[i]
            return total/len(numbers)
    except ZeroDivisionError:
        print("Warning: calculate_average called with an empty list.Returning None.")
        return None
    except TypeError:
        print("TypeError: calculate_average expects a sequence of numbers.Returning None.")
        return None
    
def get_list_element(my_list, index):
    """
    Return the element at 'index' in 'my_list'.
    If index is out of bounds -> catch IndexError,print friendly message,return None.
    If my_list is not a list -> treat as TypeError,print message,return None.
    """
    try:
        if not isinstance(my_list,list):
            raise TypeError("my_list is not a list")
        return my_list[index]
    except IndexError:
        list_len = len (my_list) if hasattr(my_list,"__len__")
        else"unknown"
        print(f"IndexERROR: INDEX {index} OUT OF BOUNDS (LIST LENGTH {list_len}). Returning None.")
        return None
    except TypeError:
       print("TypeError: get_list_element expects(list,int). Returning None.")
    return None

if__name__ == "__main__":

data1 = [10,20,30,40,50]
data2 = [5,15]
data3 = []

print(f"Average of data1 : {calculate_average(data1)}")
print(f"Average of data2 : {calculate_average(data2)}")
print(f"Average of data3 : {calculate_average(data3)}")

print("get_list_element(data1,2):",
      get_list_element(data1,2))
print("get_list_element(data1,99):",
      get_list_element(data1,99))
print("get_list_element('not a list', 0):",
      get_list_element("not a list", 0))
