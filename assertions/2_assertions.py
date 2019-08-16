# assert_stmt ::= "assert" expression1 ["," expression2]

# expression 1 is the condition we test and the optional expression 2 is the error message
# that is displayed if assertions fails

cond = 'd'
if cond == 'x':
    print('X')
elif cond == 'y':
    print('Y')

else:
    # raise Exception('This was not supposed to happen.Check the input') # Why not raise an exception?
    assert False, ('This was not supposed to happen.Check the input')


# Exceptions are used for run-time error conditions (IO errors, out of memory, can't get a database connection, etc.).

# Assertions are used for coding errors (this method doesn't accept nulls, and the developer passed one anyway).
# https://stackoverflow.com/questions/409794/exception-vs-assert
