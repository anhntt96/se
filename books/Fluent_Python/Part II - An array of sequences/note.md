*Container sequences*

`
list , tuple , and collections.deque can hold items of different types.
`

*Flat sequences*

`
str , bytes , bytearray , memoryview , and array.array hold items of one type.
`

*Container sequences* hold references to the objects they contain, which may be of any
type, while *flat sequences* physically store the value of each item within its own memory
space, and not as distinct objects. Thus, flat sequences are more compact, but they are
limited to holding primitive values like characters, bytes, and numbers.