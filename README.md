catchall-generator
=============
Generate randomized emails for your catchall adress.

Installation
------------
```
pip install git+https://github.com/joelcloud/catchall-generator
```

Usage
------------
```py
from catchall_generator import Catchall

catchall = Catchall('@mycatchall.com')

>>> catchall.generate()
'alan.z.rodriguez@mycatchall.com'

>>> catchall.generate_male()
'johnlove985@mycatchall.com'

>>> catchall.generate_female()
'kathrynbrooks@mycatchall.com'
```