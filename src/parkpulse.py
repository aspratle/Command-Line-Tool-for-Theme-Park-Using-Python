"""
ParkPulse — Week 1

Project context:
ParkPulse helps amusement park staff quickly understand the current
status of an attraction.

Week 1 feature:
Use Python variables, expressions, and formatted output to calculate
and display one attraction's utilization.

Attraction data:
- Name: Sky Loop
- Maximum capacity: 24 riders
- Current riders: 20
- Open: yes
"""
#print(20/24)

# TODO 1:
# Store the attraction data above in clearly named variables.
name = "Sky Loop"
max_capacity = 20 
current_riders = 20
is_open = True

# Think about:
# - Which Python data type fits each value?
# - Which names follow snake_case?
# - Which value should be represented as a boolean?
def calculate_utilization(riders, capacity):
    return riders / capacity # / vs //(floor division)

utilization = calculate_utilization(current_riders, max_capacity)

def eligibility(visitor_height,minimum_height):
    """
    Determine whether a visitor is tall enough to ride.

    Parameters:
        visitor_height: The visitor's height in inches.
        minimum_height: The ride's minimum height in inches
            (Sky Loop: 48 inches).

    Returns:
        True if eligible, False if too short,
        None if an input is missing or invalid.

    Eligibility rule:
        - visitor_height >= minimum_height -> True
          (exactly 48 inches on Sky Loop is eligible)
        - visitor_height < minimum_height -> False
        - either value is None, 0, or negative -> None """
    #None Guard case 
    if visitor_height is None or minimum_height is None: 
        return None
    if visitor_height <= 0 or minimum_height <=0:
        return None
    #height rule
    if visitor_height < minimum_height or None: #if visitor_height >= minimum height return true 
        return False 
    return True 


def calculate_ticket_price(ticket_type, base_price):
    """
    Determine a ticket price from its category.

    Parameters:
        ticket_type: "adult", "child", or "senior"
            (lowercase, exactly as written).
        base_price: The adult price in dollars
            (ParkPulse uses $60.00).

    Returns:
        The price as a number, or None for an
        unknown category or an invalid base price.

    Pricing rules:
        - "adult"  -> 100% of base_price  ($60.00)
        - "child"  -> 50% of base_price   ($30.00)
        - "senior" -> 75% of base_price   ($45.00)
        - any other ticket_type -> None
        - base_price is None, 0, or negative -> None
    """
    if base_price is None or base_price <=0:
        return None 

    if ticket_type == "adult":
        return base_price
    elif ticket_type == "child":
        return base_price * 0.5
    elif ticket_type == "senior":
        return base_price * 0.75 
    else:
        return None



utilization = current_riders / max_capacity
print(utilization)

# Utilization means:
# current riders divided by maximum capacity
#
# Before running your code, predict the type and value
# of the expression you write.


# TODO 3:
# Use print() and an f-string to display a readable status message.
print(f"Utilization is: {utilization:.2%}")
# Your message should include:
# - the attraction name
# - its utilization as a percentage
# - whether the attraction is open


# TODO 4:
# Review your code before you finish.
#
# Check:
# - snake_case variable names
# - spaces around operators
# - four-space indentation if you use indentation
# - no unnecessary semicolons or braces