
# 17.2 Schedule to minimize wating Time
# the time complexity is dominated by the time to sort, i.e., O(nlogn)

def minimum_total_waiting_time(service_times):
    # sort the service times in increasing order
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times)-(i+1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


print(minimum_total_waiting_time([2, 5, 1, 3]))
