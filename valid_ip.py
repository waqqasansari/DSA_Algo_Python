def restoreIpAddresses(s):
    result = []
    n = len(s)
    
    # We need at least 4 digits and at most 12 digits to form a valid IP address
    if n < 4 or n > 12:
        return result
    
    # Try placing three dots in different positions
    for i in range(1, min(4, n - 2)):
        for j in range(i + 1, min(i + 4, n - 1)):
            for k in range(j + 1, min(j + 4, n)):
                A = s[:i]
                B = s[i:j]
                C = s[j:k]
                D = s[k:]
                print(f"{A}.{B}.{C}.{D}")
                # Validate each segment
                if isValid(A) and isValid(B) and isValid(C) and isValid(D):
                    
                    result.append(f"{A}.{B}.{C}.{D}")
    
    return result

def isValid(segment):
    # Check if the segment is valid:
    # 1. Length between 1 and 3
    # 2. No leading zeros unless the segment is '0'
    # 3. Integer value is between 0 and 255
    return len(segment) <= 3 and (segment == "0" or segment[0] != '0') and 0 <= int(segment) <= 255

# Example 1
input1 = "25525511135"
print(restoreIpAddresses(input1))  # Output: ["255.255.11.135", "255.255.111.35"]

# Example 2
input2 = "25505011535"
print(restoreIpAddresses(input2))  # Output: []

# Example 3
input3 = "1111"
print(restoreIpAddresses(input3))  # Output: ["1.1.1.1"]

# Example 4
input4 = "010010"
print(restoreIpAddresses(input4))  # Output: ["0.10.0.10", "0.100.1.0"]
