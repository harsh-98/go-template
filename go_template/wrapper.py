from ctypes import *
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
shared_lib = os.path.join(root_dir, 'bind', 'template.so')
lib = cdll.LoadLibrary(shared_lib)

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

def get_go_string(val):
    return GoString(val.encode('utf-8'), len(val))

def render_template(template, value_file, output):
    template = get_go_string(template)
    value_file = get_go_string(value_file)
    output = get_go_string(output)

    lib.RenderTemplate.argtypes = [GoString, GoString, GoString]
    lib.RenderTemplate(template, value_file, output)

# render_template('sample.tmpl', 'values.yml','output.txt')