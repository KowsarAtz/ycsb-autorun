import re

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
a3 = [
    ('-','Throughput'),
    ('READ','AverageLatency'),
    ('READ','95thPercentileLatency'),
    ('READ','99thPercentileLatency'),
    ('UPDATE','AverageLatency'),
    ('UPDATE','95thPercentileLatency'),
    ('UPDATE','99thPercentileLatency')
]

b = a
b2 = a2
b3 = a3

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
c3 = [
    ('-','Throughput'),
    ('READ','AverageLatency'),
    ('READ','95thPercentileLatency'),
    ('READ','99thPercentileLatency')
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
d3 = [
    ('-','Throughput'),
    ('READ','AverageLatency'),
    ('READ','95thPercentileLatency'),
    ('READ','99thPercentileLatency'),
    ('INSERT','AverageLatency'),
    ('INSERT','95thPercentileLatency'),
    ('INSERT','99thPercentileLatency')
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
e3 = [
    ('-','Throughput'),
    ('SCAN','AverageLatency'),
    ('SCAN','95thPercentileLatency'),
    ('SCAN','99thPercentileLatency'),
    ('INSERT','AverageLatency'),
    ('INSERT','95thPercentileLatency'),
    ('INSERT','99thPercentileLatency')
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
f3 = [
    ('-','Throughput'),
    ('READ','AverageLatency'),
    ('READ','95thPercentileLatency'),
    ('READ','99thPercentileLatency'),
    ('READ-MODIFY-WRITE','AverageLatency'),
    ('READ-MODIFY-WRITE','95thPercentileLatency'),
    ('READ-MODIFY-WRITE','99thPercentileLatency')
]


def definereqs(workload):
    reqs = None
    reqs2 = None 
    reqs3 = None
    if workload == 'a':
        reqs = a
        reqs2 = a2
        reqs3 = a3
    elif workload == 'b':
        reqs = b
        reqs2 = b2
        reqs3 = b3
    elif workload == 'c':
        reqs = c
        reqs2 = c2
        reqs3 = c3
    elif workload == 'd':
        reqs = d
        reqs2 = d2
        reqs3 = d3
    elif workload == 'e':
        reqs = e
        reqs2 = e2
        reqs3 = e3
    elif workload == 'f':
        reqs = f
        reqs2 = f2
        reqs3 = f3

    return (reqs, reqs2, reqs3)

def meansfilenumbers(base_path, dbname, workload, rec_count, op_count, thrd_count):
    filename = base_path + '/' + dbname + '/' + workload + '/rc' + \
        str(rec_count) + '-op' + str(op_count) + \
        '/tc' + str(thrd_count) + '/means.txt'
    result = []
    wl = definereqs(workload)[0]
    for rq in wl:
        gp = re.search(r""+rq+".*?(\d*\.\d*)", open(filename, "r").read())
        result += [(definereqs(workload)[2][wl.index(rq)] , float(gp.group(1)))]
    return result