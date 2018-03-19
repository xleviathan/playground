def do_twice(function):
    function()
    function()
def do_three(function):
    function()
    function()
    function()
def do_four(function):
    do_twice(function)
    do_twice(function)
def print_horitzonal_pattern():
    print('+',end='')
    print(4*'-',end = '')
def print_vertical_pattern():
    print('|',end = '')
    print(' '*4,end= '')
def salute():
    do_twice(print_vertical_pattern)
    print('|')
def the_grid():
    do_twice(print_horitzonal_pattern)
    print('+')
    do_four(salute)

do_twice(the_grid)
do_twice(print_horitzonal_pattern)
print('+')