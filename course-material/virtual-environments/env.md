# Virtual Environments

During the course, we have installed libraries using the command:

```shell
sudo pip install nose
sudo pip install coverage
```

Thus, those libraries are now available for every single project in your computer.
Your projects would have to use those libraries with the same stage of development,
with the same version.
This is not ideal, because:

* It is very likely that your computer will host several Python projects.
* It is possible that some projects will depend on the same library (which is fine!)
* It is also possible that the would depend on **different versions** of those libraries
  (this will cause problems).
  
Software is continuously evolving. The a different version of the library might
render your software unusable.

Would not be great if every project could have its own libraries, with the 
specific version of the library that they need to use?

## Virtual environments to the rescue
Install the library ``virtualenvwrapper``.

```shell
sudo pip install virtualenvwrapper
```

Create a virtual environment for your project. You can specify to use whether
Pyton2 or Python3.

```shell
mkvirtualenv -p /usr/bin/python3 pydna_environment
```

You can exit your virtual enviroment with the comand ``deactivate``. You can enter
your virtual environment with the command ``workon``.

From now on, all development, testing, doctesting, generation of documentation
should be performed inside the virtual environment.

Let's create a small function to work with dates using the library ``arrow``.

```shell
workon pydna_environment
pip install arrow
```

Note that we are not using ``sudo`` as we don't want that particular version of
``arrow`` to be available for all the projects in our computers.

```python
import arrow

def humanize_my_date(date_input):
    date_object = arrow(date_input)
    humanized_date = date_object.humanize()
    return humanized_date

course_start = '2015-04-21'
course_start_humanized = humanize_my_date(course_start)
print(course_start_humanized)
```

It is important to deliver our packaged software along with a detailed list of
the required libraries. We should specify library name and exact version.

Luckily, ``pip`` is of great help. See the required libraries for this project:

```shell
pip freeze
```

Save the list to a file:
```shell
pip freeze > requirements.txt
```

So, when users want to run your software they can easily install the correct
requirements by doing this:

```shell
mkvirtualenv -p /usr/bin/python3 carlos_software
pip install -r requirements.txt
```

By doing this, you are making sure that the analyses conducted with your software
can be reproduced by anyone.
