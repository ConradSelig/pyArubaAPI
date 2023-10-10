# API Reference
### uiGetStatus


# Setting up Tests

For tests to work, you must be on a network that has access to an HP Aruba network switch. You'll also need credentials
for the switch.

Create a new file, _globals.py_ in the project directory. Your file structure should look like this:

```text
pyArubaAPI
├── .gitignore
├── globals.py     <-- This is the file you need to create.
├── pyArubaAPI.py
├── ...
└── README.md
```

_globals.py_ should contain the following, with your own details substituted for placeholder values:

```python
switch_ip = '192.168.0.2'
switch_username = 'manager'
switch_password = 'foobar'
```  