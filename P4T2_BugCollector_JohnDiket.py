# Bug Collector Video Project
#
# March 11, 2019
# CTI-110 P4T2 - Bug Collector
# John Diket
#

# Initialize the accumulator.
total = 0

# Get bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')

input()
