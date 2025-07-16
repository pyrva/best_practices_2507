def hello(name:str):
    return f'Hello, {name}'

def cli():
    import sys
    print(hello(sys.argv[1]))
