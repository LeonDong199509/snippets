class Solution:
    def singleNumber(self, nums: List[int]) -> int:

    # ✅ Bitwise Operators in Python

    # Operator	Name	Example	Description
    # &	AND	a & b	1 if both bits are 1
    # `	`	OR	`a
    # ^	XOR (exclusive or)	a ^ b	1 if bits are different
    # ~	NOT (invert)	~a	Flips all bits (two’s complement)
    # <<	Left Shift	a << n	Shifts bits left by n (multiply by 2ⁿ)
    # >>	Right Shift	a >> n	Shifts bits right by n (floor divide by 2ⁿ)


    # 🔢 Examples

    # a = 5        # 0b0101
    # b = 3        # 0b0011

    # print(a & b)   # 1  -> 0b0001
    # print(a | b)   # 7  -> 0b0111
    # print(a ^ b)   # 6  -> 0b0110
    # print(~a)      # -6 (in two's complement, ~5 = -6)

    # print(a << 1)  # 10 -> 0b1010 (shift left = *2)
    # print(a >> 1)  # 2  -> 0b0010 (shift right = //2)

        result = 0
        for num in nums:
            result ^= num
        return result

        # nums = [4, 1, 2, 1, 2]
        # Step-by-step:
        # 0 ^ 4 = 4
        # 4 ^ 1 = 5
        # 5 ^ 2 = 7
        # 7 ^ 1 = 6
        # 6 ^ 2 = 4 → ✅ answer: 4

        
