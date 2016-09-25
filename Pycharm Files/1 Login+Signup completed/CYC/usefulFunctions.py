
# to Create random keywords
import random,string
def tokenGenerator(length):
        return ''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase)for _ in range(length))

