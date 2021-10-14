'''
-- These are the variables whose values are only known to the local system we're working on, and not visible in the actual code.
-- These have 2 benefits:
    1) changing value of the variable becomes easy as all important variables are bundled at a common place.
    2) keeps classified information (eg: api keys) hidden if someone views our raw code (like on github).
'''

# in terminal write : export OWM_API_KEY=69f04e4613056b (make sure no space before and after "=" sign)
# now in terminal write: env ----------> above key will pop up.
#to use this variable further in your code:
import os
api_key = os.environ.get("OWM_API_KEY")
