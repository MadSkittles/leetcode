class Solution:
    def carFleet(self, target, position, speed):
        l = sorted(zip(position, speed), reverse=True)
        fleet, time = len(l), float("-inf")
        for position, speed in l:
            car_time = (target - position) / speed
            if car_time <= time:
                fleet -= 1
            else:
                time = car_time
        return fleet


if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(12, [3], [3]))
