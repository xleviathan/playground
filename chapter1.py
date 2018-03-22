def do_twice(function):
    function()
    function()
def do_four(function):
    do_twice(function)
    do_twice(function)
