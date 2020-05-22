
"""
Example: function for scraping lyrics

def scrape_lyrics(artist):
    ...
    return songs

assert len(scrape_lyrics("Ed Sheeran")) > 0
assert len(scrape_lyrics("false")) == 0

Assumption that our program is correct:

We see that all assertions pass:
   Code OK, tests OK
   Code wrong, tests incomplete
   Code wrong, tests wrong

We see that an assertion fails:
   Code wrong, tests OK
   OR
   Code OK, tests wrong
   OR
   Code wrong, tests wrong
   --> proves that there is a problem.

Regression:
1. Write some code
2. Write a test for it (assertions)
3. Run *all* tests
4. Go back to 1

(regression - check whether our code is still working as before)
"""
import re

def count_words(s):
    return len(re.findall("\w+", s))

# 1. Make sure the following statement works
assert count_words("hello world") == 2

# 2. Make sure the following statement fails
assert count_words("in love with the shape of you") >= 3

# 3. Insert a string that does not result in 2
assert count_words("i love you") == 3

# 4. Check an empty string
assert count_words("") == 0

# 5. Check a string with lots of special characters
assert count_words("!§$%&/()=") == 0
assert count_words("! § $ % & / ( ) =") == 0
assert count_words("abc      def") == 2
assert count_words("ping-pong") == 2

# 6. Create a very long string (10000+ chars) and check it
s = "a " * 10000
assert count_words(s) == 10000

# 7. Call the function with a number


# 8. Create some tests functions which are run each time the code is run
# test the positive assertion
