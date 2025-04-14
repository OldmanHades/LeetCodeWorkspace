class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int, debug=True, verbose=False) -> int:
        if debug:
            print(f"Input array: {arr}")
            print(f"Constraints: a={a}, b={b}, c={c}")
        
        count = 0
        n = len(arr)
        good_triplets = []  # To store the good triplets for debugging
        total_checked = 0   # Count total triplets checked
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total_checked += 1
                    # Get current triplet values and indices
                    value_triplet = (arr[i], arr[j], arr[k])
                    index_triplet = (i, j, k)
                    
                    # Check each condition separately
                    condition1 = abs(arr[i] - arr[j]) <= a
                    condition2 = abs(arr[j] - arr[k]) <= b
                    condition3 = abs(arr[i] - arr[k]) <= c
                    
                    if debug and verbose:
                        print(f"\nChecking triplet #{total_checked}:")
                        print(f"  Values: {value_triplet} at indices {index_triplet}")
                        print(f"  Condition 1: |{arr[i]} - {arr[j]}| = {abs(arr[i] - arr[j])} <= {a} : {condition1}")
                        print(f"  Condition 2: |{arr[j]} - {arr[k]}| = {abs(arr[j] - arr[k])} <= {b} : {condition2}")
                        print(f"  Condition 3: |{arr[i]} - {arr[k]}| = {abs(arr[i] - arr[k])} <= {c} : {condition3}")
                    
                    # If all conditions are met, it's a good triplet
                    if condition1 and condition2 and condition3:
                        count += 1
                        good_triplets.append((value_triplet, index_triplet))
                        if debug and verbose:
                            print(f"  ✅ Found good triplet!")
                    elif debug and verbose:
                        print(f"  ❌ Not a good triplet")
        
        if debug:
            print(f"\nSummary:")
            print(f"  Total triplets checked: {total_checked}")
            print(f"  Total good triplets found: {count}")
            if good_triplets:
                print(f"  Good triplets (values, indices):")
                for t, idx in good_triplets:
                    print(f"    {t} at indices {idx}")
            else:
                print(f"  No good triplets found.")
            
            # Verify using example cases
            if arr == [3,0,1,1,9,7] and a == 7 and b == 2 and c == 3:
                expected = 4
                if count == expected:
                    print(f"\nTest case 1 passed ✅: Expected {expected}, got {count}")
                else:
                    print(f"\nTest case 1 failed ❌: Expected {expected}, got {count}")
            
            if arr == [1,1,2,2,3] and a == 0 and b == 0 and c == 1:
                expected = 0
                if count == expected:
                    print(f"\nTest case 2 passed ✅: Expected {expected}, got {count}")
                else:
                    print(f"\nTest case 2 failed ❌: Expected {expected}, got {count}")
        
        return count

# Main function to run examples
def main():
    solution = Solution()
    
    print("Example 1:")
    solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)
    
    print("\n" + "="*50 + "\n")
    
    print("Example 2:")
    solution.countGoodTriplets([1,1,2,2,3], 0, 0, 1)
    
    # For detailed step-by-step debugging, uncomment and run:
    # print("\n" + "="*50 + "\n")
    # print("Detailed Example 1:")
    # solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3, debug=True, verbose=True)

if __name__ == "__main__":
    main()
