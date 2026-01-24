# Fundamental-Numpy-Library-Python

Ini adalah seri 1 pembelajaran machine learning

# 📘 Catatan NumPy — Dasar sampai Implementasi

## 🧠 1. Pengenalan NumPy

NumPy (Numerical Python) adalah library Python untuk komputasi numerik.  
Inti dari NumPy adalah struktur data `ndarray` (N-dimensional array) yang:

- Homogen (satu tipe data)
- Lebih cepat dari list Python
- Mendukung operasi vektor & matriks
- Banyak dipakai di Data Science, AI, dan Statistik

#### 1. Contoh import :

```python
import numpy as np
```

#### 2. Contoh Membuat Array :

- 2.1 Array 1D

```python
a = np.array([1, 2, 3, 4])
print(a)
```

- 2.2 Array 2D

```python
b = np.array([[1, 2], [3, 4]])
print(b)
```

- 2.3 Array Otomatis

```python
np.zeros((2,3))
np.ones((3,3))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

#### 3. Properti Array

```python
print(b.shape)
print(b.ndim)
print(b.dtype)
print(b.size)
```

Keterangan:

- `shape` → bentuk array

- `ndim` → dimensi

- `dtype` → tipe data

- `size` → jumlah elemen

#### 4. Operasi Matematika

```python
x = np.array([1,2,3])

x + 2
x * 3
x ** 2
np.sqrt(x)
np.sin(x)
```

Semua operasi bersifat element-wise.

#### 5. Indexing & Slicing

```python
x = np.array([10,20,30,40])
x[0]
x[1:3]
```

- Untuk 2D:

```python
y = np.array([[1,2,3],[4,5,6]])
y[0]
y[1,2]
```

Format:

- `y[row, col]`

#### 6. Reshape & Transpose

```python
a = np.arange(12)
a = a.reshape((3,4))
print(a)
```

Transpose:

```python
a.T
```

#### 7. Operasi Statistik

```python
data = np.array([80,90,75,85,95])

np.mean(data)
np.max(data)
np.min(data)
np.std(data)
np.sum(data)
```

Digunakan untuk analisis data.

#### 8. Random NumPy

```python
np.random.rand(3,3)
np.random.randint(0,10,5)
```

#### 9. Contoh Kasus Mini

##### Analisis Nilai Mahasiswa

```python
import numpy as np

nilai = np.array([70, 85, 90, 60, 95])

print("Rata-rata:", np.mean(nilai))
print("Tertinggi:", np.max(nilai))
print("Terendah:", np.min(nilai))

```
