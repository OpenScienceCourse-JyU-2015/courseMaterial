Title: Introduction to Python and Jupyter notebooks
Date: 2016-11-10  
Summary: Introduction to Python 3 and Jupyter notebooks

---

# Introduction to Python

https://etherpad.wikimedia.org/p/jyybio_day-02-am_intro-to-python

```python
import this
```

---

## About Python

### Interpreted language
- Python code is translated into machine-language instructions on the go
	- Compare with compiled language, which needs to be traslated before running (faster execution)
- Can be used in interactive mode as "advanced calculator"...

```python
>>> 2 + 2
4
>>> print("Hello World")
Hello World
```

- ... or to execute previsouly written code

```
python my_script.py
Hello World
```
### Built-in data types
Strings, integers and floats

```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

Printing values stored within variables:

```python
>>> text
"Data Carpentry"
>>> number
42
>>> pi_value
3.1415
```

Printing values stored within variables in scripts:

```python
>>> print(text)
"Data Carpentry"
>>> print(number)
42
>>> print(pi_value)
3.1415
```