def is_universal(s):
    """Check if string s is universal (lexicographically smaller than its reversal)"""
    reversed_s = s[::-1]
    return s < reversed_s

def can_make_universal(s, k):
    n = len(s)
    
    # If s is already universal, no swaps needed
    if is_universal(s):
        return "YES"
    
    # If k = 0, we can't do any swaps
    if k == 0:
        return "NO"

    # Special case for single character strings (like "a")
    if n == 1:
        return "NO"  # Always equal to its reversal

    # Check for palindrome with all identical characters (like "zzz")
    if s == s[::-1] and len(set(s)) == 1:
        return "NO"  # No swap will change anything

    # For normal palindromes (like "codeforcesecrofedoc"), we can break symmetry with 1 swap
    if s == s[::-1] and len(set(s)) > 1:
        # Find two different characters to swap
        for i in range(n):
            for j in range(i+1, n):
                if s[i] != s[j]:
                    # Simulate the swap
                    s_list = list(s)
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    swapped_s = ''.join(s_list)
                    
                    if is_universal(swapped_s):
                        return "YES"
    
    # For non-palindromes, often one swap is enough to make them universal
    # Try all possible swaps
    for i in range(n):
        for j in range(i+1, n):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            swapped_s = ''.join(s_list)
            
            if is_universal(swapped_s):
                return "YES"
    
    return "NO"

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        results.append(can_make_universal(s, k))
    
    for result in results:
        print(result)

solve()