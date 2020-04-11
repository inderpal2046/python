#!/usr/bin/env python3

# This script will accept user input as CLI arguments and perform a desired action.
# This scripts works in same way as interactive_string_actions.py but user doesn't interact with this script during its runtime.
# But user provides input at CLI
# CLI arguments can be used to capture user input or provide vars as input without interaction and can help in automation.

import sys

if len(sys.argv)==1:
    print(f"Correct script usage : {sys.argv[0]} \"input string\" \"action\"")
    print(f"input string is the string on which operation is going to be performed.")
    print(f"action can take values as [lower|upper|title|swapcase]")
    sys.exit(1)

# It is useful to assign CLI argument values to new vars in the script as below.
# In this way I don't have to mention sys.argv[1]/[2]/etc everywhere.
# And any changes in future to the arg values will have to be done at one place only and not at all places.
user_input=sys.argv[1]
user_action=sys.argv[2]

if user_action=="lower":
    print(f"{user_input.lower()}")
elif user_action=="upper":
    print(f"{user_input.upper()}")
elif user_action=="title":
    print(f"{user_input.title()}")
elif user_action=="swapcase":
    print(f"{user_input.swapcase()}")
else:
    print(f"Invalid input action. Please provide [lower|upper|title|swapcase] as user action values.")
