# Hello World from C++
A "Hello World" c++ program.

Our first C++ program is a program called "Hello World", which simply prints "Hello World" to your computer screen.
Brian Kernighan wrote the first "Hello, World!" while he was developing the C language at Bell Labs.

## I - Install Dev-C++

Visit this [link](https://sourceforge.net/projects/orwelldevcpp/) to download and install Dev-C++ which is a C++ IDE. We will be writing, compiling and running our first programs there.

## II - "Hello World" program

Open a new source file, copy/paste the program below in there and click Compile & Run (F11). This program is also available in the folder `hello-world`.

```
  #include <iostream>

  int main()
  {
    std::cout << "Hello World!";
  }
```

You should have a result that looks like this:

![hello world result](https://github.com/elmimouni/tutorials/blob/master/c%2B%2B/hello-world/hello_world_result.png)

## III - Let's examine this program

**Line 1**: `#include <iostream>` is a special instruction (called directive) that tells our *computer* to include a part of C++ code which, in this case, is named *header iostream*. This insrtuction allows our program to perform standard input and output operations, such as writing "Hello World!".

**Line 2**: is blank, and blank lines are ignored by the program.

**Line 3**: `int main()` declares a function called `main` that returns a type `int`. The function *main* is a special; it is the function called when the program is run. Which means that **your program always starts its execution from the function main**.

**Line 4 and 6**: `{` and `}` they indicate the begining and the end of a function, in this case, the main function.

**Line 5**: `std::cout << "Hello World!";` is an instruction or statement. A statement is an instruction that has some effect. This line is responsible for displaying the message to you computer screen.

We will dive in more details about this program later...
