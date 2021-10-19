"""Examples of importing other modules."""

from lessons import helpers

# Aliasing an import
from lessons import helpers as hp

# Import a function definition
from lessons.helpers import powerful

# Import a global/constant value
from lessons.helpers import THE_ANSWER

print(f"imports.py {__name__}")
print(helpers.powerful(2, 4))
print(helpers.THE_ANSWER)

# Using the alias hp (same as helpers)
print(hp.powerful(2, 5))

# Use the powerful function directly
print(powerful(2, 6))

# Use an imported constant directly
print(THE_ANSWER)