from sorters.ISORT import ISort
class QuickSort:
    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left  = [x for x in arr if x < pivot]
        mid   = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.sort(left) + mid + self.sort(right)
