"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
"""

matches_cases = [
    [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]],
    [[2,3],[1,3],[5,4],[6,4]]
]
ans = [
    [[1,2,10],[4,5,7,8]],
    [[1,2,5,6],[]]
]

def sol(matches: list) -> list:
    count_lost = {}
    lost_0 = []
    lost_1 = []
    for match in matches:
        assert type(match) == list
        if match[0] not in count_lost:
            count_lost[match[0]] = 0
        if match[1] not in count_lost:
            count_lost[match[1]] = 0
        count_lost[match[1]] += 1
    for k, v in count_lost.items():
        if v == 0:
            lost_0.append(k)
        if v == 1:
            lost_1.append(k)
    print([sorted(lost_0), sorted(lost_1)])
    return [sorted(lost_0), sorted(lost_1)]
    

for i in range(len(matches_cases)):
    assert sol(matches_cases[i]) == ans[i]