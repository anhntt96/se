### Why should we learn Go?
- Code run fast 
- Garbage collection
- Simpler objects
- Concurrency is efficient
  
### Code running fast
##### Understand Software Translation:

3 categories of languages:
- Machine language: CPU instructions, directly executed on CPU, represented in binary (1010)
- Assembly language: CPU instructions with mnemonics. 1:1 mapping with machine language. 
    - Easier to read
    - Equivalent to machine language
- High level language: C, C++, Java, Python,…
  - Much easier to use

All software must be translated into the machine language of processor.

##### Translation step:
There is 2 ways: Compiled or Interpreted.
- **Compiled**: translate instructions code once before running the code, save time. 
  - (C, C++, Java)
- **Interpreted:** translate instructions code while code is executed
  - translate occurs every execution (Python)
  - require an interpreter

This is a trade off between Compiled code and Interpreted code.
###### Efficiency and Ease-of-use
- Compiled code is fast
- Interpreters make coding easier
    - Manage memory automatically
    - Infer variable types
- Go is a good compromise

### Garbage collection
- Go includes garbage collection
    - Typically only done by interpreters.
- https://medium.com/safetycultureengineering/an-overview-of-memory-management-in-go-9a72ec7c76a8

### Object-Oriented Programming
- Organize your code through encapsulation
- Group together data and functions which are related.
- User-defined type which is specify for your application.
- Go use structs with associated methods
- Simplified implementation of classes
    - No inheritance
    - No constructors
    - No generics
- Easier to code

### Concurrency
- Performance Limits of Computer
    - Moore’s Law used to help performance
        - Number of transistors doubles every 18 months
    - More transistors used to lead to higher clock frequencies
    - Power/temperature constraints limit clock frequencies now

**How to improve performance?**

1. Parallelism
    - Number of cores in chips still increase over time
    - Multiple tasks may be performed at the same time on different cores.
    - Difficulties with parallelism
        - When do tasks start/stop?
        - What if one task need data from other tasks?
        - Do tasks conflict in memory?
2. Concurrent programming
    - Concurrency is the management of multiple tasks at the same time.
    - Key requirement for large systems.
    - Concurrent programming enables parallelism:
        - Management of tasks execution
        - Communication between tasks
        - Synchronization between tasks

**Concurrency in Go**
- Go include concurrency primitives
- **Goroutines** represent concurrent tasks.
- **Channels** are used to communicate between tasks
- **Select** enables task synchronization
- Concurrency primitives are efficient and easy to use