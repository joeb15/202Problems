# Stacks

Stacks are commonly used within programming, as they are a last in, first out list.

This means that the item that was added last will be popped off first

![Stack Design](stack)

For example, a stack of size 3 would look like this:

| 0 | 1 | 2 |
|:-:|:-:|:-:|
|   |   |   |

Now, if I were to push the letter 'c' to the stack, it would look like this:

| 0 | 1 | 2 |
|:-:|:-:|:-:|
| c |   |   |

Pushing another thing, for instance, 'q', would look like this:

| 0 | 1 | 2 |
|:-:|:-:|:-:|
| c | q |   |

*Peeking* at the stack would return 'q' **without** modifying the stack at all.

However, *popping* from the stack will return 'q' with the new stack looking like this:

| 0 | 1 | 2 |
|:-:|:-:|:-:|
| c |   |   |

[stack]: http://img.c4learn.com/2010/02/Stack-Operation-in-C-Programming.jpg
