# BASH Limits
What are good indicators your BASH script has become too complex and you should stop to re-implement your system in a "real" language?

### Index
1. ["Real" Languages](#real-languages)
    1. [Examples](#examples)
1. [Red Flags](#red-flags)
1. [Process](#process)

## "Real" Languages
BASH is a real language, a Turing-complete, interpreted scripting language. This is why "real" is in quotes throughout this document.

However, it's important to note that while BASH is Turing-complete, it is not a general-purpose programming language and it's not designed to be used for large, complex projects or for tasks that require advanced features like object-oriented programming, closures, currying, etc.

> Throughout this document, when I have referred to "real" languages, I have been using it to refer to programming languages that are typically used for general-purpose programming and have a large number of features and capabilities. These languages are generally more versatile and expressive than languages like BASH which are primarily used for system administration and command-line scripting.
>
> These languages are designed to be used for a wide range of tasks, from web development and data processing to machine learning and artificial intelligence. They are also more suited for large, complex projects, and have more robust tools for debugging, testing, and deploying code. They often provide support for object-oriented, functional and other programming paradigms, and have a larger user base and libraries.
>
> In contrast, BASH is a command-line scripting language that is primarily used for system administration and automating tasks. It's a powerful tool for working with the command-line and performing tasks like text processing, file management, and process management. But when it comes to more advanced features like object-oriented programming, closures, currying, etc. it lacks the capabilities of "real" languages.
>
> It's important to note that BASH can be used in conjunction with other languages, like Python, to accomplish more complex tasks and to be more expressive, but when the task becomes too complex or the codebase becomes too big, it's better to use a more powerful language that is better suited for the task.

### Examples
Examples of "real" languages.
- C#
- C++
- Go
- Haskell
- Java
- JavaScript
- Python
- Rust

Which languages specifically are acceptable in our repos or organization is a wholly different discussion for a different document.

## Red Flags
Here are some suggestions.
1. **Too Many Lines of Code**.
1. **Complex mathematical calculations**.
    > BASH was designed to be a shell scripting language and, while it can perform basic arithmetic operations, it is not well suited for complex mathematical computations. BASH has limited support for floating-point arithmetic, and it is prone to loss of precision and rounding errors. Additionally, the syntax for performing mathematical operations in BASH is less convenient and less expressive than in other programming languages that were specifically designed for numerical computations. For these reasons, it is generally recommended to use a specialized language for complex mathematical operations.
    - Floating point (decimal) operations.
    - Math operations invoking tools like `bc` or `dc` where the output must be known beforehand to correctly configure the tool.
        ```bash
        echo 'scale=4; 23/8' | bc
        ```
    - Math operations invoking a "real" language runtime from BASH.
        ```bash
        node -e 'console.log(23/8)'
        python3 -c 'print(23/8)'
        perl -e 'print 23/8'
        ```
1. **Complex string manipulation**, especially constructing files using repeated heredocs or `echo >>` statements, trying to construct JSON files without `jq`, trying to construct YAML files without `yq`, or constructing more complicated file types.
1. **Changing the internal field separator (IFS)**.
1. **Types or type safety** - if you need it, BASH does not have it.
1. **Exception handling** such as using `trap`, or using libraries providing try-catch functionality.
1. **Complex API interaction**, specifically API interaction involving:
	- Pagination
	- Rate-Limits
	- Error Handling
	- Backoff or Automatic Retries
	- Caching
1. **Input Validation** - if you are parsing untrusted input, use a "real" language...especially if these inputs are eventually consumed by `eval`, `exec`, `command`, or subshells with backticks (`` ` ` ``) or the more modern `$()` syntax.
1. **Extremely Large Datasets**.
	- BASH does not have memory management or garbage collection.
	- Variables and arguments have a size limit based on the memory of a machine, which is not necessarily deterministic.
	- BASH utilities have their own limits. For example, `sed` on BSD and macOS can only operate on files of 4 MB or less.
	- Working with large datasets in BASH can cause scripts to become extremely slow.
	- "Real" languages allow an engineer to predict these limits and performance on large datasets much more accurately, even independent of a specific host machine's hardware.
1. **Concurrency** - use a "real" language for multithreading or parallelization.
1. **Functional Programming Concepts**.
    > When you start implementing or approximating functional programming concepts such as recursion, currying, partial application, etc. which are not natively supported by BASH, it can become increasingly difficult to implement, test and understand the code. Additionally, implementing functional programming concepts in BASH can also make the script less performant, as BASH is not designed to handle complex functional concepts.  BASH is better suited for simple scripts and system administration tasks. While it is possible to use some functional programming concepts in BASH, it's not recommended to push the limits of BASH capabilities and to use a more suitable language for more complex programming needs instead.
    1. **Recursion** - functions which call themselves.
        > Recursion can be a powerful tool, but it can also be memory-intensive, as each recursive call creates a new function call frame on the call stack. In addition, recursion can be less efficient than an iterative solution for large inputs and can cause a stack overflow error.
        ```bash
        function factorial {
            if [[ $1 -eq 1 ]]; then
                echo 1
            else
                local result=$(( $1 * $(factorial $(( $1 - 1 ))) ))
                echo $result
            fi
        }

        factorial 5  # 120
        ```
    1. **Higher-Order Functions** - functions which take a function as an argument or return a function as a result.
        > Higher-order functions require a more sophisticated type system and language constructs than what BASH provides, making the implementation more complex, difficult to understand and maintain.
        - In BASH, you would be passing around names of functions.
        ```bash
        function add {
            echo $(( $1 + $2 ))
        }

        function multiply {
            echo $(( $1 * $2 ))
        }

        function calculate {
            local operation=$1
            shift
            $operation $@
        }

        calculate add 5 3  # 8
        calculate multiply 5 3  # 15
        ```
    1. **Currying** - where your function has completely different behavior depending on how many arguments are passed, a type of polymorphism.
        - Example in Haskell.
            ```haskell
            add :: Int -> Int -> Int
            add x y = x + y

            add5 :: Int -> Int
            add5 = add 5

            main = print (add5 3)  -- 8
            ```
        - Example in JavaScript.
            ```js
            const add = x => y => x + y;
            const add5 = add(5);
            console.log(add5(3));  // 8
            ```
        - Example in Python.
            ```python
            from functools import partial

            def add(a, b):
                return a + b

            add_5 = partial(add, 5)

            print(add_5(3))  # 8
            ```
        - Another example in Pythin using closure and higher-order functions instead of partial application.
            ```python
            def curry(f):
                def curried(*args, **kwargs):
                    if len(args) + len(kwargs) >= f.__code__.co_argcount:
                        return f(*args, **kwargs)
                    return lambda *args2, **kwargs2: curried(*(args + args2), **{**kwargs, **kwargs2})
                return curried

            @curry
            def add(x, y):
                return x + y

            add5 = add(5)

            print(add5(3))  # 8
            ```
        - Example attempting this in BASH.
            ```bash
            function add {
                local x=$1
                local y=$2
                echo $((x + y))
            }

            function curried_add {
                local x=$1
                if [[ $# -eq 1 ]]; then
                    echo "add $x \$1"
                else
                    echo $(add $x $2)
                fi
            }

            add_5=$(curried_add 5)
            $add_5 3  # 8
            ```
    1. **Partial Application** - where a function is called with fewer arguments than it is defined to take, returning a new function that takes the remaining arguments.
        > Stated another way, partial application is where you have some function 𝑓 and you derive some other function 𝑓' that is called with fewer arguments, then 𝑓' turns around and invokes 𝑓 with all arguments. Partial application is a functional concept distinct from default parameter values. There is nothing wrong with using default values for function parameters.
        - Example in Haskell.
            ```haskell
            add :: Int -> Int -> Int
            add x y = x + y

            add5 :: Int -> Int
            add5 = add 5

            main = print (add5 3)  -- 8
            ```
        - Example in JavaScript.
            ```js
            const add = (x, y) => x + y;
            const add5 = add.bind(null, 5);
            console.log(add5(3));  // 8
            ```
        - Example in Python.
            ```python
            def add(x, y):
                return x + y

            add5 = lambda y: add(5, y)

            print(add5(3))  # 8
            ```
        - Example attempting this in BASH.
            ```bash
            function add {
                echo $(( $1 + $2 ))
            }

            function partial_add {
                local x=$1
                echo "add $x \$1"
            }

            add_5=$(partial_add 5)
            $add_5 3  # 8
            ```
            > It's important to note that this is not a proper implementation of partial application. The returned string is not a function, it's just a string, and it's not a secure way to run commands. Additionally, BASH does not have closures, so it's not possible to have a function that closes over variables and maintains the state of the variable as it was at the time the outer function returned.
1. **Object-Oriented Concepts** - if you are trying to implement object-oriented concepts, use a "real" language.
    > BASH was not designed to be an object-oriented language, and implementing object-oriented concepts in BASH is difficult, convoluted, and often error-prone. This is because BASH is a shell scripting language meant primarily for running commands and creating simple scripts, rather than a high-level programming language with features for complex logic and data structures. When object-oriented concepts are attempted in BASH, it usually results in verbose and less readable code, which can be harder to maintain and less secure. In such cases, it is often better to use a "real" programming language that was designed with these features in mind.
	- Using global variables to simulate object properties.
	- Using functions to simulate object methods.
	- Using associative arrays to simulate object properties and methods.
	- Using command substitution and string concatenation to build object-like structures.
	```bash
	# define the class
	class_name=MyClass
	declare -A $class_name

	# define properties and methods
	$class_name[property1]=value1
	$class_name[property2]=value2
	$class_name[method1]="echo property1 is ${$class_name[property1]}"

	# create an instance of the class
	instance_name=instance1
	eval $instance_name=\($class_name\)

	# access properties and methods
	echo ${$instance_name[property1]}
	${$instance_name[method1]}
	```

## Process
At the 2023-01-24 ENF Engineering Weekly Meeting, the team decided that these indicators are reasonable and they should be used as guidelines for engineers to stop writing in BASH, but it is not a mandate. If two or more engineers feel a BASH system has reached this level of complexity and there is contention about re-implementing it in a "real" language, they can escalate it to the Engineering team for discussion and to make a formal decision one way or the other.

***
**_Legal notice_:**  
This document was generated in collaboration with the 2023-01-09 version of ChatGPT from OpenAI, a machine learning algorithm or weak artificial intelligence (AI). At the time of this writing, the [OpenAI terms of service agreement](https://openai.com/terms) §3.a states:
> Your Content. You may provide input to the Services (“Input”), and receive output generated and returned by the Services based on the Input (“Output”). Input and Output are collectively “Content.” As between the parties and to the extent permitted by applicable law, you own all Input, and subject to your compliance with these Terms, OpenAI hereby assigns to you all its right, title and interest in and to Output.

This notice is required in some countries.
