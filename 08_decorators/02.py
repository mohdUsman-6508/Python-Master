
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = (", ").join(str(arg) for arg in args)
        kwargs_value = (", ").join(str(f"{k} {v}") for k,v in kwargs.items())
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        result = func(*args,**kwargs)
        return result
    return wrapper


@debug
def sayHello():
    print("Hello!")
    
@debug
def greet(name, greeting="Hello!"):
    print(f"{greeting},{name}")
    
sayHello()
greet("Python",greeting="Welcome!")