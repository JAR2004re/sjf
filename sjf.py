def sjf(processes, n):
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[0])

    execution_order = []
    current_time = 0
    total_waiting_time = 0

    while len(processes) > 0:
        # Get all processes that have arrived by the current time
        available_processes = [p for p in processes if p[0] <= current_time]

        if len(available_processes) == 0:
            # If no processes have arrived, move to the next arrival time
            current_time = processes[0][0]
        else:
            # Sort available processes based on their burst time
            available_processes.sort(key=lambda x: x[1])

            # Select the process with the shortest burst time
            shortest_job = available_processes[0]

            # Update current time to include the burst time of the selected job
            current_time += shortest_job[1]
            # Calculate waiting time for the selected job
            total_waiting_time += current_time - shortest_job[0] - shortest_job[1]
            # Record the execution order
            execution_order.append(shortest_job[2])

            # Remove the executed process from the list
            processes.remove(shortest_job)

    # Calculate the average waiting time
    average_waiting_time = total_waiting_time / n

    return execution_order, average_waiting_time

if __name__ == "__main__":
    # List of processes: (arrival_time, burst_time, process_id)
    processes = [(0, 6, 'P1'), (1, 8, 'P2'), (2, 7, 'P3'), (3, 3, 'P4')]
    num_processes = len(processes)

    execution_order, avg_waiting_time = sjf(processes, num_processes)

    print("Execution order:", execution_order)
    print("Average waiting time:", avg_waiting_time)
