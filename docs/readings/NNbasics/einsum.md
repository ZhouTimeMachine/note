<link rel="stylesheet" href="../../../css/counter.css" />

# Einsum

!!! info "Reference: [Einsum Is All You Need: NumPy, PyTorch and TensorFlow](https://www.youtube.com/watch?v=pkVwUVEHmfI)"

!!! warning "该页面还在建设中"

## Example Uses in PyTorch

```python hl_lines="4 10 14 18"
>>> x = torch.tensor([[1, 2, 3],
                      [4, 5, 6]])

# permutation
>>> torch.einsum("ij->ji", x)
tensor([[1, 4],
        [2, 5],
        [3, 6]])

# summation
>>> torch.einsum("ij->", x)
tensor(21)

# column sum
>> torch.einsum("ij->j", x)
tensor([5, 7, 9])

# row sum
>> torch.einsum("ij->i", x)
tensor([ 6, 15])
```

```python
>>> x = torch.tensor([[1, 2, 3],
                      [4, 5, 6]])
>>> v = torch.tensor([[1, 0, -1]])

# martix-vector multiplication: xv^T
>>> torch.einsum("ij,kj->ik", x, v)
tensor([[-2],
        [-2]])

# martix-matrix multiplication: xx^T
>>> torch.einsum("ij,kj->ik", x, x)  # 2*2: (2*3) @ (3*2)
tensor([[14, 32],
        [32, 77]])

# dot product first row with first row of matrix
>>> torch.einsum("i,i->", x[0], x[0])
tensor(14)
```

```python
>>> x = torch.tensor([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# dot product with matrix
>>> torch.einsum("ij,ij->", x, x)
tensor(285)

# Hadamard product (element-wise multiplication)
>>> torch.einsum("ij,ij->ij", x, x)
tensor([[ 1,  4,  9],
        [16, 25, 36],
        [49, 64, 81]])
```

```python
# outer product
>>> a = torch.tensor([1, 0, -1])
>>> b = torch.tensor([1, 2, 3, 4, 5])
>>> torch.einsum("i,j->ij", a, b)
tensor([[ 1,  2,  3,  4,  5],
        [ 0,  0,  0,  0,  0],
        [-1, -2, -3, -4, -5]])

# batch matrix multiplication
>>> generator = torch.manual_seed(12)
>>> a = torch.rand((3, 2, 5), generator=generator)
tensor([[[0.4657, 0.2328, 0.4527, 0.5871, 0.4086],
         [0.1272, 0.6373, 0.2421, 0.7312, 0.7224]],

        [[0.1992, 0.6948, 0.5830, 0.6318, 0.5559],
         [0.1262, 0.9790, 0.8443, 0.1256, 0.4456]],

        [[0.6601, 0.0554, 0.1573, 0.8137, 0.7216],
         [0.2717, 0.3003, 0.6099, 0.5784, 0.6083]]])
>>> b = torch.rand((3, 5, 3), generator=generator)
tensor([[[0.4339, 0.8813, 0.3216],
         [0.2604, 0.2566, 0.1872],
         [0.6423, 0.1786, 0.1435],
         [0.7490, 0.7275, 0.1641],
         [0.3273, 0.1239, 0.6138]],

        [[0.4535, 0.7659, 0.1800],
         [0.3338, 0.9526, 0.8919],
         [0.9859, 0.6348, 0.8811],
         [0.9391, 0.1173, 0.1342],
         [0.9405, 0.6803, 0.5556]],

        [[0.8713, 0.0782, 0.8578],
         [0.7540, 0.6698, 0.5817],
         [0.3829, 0.7163, 0.8930],
         [0.5597, 0.2803, 0.2476],
         [0.4738, 0.1306, 0.2024]]])
>>> torch.einsum("ijk,ikl->ijl", a, b)
tensor([[[1.1270, 1.0287, 0.6055],
         [1.1608, 0.9403, 0.7584]],

        [[2.0132, 1.6369, 1.5629],
         [1.7535, 1.8831, 1.9043]],

        [[1.4744, 0.5236, 1.0864],
         [1.3086, 0.9008, 1.2188]]])
```


```python
>>> x = torch.tensor([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# matrix diagonal
>>> torch.einsum("ii->i", x)
tensor([1, 5, 9])

# matrix trace
>>> torch.einsum("ii->", x)
tensor(15)
```