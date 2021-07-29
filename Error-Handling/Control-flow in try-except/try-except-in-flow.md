```py
try: -> main flow
    statement-1
    statement-2
    statement-3
except xxx: [corresponding errors] alternative flow
    statement-4
statement-5
```

1. if there is no errors in program which statement will be executed?
- 1, 2, 3, 5
2. if errors in 2, which statement will be executed?
- 1, 4, 5
3. if erros in sta-2 and no matched exception code which statemtn will be executed?
- 1, abnormal termination
4. if an errors raise sta - 4 or 5
- any exception outside of try block always abnormal termination
- abnormal termination

```py
# best practice for it ==>
statement - 1
statement - 2
statement - 3
try:
    statement - 4  # could raise exception
except xxx:
    # alternative flows
    exception code
statement - 5
```
