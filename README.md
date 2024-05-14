# Vector Class

The `Vector` class provides a convenient way to work with 3-dimensional vectors and perform various vector operations.

## Installation

This is a standalone Python class and does not require any installation. Simply include the `Vector` class in your Python project or import it as needed.

## Usage

To use the `Vector` class, first, create instances of the class by providing the x, y, and z coordinates. You can then perform various operations on these vectors such as addition, subtraction, multiplication, division, computing scalar products, and computing cross products.

### Example

```python
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Perform vector operations
v_add = v1 + v2
v_sub = v1 - v2
v_mul = v1 * v2
v_div = v1 / v2
scalar_product = v1.scalar(v2)
cross_product = v1.cross(v2)

# Display results
print("Vector Addition:", v_add)
print("Vector Subtraction:", v_sub)
print("Vector Multiplication:", v_mul)
print("Vector Division:", v_div)
print("Scalar Product:", scalar_product)
print("Cross Product:", cross_product)
```

