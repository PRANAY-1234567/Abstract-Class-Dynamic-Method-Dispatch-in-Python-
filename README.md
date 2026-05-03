# 🔷 Abstract Class & Dynamic Method Dispatch in Python (Shape Example)

## 📌 Description

This Python program demonstrates **Abstraction** and **Dynamic Method Dispatch** using an abstract class `Shape`. Different shapes (`Rectangle`, `Triangle`, `Circle`) implement their own version of the `area()` method.

---

## 🚀 Features

* Uses **Abstract Base Class (ABC)**
* Implements **method overriding**
* Demonstrates **runtime polymorphism (dynamic dispatch)**
* Supports multiple shapes:

  * Rectangle
  * Triangle
  * Circle

---

## 🛠️ How It Works

### 1️⃣ Abstract Class `Shape`

* Contains:

  * `dim1`, `dim2` → dimensions
  * `setDimensions()` → sets values
  * `showDimensions()` → displays values
  * `area()` → abstract method (must be implemented by child classes)

---

### 2️⃣ Child Classes

#### ▭ Rectangle

```python
area = length × breadth
```

#### 🔺 Triangle

```python
area = (base × height) / 2
```

#### ⚪ Circle

* Uses only one value (radius)
* Overrides `setDimensions()`

```python
area = π × r²
```

---

### 3️⃣ Dynamic Method Dispatch

```python
ref = t
ref.area()
```

👉 `ref` can point to **any object**
👉 Method call depends on **actual object type at runtime**

---

## 💻 Code

```python id="q7x2lp"
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        self.dim1 = 0
        self.dim2 = 0

    def setDimensions(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def showDimensions(self):
        print("First dimension :", self.dim1)
        print("Second dimension:", self.dim2)

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        print("Area of rectangle :", self.dim1 * self.dim2)


class Triangle(Shape):
    def area(self):
        print("Area of triangle :", self.dim1 * self.dim2 / 2)


class Circle(Shape):
    def setDimensions(self, rad):
        super().setDimensions(rad, 0.0)

    def area(self):
        print("Area of circle :", math.pi * self.dim1 * self.dim1)


# Main program
t = Triangle()
t.setDimensions(45.3, 62.4)

r = Rectangle()
r.setDimensions(76.5, 36.5)

c = Circle()
c.setDimensions(55.4)

# Dynamic Method Dispatch
ref = t
print("Triangle\n------------")
ref.showDimensions()
ref.area()

ref = r
print("\nRectangle\n------------")
ref.showDimensions()
ref.area()

ref = c
print("\nCircle\n------------")
ref.showDimensions()
ref.area()
```

---

## ▶️ Sample Output (Approx)

```id="n8k4pz"
Triangle
------------
First dimension : 45.3
Second dimension: 62.4
Area of triangle : 1413.36

Rectangle
------------
First dimension : 76.5
Second dimension: 36.5
Area of rectangle : 2792.25

Circle
------------
First dimension : 55.4
Second dimension: 0.0
Area of circle : 9638.77
```

---

## 📚 Concepts Used

* Abstract Class (`ABC`)
* Abstract Method (`@abstractmethod`)
* Inheritance
* Method Overriding
* Runtime Polymorphism
* Dynamic Method Dispatch

---

## 🧠 Key Concepts (Exam Important 🔥)

### ✔ Abstraction

* Hides implementation details
* Forces subclasses to define `area()`

### ✔ Polymorphism

* Same method name → different behavior

### ✔ Dynamic Binding

* Method call resolved at runtime

---

## ⚠️ Important Notes

* Cannot create object of abstract class:

```python
Shape() ❌
```

* Must override `area()` in child classes

---

## 🔧 Future Improvements

* Add more shapes (Square, Ellipse)
* Take input from user
* Return values instead of printing
* Add GUI visualization

---

## 📄 License

Open-source and free to use.

<img width="637" height="717" alt="image" src="https://github.com/user-attachments/assets/db591c96-7fb6-44f8-9041-814726416fc0" />

