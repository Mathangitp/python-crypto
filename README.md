crypto
======

Python library for simply text cryptography.

Authors
-------
*  Ondrej Sika, <http://ondrejsika.com>, dev@ondrejsika.com

Source
------
* Documentation: <http://ondrejsika.com/docs/python-crypto>
* Python Package Index: <http://pypi.python.org/pypi/crypto>
* GitHub: <https://github.com/sikaondrej/python-crypto>

Documentation
=============

Instalation
-----------

Instalation is very simple over pip.
    # pip install crypto

Functions
---------

### Generate keys pair
    import crypto
    key_length = 256
    public, private = crypto.newkeys(key_length)

### Export key to string, file
    public_string = crypto.export_key(public)  # export key to string
    crypto.export_key_file(public, "id_rsa.pub")  # expo key to string

### Load key to string, file
    public = crypto.load_key(public_string)  # load key from string
    private = crypto.load_key_file("id_rsa.pub")  # load key from string

### Encrypt to bin
    message = "My secret message"
    encrypted = crypto.encrypt(message, public)

### Decrypt from bin
    message = crypto.decrypt(encrypted, private)

### Encrypt to string
    message = "My secret message"
    encrypted = crypto.encrypt_str(message, public)

### Decrypt from string
    message = crypto.decrypt_str(encrypted, private)