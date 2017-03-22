# Simple Password Maker

Use the python hash methods to generate passwords for input values and options.

# Usage

To run the script interactively:
```bash
./simple_password_maker.py
```

Or run the program with the flags:
```bash
./simple_password_maker.py -a sha256 -m password -r github.com -u user -d modifier -g 20 -c 0123456789abcdef
```

Use the `-h` or `--help` flag for usage and description of the flags:
```bash
./simple_password_maker.py -h
```

# License

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

# Caveat

This program was only written to sharpen my python skills. I am not a
cryptography expert, and this technique has not been reviewed by one. I do not
use this program to generate my passwords, and neither should you.
