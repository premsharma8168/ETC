class ArrayConverter:
    def __init__(self):
        self.array = []

    def read_array(self):
        self.array = []
        while True:
            try:
                self.array.extend(map(int, input("Enter array elements separated by spaces (press Enter when done): ").split()))
                break
            except ValueError:
                print("Please enter valid integers separated by spaces.")
        return self.array

    def convert_array_to_dimension(self, array, dimension):
        total_elements = len(array)
        
        if dimension < 1:
            return "Error: Invalid dimension. The new dimension must be greater than 0."
        
        if dimension > total_elements:
            return "Error: Invalid dimension. The new dimension must be less than or equal to the total number of elements."
        
        new_dimension_size = total_elements // dimension
        
        if total_elements % dimension != 0:
            return "Error: Invalid dimension. The new dimension must evenly divide the total number of elements."
        
        new_array = []
        for i in range(dimension):
            new_array.append(array[i * new_dimension_size : (i + 1) * new_dimension_size])
        
        return new_array

array_converter = ArrayConverter()
array = array_converter.read_array()
dimension = int(input("Enter the new dimension (Sqrt of array elements.): "))
result = array_converter.convert_array_to_dimension(array, dimension)

if isinstance(result, str):
    print(result)
else:
    print("Original Array:")
    for row in array:
        print(row)
    print("\nArray with New m*n Dimension:")
    for row in result:
        print(row)