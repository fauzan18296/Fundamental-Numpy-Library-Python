import numpy as np
# TODO: part 1 - Bab Numpy (Pengantar Numpy)
# array = np.array([1, 2, 3, 4])
# array = array * 2
# print("Numpy array:", array)
# print(type(array))

# TODO: part 2 - Bab Numpy (Sub bab Multi dimensional array)
# * Explain:
# ? array.ndim -> menampilkan dimensi array dalam bentuk integer
# ? array.shape -> menampilkan bentuk array dalam bentuk tuple
# ? print(array.ndim) => Output: integer -> jumlah dimensi array
# ? print(array.shape) => Output: (kedalaman/lapisan, baris, kolom) -> tuple(int, int, int)
# ? print(array[0][0][0]) -> Mengakses elemen pada array 3D dengan cara chain indexing
# ? print(array[0, 0, 0]) -> Mengakses elemen pada array 3D dengan cara multidimensional indexing 
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print("Jumlah dimensi: ", array.ndim)
print("tuple: ", array.shape) 
print("Mengakses array dengan cara chain indexing: ", array[0][0][0])
print("Mengakses array dengan cara multidimensional indexing: ", array[0, 0, 0]) 
# * Exercise:
word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
print("Exercise word: ", word)  # Output: "ASS"