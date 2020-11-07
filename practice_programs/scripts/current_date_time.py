#!/usr/bin/env python3

###############################################################################
# File          : current_date_time.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 07 Nov, 2020
# Updated       : 07 Nov, 2020
# Description   : A script to display current date and time.
################################################################################

# Import modules.

import datetime

# Display current date and time.

now=datetime.datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")