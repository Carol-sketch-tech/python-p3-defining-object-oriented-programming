'''
an object oriented programming is programming that is oriented around data (made mobile and changable in objects)
rather  than functionality.

object orinted does mmore than just bundle up individua; pirces of data that represent a thing - it also bundles 
customized functions that can be performed on that data. these are called methods. behaviors that an onject performs 
upon its internal sata nad even upon other code objects.

'''
# Class and instances.
'''
Defining a class .
think of a class like a blueprint that defines how to build an object.
the python class both contains the instructions for creating new objects from an assembly line which produces a series of 
similar dog objects based on the same Dog template.

'''

# class Dog:  # the Dog class is defined with the class keyword followed by the class na,e and closed with a  deindentations to the level where we defined the Dog class.
    # class names begin with capital letters becasue they are stored in python constants.if your class name contains two words the name should be U
    # UpperCamelCase also called the pascalCase if your feeling fancy😘.

class MyClass:


# creating class instances. Given the following code 

class Dog:
    pass

fido = Dog()
fido  # we instantiate an instance of a dog class by calling the contructor function Dog(). this creates our instance of the Dog class,
    #   which we assign to the variable fido. instanciate means briging an object to life.
    # if we have several dogs with the names lucy, ben and puff the we instatiate these individual dogs by calling the class costrutor function Dog()
    # we call each individuals, specific dog or versions of our class , instances. 

    # An instance is a single occurence of an obeject. instances refer to the indivdual objects produced from the class.

# creating another intance of a Dog 
suzy = Dog()
suzy
# another instance of the Dog obeject.
puff= Dog()
puff
# suzy and puff are instances of the Dog class.

#  Note that different instances are different Objects.

# note that classes are blueprints that define the behaviour and information our objects will contain.
# To use the class to create individual objects, call the class with closed parentheses as you would a function or method.
# this will instantiate (create a new instance of an object from the class.)