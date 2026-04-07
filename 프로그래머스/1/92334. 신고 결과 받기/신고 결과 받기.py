def solution(id_list, report, k):
    answer = {id: 0 for id in id_list }
    report_dict = { id: [] for id in id_list }
    report_cnt = { id: 0 for id in id_list }
    
    for re in report:
        reporter, reportee = re.split()
        if reportee not in report_dict[reporter]:
            report_dict[reporter].append(reportee)
            report_cnt[reportee] += 1
    
    for id, cnt in report_cnt.items():
        if cnt >= k:
            for er, ee in report_dict.items():
                if id in ee: answer[er] += 1
    
    return list(answer.values())