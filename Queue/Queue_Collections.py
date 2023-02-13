from collections import deque
customQueue = deque(maxlen=10)
for i in range(11):
    customQueue.append(i)


print(customQueue.popleft())
print(customQueue)

print(customQueue.clear())
print(customQueue)