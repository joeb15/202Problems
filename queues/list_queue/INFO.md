# Circular List Queues

The idea behind a circular list queue is that you will have a list of a given size and that will be the size of your queue  
For example, a queue of size 4 would look like this:

| 0 | 1 | 2 | 3 | 
|:-:|:-:|:-:|:-:|
|   |   |   |   |

front=0  
end=0

If you were to call *queue.enqueue(5)*, the resulting list will look like this

| 0 | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| 5 |   |   |   |

front=0  
end=1

Another call of *queue.enqueue(2)* would result in

| 0 | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| 5 | 2 |   |   |

front=0  
end=2

However, one thing to be sure of is that dequeueing should also increment your front  
A call of *queue.dequeue()* will result in

| 0 | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
|   | 2 |   |   |

front=1  
end=1  
returned 5


