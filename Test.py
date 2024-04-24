def my_function():
    print("Hello, I'm a function!")

# Function name as a string
function_name = "my_function"

# Call the function using globals()
if function_name in globals() and callable(globals()[function_name]):
    globals()[function_name]()

# Or using locals() if the function is in the current scope
if function_name in locals() and callable(locals()[function_name]):
    locals()[function_name]()