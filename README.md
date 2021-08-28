
<H1 align="center">LoggingDecorator</H1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/lkellermann/logging-decorator.svg)](https://github.com/lkellermann/logging-decorator/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/lkellermann/logging-decorator.svg)](https://github.com/lkellermann/logging-decorator/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>


<p align="center">  A simple way to log your Python methods.
    <br> 
</p>

## About <a name = "about"></a>

LoggingDecorator is a MIT licensed general-purpose software package written in Python that simplyfies the task of logging methods of other Python scripts.

## Getting Started <a name = "getting_started"></a>

To install this package you can just type in your Python terminal:

```shell
pip install logging-decorator
```

### Prerequisites

This Python package only works with `Python 3.6` or later.

## Usage <a name="usage"></a>

The simplest use case is logging a generic method and displaying the log on screen.
```python
from LoggingDecorator import logd

@logd
def foo():
  print('foo method')

def main():
  foo()

if __name__ == '__main__'
  main()
```

## Features <a name="-gem-features-"></a>

- Generate `.log` files inside a `log` folder in the current working directory.

```python
from LoggingDecorator import logd

@logd(file=True)
def foo():
  print('foo method')

def main():
  foo()

if __name__ == '__main__'
  main()
```

- Continue running the script if an exception is raised:

```python
from LoggingDecorator import logd

@logd(raise_error=False)
def foo():
  print('foo method')

def main():
  foo()

if __name__ == '__main__'
  main()
```

- Set logging level:

```python
from LoggingDecorator import logd

@logd(logging_level='critical')
def foo():
  print('foo method')

def main():
  foo()

if __name__ == '__main__'
  main()
```
    
  - The available options are: `critical`, `error`, `warning`, `info`, `debug` and `notset`.
## Output Sample

Supose that you have a `foo` project with the following structure:
```
📦foo
 ┗ 📜foo.py
 ```
 And the contents of the `foo.py` file is the following:
```python
from time import sleep
from LoggingDecorator import logd

@logd(file=True, logging_level='debug')
def foo_sum(a:int, b:int=1):
    sleep(3)
    return a+b

@logd(file=False, raise_error=True)
def foo_div(a:int, b:int=0):
    return a/b

def main():
    foo_sum(1)
    foo_div(5)
    
if __name__=='__main__':
    main()
```

The method `foo_sum` will print and generate a file like `./foo/log/foo_foo_sum_28Aug2021_114203.log` with the following content:

```
2021-08-28 11:42:03,695 - Working directory:     /absolute/path/to/foo
2021-08-28 11:42:03,695 - Module name:           __main__
2021-08-28 11:42:03,696 - Method name:           foo_sum
2021-08-28 11:42:03,696 - Error message:         None
2021-08-28 11:42:03,696 - Start time:            2021-08-28 11:42:00.690282
2021-08-28 11:42:03,696 - End time:              2021-08-28 11:42:03.694016
2021-08-28 11:42:03,696 - Elapsed time:          0:00:03.003734
2021-08-28 11:42:03,697 - Variables:             (a: int, b: int = 1)
2021-08-28 11:42:03,697 - Args:                  None
2021-08-28 11:42:03,697 - Kwargs:                None
2021-08-28 11:42:03,697 - Log path:              /absolute/path/to/foo/log/foo_foo_sum_28Aug2021_114203.log
```

And the `foo_div` will generate the following message in your screen:

```

2021-08-28 11:42:03,698 - Module name:           __main__
2021-08-28 11:42:03,699 - Method name:           foo_div
2021-08-28 11:42:03,699 - Error message:         division by zero
2021-08-28 11:42:03,699 - Start time:            2021-08-28 11:42:03.698178
2021-08-28 11:42:03,699 - End time:              2021-08-28 11:42:03.698622
2021-08-28 11:42:03,699 - Elapsed time:          0:00:00.000444
2021-08-28 11:42:03,700 - Variables:             (a: int, b: int = 0)
2021-08-28 11:42:03,700 - Args:                  (5,)
2021-08-28 11:42:03,700 - Kwargs:                {}
2021-08-28 11:42:03,700 - Log path:              None
Traceback (most recent call last):
  File "/absolute/path/to/foo/foo.py", line 18, in <module>
    main()
  File "//absolute/path/to/foo/foo/foo.py", line 15, in main
    foo_div(5)
  File "/local/python/path/site-packages/LoggingDecorator/LoggingDecorator.py", line 33, in wrapped_function
    return LoggingDecorator(*dargs, **dkwargs).call(original_method, *args, **kwargs)
  File "/local/python/path/site-packages/LoggingDecorator/LoggingDecorator.py", line 78, in call
    return self._summary(original_method, 
  File "/local/python/path/site-packages/LoggingDecorator/LoggingDecorator.py", line 149, in _summary
    raise LogException(error_message)
LoggingDecorator.LoggingDecorator.LogException: LogException[division by zero]

```


## Authors <a name = "authors"></a>

- [@lkellermann](https://github.com/lkellermann) - Idea & Initial work
