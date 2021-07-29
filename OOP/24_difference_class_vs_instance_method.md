| Instance Method      | Class Method |
| ----------- | ----------- |
| Inside method if we are using at least one instanceVariable then we can call it instance method     | Inside method if we are using at least one classVariable then we can call it class method       |
| we can access both classVariable(by using ClassName) or instanceVariable   | we can access only class variables inside method       |
| first argument is always self   | first argument is always cls       |
| No decorator is required   | decorator `@classmethod` is required        |
| call by object reference   | call by ClassName or object reference but className is recommended        |