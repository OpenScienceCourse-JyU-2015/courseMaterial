# Documentation and modules in Python 

(Carlos Peña)

## Overview
* [Create a module for your Python code](create a module for your python code)
* [How to document software](#how-to-document-software)

## Create a module for your Python code
Fist of all, your Python code should be packed as a module. You have been 
working the in the ``testing_repo`` folder but your script is not modular in 
the pythonic way.

You need to create a python module, a folder, to contain your code:

```shell
mkdir pydna
mv seq_utils.py pydna/.
```

Thus, every Python module is contained into one folder. For this module to be
complete, an empty file should be created:

```shell
touch pydna/__init__.py
```

Now your module is now complete. This is a good opportunity to commit your
changes:

```shell
git add pydna/seq_utils.py
git add pydna/__init__.py
git commit -a -m 'creating python module'
git push origin master
```

Try to run your unit tests. Do they pass?
```shell
nosetests tests.py
```

They fail because you need to correct the imports. You should import the module
and them import the file with your Python code.
Edit your ``tests.py`` file:

```
from pydna import seq_utils
```

Save it and run the tests again. If everything is ok, then commit your changes:

```shell
git add tests.py
git commit -m 'correcting import in tests file'
git push origin master
```

## How to document software
Automatically using ``sphinx`` in combination with **"read the docs"**.
Go to Google and search for "read the docs". Follow the instructions in the 
documentation:

Install ``sphinx``:

```shell
sudo pip install sphinx
sudo pip install sphinx-autobuild
```

Create a directory inside your project to hold your docs:

```shell
cd /path/to/testing_repo
mkdir docs
```

Run sphinx-quickstart in there:

```shell
cd docs
sphinx-quickstart
```

Accept most default values. But make sure that we allow:
* autodoc: automatically insert docstrings from modules
* doctest: automatically test code snippets in doctest blocks

You will find the new file, ``conf.py``. Open it in your text editor and 
fix and include the following lines.
This will help us to include our code into the documentation.

```python
sys.path.insert(0, os.path.abspath('..'))
import pydna
```

Generate documentation for your Python module:
```shell
sphinx-apidoc -o . ../pydna
make html
```

You will find new folder and files. Open the file ``_build/html/index.html``
in your web browser. Explore your documentation.
There is not much. Add documentation and docstrings.

This is a docstring:
```python
"""Validates a codon by checking that allowed list of bases are included
in our input variable.

:param input_codon: codon, may be valid or not
:return: True or False
"""
```

Regenerate the documentation:
```shell
make html
```

In the docstrings, you can include examples to explain how your code can be used.
These are the so called **doctests**.
```python
>>> from pydna import seq_utils
>>> input_codon = 'ATC'
>>> seq_utils.is_codon_correct(input_codon)
True
```

The library Sphinx will execute the code that you put in the docstrings. If
you change the code in your module, these doctests may fail.
Run the doctests:

```shell
make doctest
```

Having doctests in docstrings will help you write the documentation of your
software. By checking that the doctests pass, your users will be able to successfully
run the examples in your documentation.

You can also write additional documentation by creating ``.rst`` files. 
Let's create the file ``usage.rst`` with the following content:

```rst
Usage
=====

This is how you can use my cool Python program ``PyDNA``:

>>> from pydna import seq_utils
>>> codon = 'ATT'
>>> seq_utils.complement_codon(codon)
'ATC'
```

If you run your doctest, this should fail. Fix it and rerun.

You can automate the generation of your documents by using the services
of "read the docs". [Go to this page](https://read-the-docs.readthedocs.org/en/latest/getting_started.html#import-your-docs) 
and follow the instructions to set up a read the docs account for your software.
