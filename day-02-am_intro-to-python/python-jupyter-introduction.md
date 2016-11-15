Title: Introduction to Python and Jupyter notebooks  
Date: 2016-11-10  
Summary: Introduction to Python 3 and Jupyter notebooks

---

# **Introduction to Python**

Lesson adapted from Data Carpentry's "Python for ecologists"- lesson ([CC-BY](https://creativecommons.org/licenses/by/2.0/) license): http://www.datacarpentry.org/python-ecology-lesson/

Etherpad notes available at: https://etherpad.wikimedia.org/p/jyybio_day-02-am_intro-to-python

---

# Before the lesson

Prerequisites:
* -

# After the lesson

You will know about:
* 

---

# 1. Basics of Python

```python
import this
```

## 1.1. Interpreted language

* Python code is translated into machine-language instructions on the go
	- Compare with compiled language, which needs to be traslated before running (faster execution)
* Can be used in interactive mode as "advanced calculator"...

```python
>>> 2 + 2
4
>>> print("Hello World")
Hello World
```

* ... or to execute previsouly written code

```
python my_script.py
Hello World
```
## 1.2. Built-in data types
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

In a script we need to explicitly `print` the variable:
```python
>>> print(text)
"Data Carpentry"
>>> print(number)
42
>>> print(pi_value)
3.1415
```

## 1.3. Operators
Calculations can be performed with basic operators like `+, -, /, *, %`
```python
2 + 2 # Addition
4 - 1 # Subtraction
9 / 3 # Division
6 * 2 # Muplitplication
3 ** 2 # Exponent
13 % 5 # Modulo
9 // 2 # Floor division
```

Comparison operators can also be used `<, >, ==, !=, <=, >=`:
```python
3 > 4
6 == (3 * 2)
6 != 7
```

## 1.3. Sequential types: Lists and Tuples

### 1.3.1. Lists
Lists hold an ordered list of elements, which can contain several different types of elements:
```python
numbers = [1,2,3]
```

Individual elements within lists can be accessed with indexing:
```python
numbers[0]
```

**Note!** Python uses 0- based indexing!

![](images/slicing-indexing.svg)

![](images/slicing-slicing.svg)

**Note!** when defining where to end the slice you set the stop bound one step beyond the final element of interest! So, to select the first two elements:
```python
numbers[0:2]
```

We can also write this shorthand:
```python
numbers[:2]
# compare with
numbers[2:]
```

To get the last element in a list:
```python
numbers[-1]
```

Elements in a list can also be sequentially accessed with a `for` loop (**Note** the intendation!):

```python
for num in numbers:
	print(num)
```

We can append elements to a list with `append`:
```python
numbers.append(4)
```

The `.` after the list signifies that we are using a method, which is a way of interacting with the object. We can get a list of available methods by using the `help` command:
```python
help(aaa)
```

Alternatively, in a Jupyter notebook we can type the object name with a `.` and then press `tab` to get a list of available methods (although not special methods, which are usually accessed differently)

### 1.3.2. Tuples

Tuples can be thought of as list that cannot be modified once created
```python
a_tuple = (1, 2, 3)
# Compare with creating a list
a_list = [1, 2, 3]
```

## 1.4. Dictionaries

Dictionaries are objects that hold element pairs, each entry is comprised of a key and a value:
```python
translation = {"one" : 1, "two" : 2}
translation["one"]
```

Note that you cannot index a dictionary like a list since a dictionary is not ordered (the order of a dictionary can change every time you use it). Instead, you index dictionaries with keys. **Note!** Keys need to be unique!

To add a new value to a dictionary we assign a value to a new key:
```python
translation[3] = "three"
translation
```

To cycle through elements we can also use `for` loops, but with a slightly different logic:
```python
for key, value in translation.items():
	print(key, value)
```

or
```python
for key in translation.keys():
	print(key, translation[key])
```

> Modify the value stored with the key `two` so that it is "open-science"

## 1.5. Functions

If you need to repeat a task mulitple times in a script, instead of writing it out time after time you can define a function with `def`:
```python
def add_function(a, b):
	result = a + b
	return result

z = add_function(20, 22)
print(z)
```
---

# 2. Working with data

## 2.1. About the Pandas library

Pandas is a library, which is comparable to a package in R. To load a library we use the `import` statement. A commonly used strategy is to give the library a shortened name, and call individual functions using the nickname:
```python
import pandas as pd
pd.read_csv("surveys.csv")
```

## 2.2. Reading CSV data into Pandas

Download example dataset here: https://ndownloader.figshare.com/files/2292172

You can either copy the csv file into the directory from where you started the jupyter notebook, change the working directory or specify which directory to use when loading the data (see below):
```python
import os
os.getcwd()
os.chdir("XXX")
```

Then we can read the csv file:
```python
pd.read_csv("surveys.csv")
pd.read_csv("~/Downloads/surveys.csv")
```
 We have now read in the csv file as a DataFrame, which a 2D indexed data structure that can store different data types. This is comparable to a data.frame in R. However, we have not actually saved the data read into Pandas. To do this we need assign it to an object:
 ```python
 surveys_df = pd.read_csv("surveys.csv")
```

