# Day-10 Part-6 — NumPy Shapes & Dimensions

This note explains NumPy shapes from ZERO level.
Each example includes:
- code
- output
- meaning (plain English)

---

## 1. What is Shape?

Shape tells how data is arranged in a NumPy array.

It answers:
- how many elements?
- how many rows?
- how many columns?

Check shape using:
```python
array.shape

#2. 1D Array (Most Basic Form)
import numpy as np

a = np.array([10, 20, 30])
print(a)
print(a.shape) #[10 20 30]
(3,)

# Row vector
b = np.array([[10, 20, 30]])
print(b)
print(b.shape)

#4. Column Vector (Very Important)
