
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

- Continue running the script if an exeception is raised:

```python
from LoggingDecorator import logd

@logd(raise_exception=False)
def foo():
  print('foo method')

def main():
  foo()

if __name__ == '__main__'
  main()
```

## Authors <a name = "authors"></a>

- [@lkellermann](https://github.com/lkellermann) - Idea & Initial work
