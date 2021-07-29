# all valid syntax

```py
except ZeroDivisionError:
  print('')

except (ZeroDivisionError):
  print('')

except ZeroDivisionError as e:
  print(e)

except (ZeroDivisionError, ValueError) as e:
  print(e)

## default is

except:
```
