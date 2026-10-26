class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position,speed),reverse=True)

        cars=[]
        for position,speed in fleet:
            time = (target-position)/speed

            if cars and time<=cars[-1]:
                continue
            else:
                cars.append(time)
        return len(cars)