def solution(id_list, report, k):
    record = {}    
    for r in report:
        reporter, reported = r.split()
        if reporter not in record:
            record[reporter] = {reported}
        else:
            record[reporter].add(reported)
    
    count = {}
    for reporteds in record.values():
        if reporteds != 0: 
            for r in reporteds:
                if r not in count:
                    count[r] = 1
                else:
                    count[r] += 1
    
    l = [0] * len(id_list)
    for reported, count in count.items():
        if count >= k:
            for reporter, value in record.items():
                if reported in value:
                    l[id_list.index(reporter)] += 1

    return l