from collections import deque
from multiprocessing import Queue

q = deque(maxlen=3)

print(q)

q.append(1)
q.append(2)
q.append(3)
q.popleft()
print(q)
q.clear()
print(q)



c = Queue(maxsize=3)
print(c)

c.put(1)
c.put(2)
print(c.get())