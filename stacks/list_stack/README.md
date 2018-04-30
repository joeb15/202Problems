# Stacks

Stacks are commonly used within programming, as they are a last in, first out list.

This means that the item that was added last will be popped off first

![][stack-image]

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

[stack-image]: https://moometric.com/wp-content/uploads/2015/10/stack1.png
