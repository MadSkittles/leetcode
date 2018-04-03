class Solution:
    def exclusiveTime(self, n, logs):
        status_map, spent_time, stack, cur_scope, pre_status, pre_timetamp = {'start': 1, 'end': 0}, {}, [], None, None, 0
        for log in logs:
            id, status, timestamp = log.split(':')
            id, timestamp = int(id), int(timestamp)
            if cur_scope is not None:
                diff = status_map[pre_status] - status_map[status]
                spent_time[cur_scope] = spent_time.get(cur_scope, 0) + timestamp - pre_timetamp + diff
            if status == 'start':
                stack.append(cur_scope)
                cur_scope = id
            else:
                cur_scope = stack.pop()
            pre_timetamp, pre_status = timestamp, status
        return [spent_time.get(id, 0) for id in range(n)]