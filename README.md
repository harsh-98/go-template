# Go-template

[![PyPI Version](https://img.shields.io/pypi/v/go_template.svg)](https://pypi.python.org/pypi/go_template)
[![Wheel Status](https://img.shields.io/badge/wheel-yes-brightgreen.svg)](https://pypi.python.org/pypi/go_template)
![Build Status](https://img.shields.io/travis/SixQuant/project-template-python/master.svg)

## Overview
Python bindings for go text/template



## Quickstart

### Pip
`go_template` works Python 2.7, 3.5, 3.6, 3.7.
```
pip install go_template
```

## Example

Content of sample.tmpl
```
{{.Count}} items are made of {{.Material}}
```
Content of values.yml
```
Count: 12
Material: Wool
```

1)  Print rendered output to stdout
```
>>> import go_template
>>> go_template.render_template('tests/sample.tmpl','tests/values.yml','')
12 items are made of Wool
```

2) Get rendered output in a file
```
>>> import go_template
>>> go_template.render_template('tests/sample.tmpl','tests/values.yml','output.txt')

```
 Content of output.txt
```
12 items are made of Wool
```


__NOTE__: Paths provided to render_template should either be absolute path or relative to directory where it is ran.

## Build shared library


For building a fresh shared object of text/template, you must have golang^1.5 installed.

```
./build.sh
```

This will create [template.so](https://github.com/harsh-98/go-template/blob/master/bind/template.so) in the `bind` folder.

## Motivation
Currently, there is no python package which exposes golang `text/template` functionality to python. And I am in the process of learning about interoperability between different languages. So, I started working on this as a learning project.

## Explanation
Golang library cannot be directly used in python. Firstly, we have to compile it as shared object or archive for interoperability with C. And then create python bindings for this C object.

[CPython](https://github.com/python/cpython) is the original Python implementation and provides cpython API for creating python wrapper, but the wrapping code is in C. There is a library [gopy](https://github.com/go-python/gopy) which exactly uses this approach. But it works only on go1.5 and for python2.

If we want to write the wrapping code in python, there are [Cython](https://cython.org/) and [ctypes](https://docs.python.org/3/library/ctypes.html). Ctypes allow directly importing the C library and calling functions through its interface. This project uses `ctypes` for calling go functions.

When a golang library is compiled as shared object, [cgo](https://golang.org/cmd/cgo/) handles exposing functions and data type conversion. Using ctypes, we can only modify simple data type, string, int, float, bool. I tried converting python class to golang struct, but it failed.

So, I created a golang wrapper over text/template library, which takes simple datatypes. And handles complex operation in this layer. Then a python wrapper over this layer using `ctypes`.

It is far from complete and doesn't use the best approach. Currently, it has only one function which takes path of template and value file. And depending on the third argument, either writes to stdout if empty  or to file if given its path.

## License

This project is licensed under [MIT](https://github.com/harsh-98/go-template/blob/master/LICENSE) License.