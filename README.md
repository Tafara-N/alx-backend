# Pagination

![Paginated Cat](pictures/pagination.png)

![Paginated Cat](pictures/pagination_2.png)

![Paginated Cat](pictures/pagination_3.png)

# Resources

**Read or watch:**
- [REST API Design: Pagination](https://intranet.alxswe.com/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw)
- [HATEOAS](https://intranet.alxswe.com/rltoken/tfzcEbTSdMYSYxsspJH_oA)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/zQ78qQVUjaPExupXQpAaHw), **without the help of Google:**

How to paginate a dataset with simple page and page_size parameters
How to paginate a dataset with hypermedia metadata
How to paginate in a deletion-resilient manner

# Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version `3.7`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version `2.5.*`)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Setup: `Popular_Baby_Names.csv`

[use this data file](https://intranet.alxswe.com/rltoken/NBLY6mdKDBR9zWvNADwjjg) for your project

# Caching

# Background Context

In this project, you learn different caching algorithms.

## Resources

**Read or watch:**
- [Cache replacement policies - FIFO]()
- [Cache replacement policies - LIFO]()
- [Cache replacement policies - LRU]()
- [Cache replacement policies - MRU]()
- [Cache replacement policies - LFU]()

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](), **without the help of Google:**

## General
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

# More Info

**Parent class BaseCaching**

All your classes must inherit from `BaseCaching` defined below

```bash
$ cat base_caching.py
#!/usr/bin/python3

"""
BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """

        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """

        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """

        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """

        raise NotImplementedError("get must be implemented in your cache class")
```
