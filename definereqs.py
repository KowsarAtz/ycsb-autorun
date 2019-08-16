a = [
    'Throughput',
    'READ.*AverageLatency',
    'READ.*95thPercentileLatency',
    'READ.*99thPercentileLatency',
    'UPDATE.*AverageLatency',
    'UPDATE.*95thPercentileLatency',
    'UPDATE.*99thPercentileLatency'
]
a2 = [
    '       | Throughput            | ',
    'READ   | AverageLatency        | ',
    'READ   | 95thPercentileLatency | ',
    'READ   | 99thPercentileLatency | ',
    'UPDATE | AverageLatency        | ',
    'UPDATE | 95thPercentileLatency | ',
    'UPDATE | 99thPercentileLatency | '
]

b = a
b2 = a2

c = [
    'Throughput',
    'READ.*AverageLatency',
    'READ.*95thPercentileLatency',
    'READ.*99thPercentileLatency'
]
c2 = [
    '       | Throughput            | ',
    'READ   | AverageLatency        | ',
    'READ   | 95thPercentileLatency | ',
    'READ   | 99thPercentileLatency | '
]

d = [
    'Throughput',
    'READ.*AverageLatency',
    'READ.*95thPercentileLatency',
    'READ.*99thPercentileLatency',
    'INSERT.*AverageLatency',
    'INSERT.*95thPercentileLatency',
    'INSERT.*99thPercentileLatency'
]
d2 = [
    '       | Throughput            | ',
    'READ   | AverageLatency        | ',
    'READ   | 95thPercentileLatency | ',
    'READ   | 99thPercentileLatency | ',
    'INSERT | AverageLatency        | ',
    'INSERT | 95thPercentileLatency | ',
    'INSERT | 99thPercentileLatency | '
]

e = [
    'Throughput',
    'SCAN.*AverageLatency',
    'SCAN.*95thPercentileLatency',
    'SCAN.*99thPercentileLatency',
    'INSERT.*AverageLatency',
    'INSERT.*95thPercentileLatency',
    'INSERT.*99thPercentileLatency'
]
e2 = [
    '       | Throughput            | ',
    'SCAN   | AverageLatency        | ',
    'SCAN   | 95thPercentileLatency | ',
    'SCAN   | 99thPercentileLatency | ',
    'INSERT | AverageLatency        | ',
    'INSERT | 95thPercentileLatency | ',
    'INSERT | 99thPercentileLatency | '
]

f = [
    'Throughput',
    'READ.*AverageLatency',
    'READ.*95thPercentileLatency',
    'READ.*99thPercentileLatency',
    'READ-MODIFY-WRITE.*AverageLatency',
    'READ-MODIFY-WRITE.*95thPercentileLatency',
    'READ-MODIFY-WRITE.*99thPercentileLatency'
]
f2 = [
    '                  | Throughput            | ',
    'READ              | AverageLatency        | ',
    'READ              | 95thPercentileLatency | ',
    'READ              | 99thPercentileLatency | ',
    'READ-MODIFY-WRITE | AverageLatency        | ',
    'READ-MODIFY-WRITE | 95thPercentileLatency | ',
    'READ-MODIFY-WRITE | 99thPercentileLatency | '
]


def definereqs(workload):
    
    reqs = None
    reqs2 = None 

    if workload == 'a':
        reqs = a
        reqs2 = a2
    elif workload == 'b':
        reqs = b
        reqs2 = b2
    elif workload == 'c':
        reqs = c
        reqs2 = c2
    elif workload == 'd':
        reqs = d
        reqs2 = d2
    elif workload == 'e':
        reqs = e
        reqs2 = e2
    elif workload == 'f':
        reqs = f
        reqs2 = f2

    return (reqs, reqs2)