## 2.3. Manipulating data

Let's have a look at the data we read into Pandas:
```python
type(surveys_df)
surveys_df.dtypes
```

> What do the following commands do?  
> 1. `surveys_df.columns`
> 2. `surveys_df.head()`
> 3. `surveys_df.tail()`
> 4. `surveys_df.shape`

## 2.4. Calculating statistics

We can quickly get summary statistics from our DataFrame:
```python
surveys_df.describe()
```

Or for a single column:
```python
surveys_df['weight'].describe()
```

### 2.4.1. Grouping

Before grouping we might want to get an idea of what columns we have:
```python
surveys_df.columns.values
```

Then we might want to print out all unique values in the `species` column:
```python
pd.unique(surveys_df['species_id'])
```

> Create a list of unique plot ID's found in the surveys data. Call it plot_names.  
> 1. How many unique plots are there in the data?  
> 2. How many unique species are in the data?

By using the `.groupby` method we can create an object from which group- level statistics can be calculated:
```python
sorted = surveys_df.groupby('sex')
sorted.describe()
```

Alternatively, we could do it all in one go:
```python
surveys_df.groupby('sex').describe()
surveys_df.groupby('sex').mean()
```

> Summarize weight values for each plot in your data. HINT: you can use the following syntax to only create summary statistics for one column in your data by_plot['weight'].describe()

To quickly count the number of observations within groups we can use the `count()` method:
```python
sort = surveys_df.groupby('species_id')
sort['record_id'].count()
# or
surveys_df.groupby('species_id')['record_id'].count()
```

 ---
 
# 3. Indexing, slicing and subsetting

First, let's make sure pandas and our data is loaded:
```python
import pandas as pd
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
```

## 3.1. Indexing and slicing

### 3.1.1. Selecting data with labels

By specifying column names we can easily select columns from a DataFrame:
```python
surveys_df["species_id"]
surveys_df.species_id
```

To specify multiple column names at once we need to specify them in a list. Note that the order of the columns is determined by the order in the list:
```python
surveys_df[['species_id', 'plot_id']]
surveys_df[['plot_id', 'species_id']]
```

### 3.1.2. Extracting Range based Subsets: Slicing

We can select rows from a DataFrame in a similar fashion to slicing a list object. Remember 0 indexing and setting the stop bound one step beyond! So, to select rows 0, 1 and 2, or the last row:
```python
surveys_df[0:3]
surveys_df[-1:]
```

We can use slicing to quickly modify several rows, but before that we want to make a copy of the DataFrame:
```python
surveys_copy = surveys_df
surveys_copy[0:3] = 0
surveys_copy.head()
surveys_df.head()
```

What just happened? Why is our original DataFrame different as well? Let's jump to the next section to find out.

### 3.1.3. A word about referencing vs copying objects

We didn't actually make a new copy of the DataFrame. We created a new object that actually referenced the original. Thus, modifications to the new object also change the original! **Beware!**. To truly make a copy we would:
```python
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
surveys_copy = surveys_df.copy()
surveys_copy[0:3] = 0
surveys_copy.head()
surveys_df.head()
```

### 3.1.4. Slicing Subsets of Rows and Columns in Python

To simultaneously subset a DataFrame using columns and rows we use:
* `loc` to index based on labels
* `iloc` to index based on integers

The following lines of code do the same thing:
```python
surveys_df.loc[0:4, ["record_id", "species_id"]]
surveys_df.iloc[0:5, [0, 5]]
```

**Note** subsetting with `loc` with 0:4 gives a different result from subsetting with `iloc` with 0:4 since in the first case we are not actually slicing but finding rows that have an index value between 0 and 4!

### 3.1.5. Subsetting Data Using Criteria

By specifying criteria we can, for example, select only entries from the year 2000:
```python
surveys_df[surveys_df.year == 2002]
# Try the following code to understand the logic of subsetting with criteria
surveys_df.year == 2002
```

We can also write code to select all entries that do not fit a certain criterion:
```python
surveys_df[surveys_df.year != 2002]
```

...and combine several different selection criteria:
```python
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]
```

> Select a subset of rows in the surveys_df DataFrame that contain data from the year 1999 and that contain weight values less than or equal to 8. How many columns did you end up with?

## 3.2. Using masks

In order to understand masks we need to understand boolean objects, which include `true` or `false` values. For example:
```python
x = 5
x > 5
x == 5
pd.isnull(surveys_df)
```

We can then apply a boolean object with the same dimensions as our object of interest to select only rows with NaN values:
```python
surveys_df[pd.isnull(surveys_df).any(axis=1)]
```

> Create a new DataFrame that only contains observations with sex values that are not female or male. Determine the number of null values in the subset.

---

# 4. Data types and formats

## 4.1. Numeric

## 4.2. Character

## 4.3. Checking data format

## 4.4. Integers and floats

## 4.5. Missing data values

---

# 5. Merging data

## 5.1. Concatenating

## 5.2. Joining

### 5.2.1. Join keys

### 5.2.2. Inner joins

### Left joins

### Other joins

---

# Loops and functions

## For loops

## Data processing with loops

## Functions

