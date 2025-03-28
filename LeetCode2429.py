#LeetCode 2429: Minimize XOR
#Given two positive integers num1 and num2, find the positive integer x such that:

#    x has the same number of set bits as num2, and
#    The value x XOR num1 is minimal.

#Note that XOR is the bitwise XOR operation.

#Return the integer x. The test cases are generated such that x is uniquely determined.

#The number of set bits of an integer is the number of 1's in its binary representation.

 

#Example 1:

#Input: num1 = 3, num2 = 5
#Output: 3
#Explanation:
#The binary representations of num1 and num2 are 0011 and 0101, respectively.
#The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

#Example 2:
#Input: num1 = 1, num2 = 12
#Output: 3
#Explanation:
#The binary representations of num1 and num2 are 0001 and 1100, respectively.
#The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

#Constraints:

#    1 <= num1, num2 <= 109

#Solution:

from typing import List

class Solution:
    def count_bits(self, num: int) -> int:
        # Count number of 1s in the binary representation of num
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count set bits in num2
        target_bits = self.count_bits(num2)
        
        # If num1 and num2 have the same number of set bits, return num1
        if self.count_bits(num1) == target_bits:
            return num1
        
        result = 0
        
        # Strategy: Try to match the most significant bits of num1 first
        # This minimizes the XOR value
        
        # Convert num1 to binary and analyze from most significant bit to least
        binary_num1 = bin(num1)[2:]
        remaining_bits = target_bits
        
        # First pass: set bits where num1 has 1s, starting from MSB
        for i, bit in enumerate(binary_num1):
            if bit == '1' and remaining_bits > 0:
                # Set this bit in the result
                position = len(binary_num1) - i - 1
                result |= (1 << position)
                remaining_bits -= 1
        
        # Second pass: if we need more 1s, add them in least significant positions
        bit_position = 0
        while remaining_bits > 0:
            # Check if this position is not set in result or num1
            if (result & (1 << bit_position)) == 0 and (num1 & (1 << bit_position)) == 0:
                result |= (1 << bit_position)
                remaining_bits -= 1
            bit_position += 1
            
        return result

# Example usage - Example 1 from the problem statement
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    num1 = 3
    num2 = 5
    result = solution.minimizeXor(num1, num2)
    print(f"Example 1:")
    print(f"Input: num1 = {num1}, num2 = {num2}")
    print(f"Output: {result}")
    print(f"Binary num1: {bin(num1)[2:].zfill(4)}, Binary num2: {bin(num2)[2:].zfill(4)}, Binary result: {bin(result)[2:].zfill(4)}")
    print(f"Expected: 3")
    print(f"XOR value: {result ^ num1}")
    print(f"Explanation: The binary representations of num1 and num2 are 0011 and 0101, respectively.")
    print(f"The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.")
    print()
    
    # Example 2
    num1 = 1
    num2 = 12
    result = solution.minimizeXor(num1, num2)
    print(f"Example 2:")
    print(f"Input: num1 = {num1}, num2 = {num2}")
    print(f"Output: {result}")
    print(f"Binary num1: {bin(num1)[2:].zfill(4)}, Binary num2: {bin(num2)[2:].zfill(4)}, Binary result: {bin(result)[2:].zfill(4)}")
    print(f"Expected: 3")
    print(f"XOR value: {result ^ num1}")
    print(f"Explanation: The binary representations of num1 and num2 are 0001 and 1100, respectively.")
    print(f"The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.")