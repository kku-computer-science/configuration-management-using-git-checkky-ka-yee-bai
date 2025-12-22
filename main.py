from sorters.quick import QuickSort
from sorters.bubble import BubbleSort
from sorters.ISORT import ISort  

test_data = [84,12,59,34,76,91,5,23,45,67,89,10,32,54,78,90,2,15,37,49,61,83,95,8 ,29 ,41]



if __name__ == "__main__":
    if test_data:
        print(f"\nOriginal: {test_data}")
        print('-'*50)

        sorter = QuickSort()
        result = sorter.sort(test_data)
        print(f'QuickSort Result : {result}')
        print('-'*50)

        
        sorter = BubbleSort()
        result = sorter.sort(test_data)
        print(f'BubbleSort Result : {result}')
        print('-'*50)