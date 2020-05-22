from words import count_words

# 1. Make sure the following statement works
def test_hello():
    assert count_words("hello world") == 2

# 2. Make sure the following statement fails
def test_shape():
    assert count_words("in love with the shape of you") == 7

# 3. Insert a string that does not result in 2
assert count_words('these are four words') == 4

# 4. Check an empty string
assert count_words("") == 0

# 5. Check a string with lots of special characters
assert count_words('What the hell does $%& mean?') == 5

# 6. Create a very long string (10000+ chars) and check it
s = ['s'] * 1000
assert count_words(' '.join(s)) == 1000

# 7. Call the function with a number
try:
    count_words(777)
    assert False
except:
    assert True
