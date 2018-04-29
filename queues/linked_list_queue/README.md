# Priority/Linked List Queues

The priority queue is often used in real world examples of queues as it allows for items to be prioritized in a list

For example, one could view a hospital as a priority queue

Lets say that I checked in with a broken toe:

| Person | Condition | Priority |
|:------:|:---------:|:--------:|
|  Joe   | Broken Toe|  MEDIUM  |
|        |           |          |

Now lets say that someone else was rushed in with a cough:

| Person | Condition | Priority |
|:------:|:---------:|:--------:|
|  Joe   | Broken Toe|  MEDIUM  |
| Johnny |   Cough   |   LOW    |
|        |           |          |

However, if someone was then rushed in with a heart attack:

| Person | Condition | Priority |
|:------:|:---------:|:--------:|
| Benny  |Heart Attack|  HIGH   |
|  Joe   | Broken Toe|  MEDIUM  |
| Johnny |   Cough   |   LOW    |
|        |           |          |

**Notice** that the person with a heart attack is now set at the top of the queue, as their condition is most dire

If we were to now *dequeue* from this list, Benny would be the person that is first

This set up is inefficient to implement by pushing items between other ones, so Computer Scientists like to use linked lists for this:

The structure of the queue code:
* We will only be worrying about the priority of the item being pushed
* Each item being added will be in the form of a node  
> Each node will contain  
    > Data (the priority)  
    > Previous node(If it has one)  
    > Next node(If it has one)
> **Note**
    > The *first* node is called the head and the *last* is called the tail  
    > If there are zero items in the queue, the head and tail will be of type None  
    > If there is one item in the queue, the head and tail will both be the only node
* Due to each node having a previous and a next node, the index of the nodes in the list does NOT matter
* You are allowed to use *append* and *remove* for the list
