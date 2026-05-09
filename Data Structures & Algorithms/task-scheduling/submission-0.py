class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Creates maxHeap of letter frequencies
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Stores frequency of letter and idle time
        q = deque()  
        time = 0    

        # Keep processing as long as one is not empty
        while maxHeap or q:
            time += 1
            if maxHeap:
                # Decreases frequency by 1 (Add 1 since frequency is negative)
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    # Add idle time to current time of value
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                popped_count = q.popleft()[0]
                heapq.heappush(maxHeap, popped_count)
        
        return time

                