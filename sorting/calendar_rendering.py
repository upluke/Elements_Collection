# 13.5 Render a calendar
# sorting the endpoint array takes O(nlogn) time; iterating through the sorted array takes O(n) time, yielding an O(nlogn)time complexity. The space complexity is O(n), which is the size of the endpoint array.
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

#lc:
import heapq

def maxEvents(A):
    A.sort(reverse=1)
    h = []
    res = d = 0
    while A or h:
        if not h: 
          d = A[-1][0]
        while A and A[-1][0] <= d:
          heapq.heappush(h, A.pop()[1])
        heapq.heappop(h)
        res += 1
        d += 1
        while h and h[0] < d:
            heapq.heappop(h)
    return res

print(maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])) # 4

# element (w/ error):
import collections
import functools
 
# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
    # are equal, start_time comes first
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    
    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events

print(find_max_simultaneous_events([[1,4],[4,4],[2,2],[3,4],[1,1]])) # 4
 