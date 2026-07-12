class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = [(p, s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        fleets, cur_max = 0, 0 
        for p, s in pair:
            time_to_target = (target - p) / s
            if time_to_target <= cur_max:
                continue
            else:
                fleets += 1
                cur_max = time_to_target
        return fleets
