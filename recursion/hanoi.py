# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# https://www.youtube.com/watch?v=GaC1Dzpafhk
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    pass
    if n == 1:

        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return

    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


print(TowerOfHanoi(4, 'A', 'C', 'B'))

# 15.1
# time: O(2^n)
# Print single move takes O(1)
NUM_PEGS = 3


def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(
                num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(
                num_rings_to_move - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings+1)))]+[[]
                                                    for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


print(compute_tower_hanoi(4))
