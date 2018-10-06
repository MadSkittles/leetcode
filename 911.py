import heapq
from bisect import bisect_right
from collections import Counter


class TopVotedCandidate:
    def __init__(self, persons, times):
        cnt, q = Counter(), []
        self.time, self.leader = [], []
        for i, p in enumerate(persons):
            self.time.append(times[i])
            cnt[p] += 1
            heapq.heappush(q, (-cnt[p], -i, p))
            self.leader.append(q[0][-1])

    def q(self, t):
        pos = bisect_right(self.time, t)
        return self.leader[pos - 1]


if __name__ == "__main__":
    topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(topVotedCandidate.q(3))
    print(topVotedCandidate.q(12))
    print(topVotedCandidate.q(25))
    print(topVotedCandidate.q(15))
    print(topVotedCandidate.q(24))
    print(topVotedCandidate.q(8))
