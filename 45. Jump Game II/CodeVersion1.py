def jump(nums):
    MinJumps = []
    jumps = 0

    def CheckPos(pos, MinJumps, jumps):
        if pos == len(nums) - 1:
            MinJumps.append(jumps)

        lastStep = min(pos + nums[pos], len(nums) - 1)
        for NextStep in range(pos + 1, lastStep + 1):
            CheckPos(NextStep, MinJumps, jumps + 1)

    CheckPos(0, MinJumps, jumps)
    return min(MinJumps)
