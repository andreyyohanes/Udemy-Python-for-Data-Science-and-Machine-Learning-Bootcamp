# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    _speed = speed    
    if is_birthday:
        _speed -= 5
        
    if _speed <= 60:
        return "No Ticket"
    elif _speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"
