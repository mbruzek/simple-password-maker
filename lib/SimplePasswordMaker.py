"""
SimplePasswordMaker creates passwords with hash functions.

Copyright 2016 Matthew Bruzek

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import hashlib
import string
import sys


class SimplePasswordMaker:
    """Main class used for generating passwords."""
    # The default charset is uppercase + lowercase + digits + punctuation
    CHARSET = string.ascii_uppercase + string.ascii_lowercase + \
        string.digits + string.punctuation

    def generate_password(self, algorithm, master, data, length, charset):
        """Generate the password using the provided hash algorithm."""
        self.verify_algorithm(algorithm)
        hash = hashlib.new(algorithm)
        # Add the master to the hash data.
        hash.update(master.encode('utf-8'))
        # Add the data to the hash algorithm.
        hash.update(data.encode('utf-8'))
        digest = hash.digest()
        digest_length = len(digest)
        pwd_len = int(length)
        # Can not make the password any longer than the digest bytes.
        if pwd_len > digest_length:
            pwd_len = digest_length
        # Return a string with characters only from the charset.
        return ''.join(charset[digest[a] % len(charset)] for a in range(pwd_len))  # noqa

    def verify_algorithm(self, algorithm):
        """Verify that the hash algorithm is valid."""
        if sys.version[:5] >= '2.7.9':
            algorithms = hashlib.algorithms_available
        else:
            algorithms = hashlib.algorithms
        # Ensure the hash algorithm exists the available algorithms.
        if algorithm in algorithms:
            return True
        else:
            raise ValueError('Invalid hash algorithm "{0}"'.format(algorithm))
