# Interview question Finally vs Destructor

## Finally block

Finally block meant for cleanup activities related to try block. whatever resources we opened as the part of try block will be closed inside finally block.

## Destructor

Destructor meant for cleanup activities related to objects. Whatever resources associated with the object should be deallocated inside destructor, which will be executed before destroying object.