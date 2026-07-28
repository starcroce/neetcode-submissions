class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = {}
        for t in tasks:
            task_cnt[t] = task_cnt.get(t, 0) + 1
        
        max_task, max_cnt = None, 0
        for t in task_cnt:
            if task_cnt[t] > max_cnt:
                max_task, max_cnt = t, task_cnt[t]

        total_idle = (max_cnt - 1) * n
        for t in task_cnt:
            if t != max_task:
                total_idle -= min(max_cnt - 1, task_cnt[t])
        
        res = len(tasks) + max(0, total_idle)
        return res
        