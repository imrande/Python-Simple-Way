# Nested try-except block

```py
try:
    try:
        pass
    except:
        pass
    finally:
        pass
except:
    try:
        pass
    except:
        pass
    finally:
        pass
finally:
    try:
        pass
    except:
        pass
    finally:
        pass
```

We can take try-except-finally blocks inside try or except or finally. Hence nesting of try-except-finally blocks is possible.

General risky code we have to take inside outer try block and too much risky code we have to take inside inner try block.

Inside inner try block if an exception raised then inner except block is responsible to handle. If it is unable to handle then outer except block is responsible to handle.