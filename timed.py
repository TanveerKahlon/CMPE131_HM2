# Import time
import time

# defining a decorator
def timeme(func):
    # inner1 is a Wrapper function in
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        # Store start time
        begin = time.time()
    
        # calling the actual function now
        # inside the wrapper function.
        timer()
        
        # Store end time
        end = time.time()
    
        # Print total time taken
        print("Total time ",end - begin)
    return inner1
  
 
# defining a function, to be called inside wrapper
def timer():
    time.sleep(2)
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behavior
function = timeme(timer)
 
 
# calling the function
function()