# Mock function to simulate the API for checking bad versions
def isBadVersion(version):
    # Replace this logic with the actual bad version logic
    # For example, let's say versions 4 and above are bad:
    return version >= 4

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n  # Starting from 1 because versions are 1-indexed
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                else:
                    end = mid - 1  # Move left
            else:
                start = mid + 1  # Move right
        return -1  # If no bad version is found

# Example usage:
solution = Solution()
n = 5  # Assume we have 5 versions
first_bad = solution.firstBadVersion(n)
print(f"The first bad version is: {first_bad}")