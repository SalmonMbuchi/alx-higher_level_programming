
# EVERYTHING IS AN OBJECT

It means that almost everything that you use:

    1. is an instance of a class
    2. has attributes

I say "almost" because this doesn't hold for keywords (such as for, if, def etc).

## Everything is an instance of a class

When you define a variable, Python creates a pointer to an object in memory. This object is an instance of a class. You can use the function type() to see the class your variable belongs to.

'>>> x = 100'
'>>> type(x)'
'int'

int is the class itself - not a string representing it. Indeed, you could use this class to create other integers. You could think of classes as "factories" that create new objects of the type that they describe.

'>>> # the class int is taking a string as a parameter and creating an integer'
'>>> int('123')'
'123'

Going one step further, since we said that "everything is an object", classes must also be objects. But, if every object is an instance of a class, then also the classes must be an instance of some classes.

It turns out that in Python there is a metaclass type of which all classes are instances. You can think of it as a sort of "universal" factory that creates factories (our classes).

'>>> type(int)'
'type'

##Everything has attributes

To see the attribute of an object you can use the dir function:

'dir(x)'

Attributes can be methods or simply store some data. For instance:

'>>> import os'
'>>> os.sep  # returns the string (some data) that shows the default path separator of your operating system
'/''

Finally, remember that you can change attributes

'os.sep = '\\'' # change to Window path separator

or create new ones:

'os.pc_owner = 'hb''


