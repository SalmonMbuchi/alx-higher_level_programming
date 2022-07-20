# OBJECT ORIENTED PROGRAMMING


Object Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects. It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects. There are many object-oriented programming languages including JavaScript, C++, Java, and Python.

A class is an abstract blueprint used to create more specific, concrete objects. Classes often represent broad categories, like Car or Dog that share attributes. These classes define what attributes an instance of this type will have, like color, but not the value of those attributes for a specific object.

Classes can also contain functions, called methods available only to objects of that type. These functions are defined within the class and perform some action helpful to that specific type of object.

## BENEFITS OF OOP

    1. OOP models complex things as reproducible, simple structures
    2. Reusable, OOP objects can be used across programs
    3. Allows for class-specific behavior through polymorphism
    4. Easier to debug, classes often contain all applicable information to them
    5. Secure, protects information through encapsulation

**Object**

This is the basic unit of object-oriented programming. That is both data and function that operate on data are bundled as a unit called an object.

**Class**

When you define a class, you define a blueprint for an object. This doesn't actually define any data, but it does define what the class name means, that is, what an object of the class will consist of and what operations can be performed on such an object.

OOP has four basic concepts on which it is totally based. Let's have a look at them individually −

     1. **Abstraction** − It refers to, providing only essential information to the outside world and hiding their background details. For example, a web server hides how it processes data it receives, the end user just hits the endpoints and gets the data back.
     
     2. **Encapsulation** − Encapsulation is a process of binding data members (variables, properties) and member functions (methods) into a single unit. It is also a way of restricting access to certain properties or component. The best example for encapsulation is a class.
     
     3. **Inheritance** − The ability to create a new class from an existing class is called Inheritance. Using inheritance, we can create a Child class from a Parent class such that it inherits the properties and methods of the parent class and can have its own additional properties and methods. For example, if we have a class Vehicle that has properties like Color, Price, etc, we can create 2 classes like Bike and Car from it that have those 2 properties and additional properties that are specialized for them like a car has numberOfWindows while a bike cannot. Same is applicable to methods.
     
     4. **Polymorphism** − The word polymorphism means having many forms. Typically, polymorphism occurs when there is a hierarchy of classes and they are related by inheritance. C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.
