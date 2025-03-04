# Flood Fill Algorithm:733  LC : [https://leetcode.com/problems/flood-fill/description/]

#Intuition: 
# How to solve this problem using a graph?
# Think of all the pixels in the image as nodes or vertices which are connected through each other via 4 edges.

# Given the starting pixel, any traversal algorithm can be used to find all the neighbors having similar pixel value. During the traversal, each pixel value can be changed to the new color value to get the flood filled image.

# How to traverse the neighbours efficiently?
# The 4 neighbours of the current cell can be shown like this:


# For efficient traversal of all neighboring pixels, the delRow and delCol arrays can be used where:

# delRow = {-1, 0, 1, 0}
# delCol = {0, 1, 0, -1}

# Approach:
# Initialise a new image to store the image after flood fill. (The given image can be used for the same but it is considered a good practice if the given input is not altered.)
# To navigate to the neighboring pixels, direction vectors are defined for moving up, right, down, and left. A helper function checks if a pixel is within the bounds of the image. This ensures that the traversal does not go out of the image boundary.
# Starting from the given pixel, a recursive DFS traversal is performed during which all the pixels having same initial color are marked with new color in the new image.
# Once the traversal terminates, the new image stores the flood filled image.


#code:

class Solution:
    def dfs(self, sr, sc, n, m, newImage, newColor, initialColor):
        newImage[sr][sc] = newColor
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        for i in range(0, 4):
            row = delRow[i] + sr
            col = delCol[i] + sc
            if row>=0 and row<n and col>=0 and col<m and newImage[row][col] == initialColor and newImage[row][col] != newColor:
                self.dfs(row, col, n, m, newImage, newColor, initialColor)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        newImage = image
        initialColor = image[sr][sc]
        self.dfs(sr, sc, n ,m, newImage, color, initialColor)
        return newImage


# Complexity Analysis:
# Time Complexity: O(N*M) (where N and M are the dimensions of image)

# In the worst case, all the pixel will have same color, DFS call will be made for (N*M) nodes.
# For every pixel, its four neighbors are traversed, taking O(4*N*M) time.
# Space Complexity: O(N*M)

# Extra space for new image takes O(N*M) space.
# Recusive stack space for DFS calls will take at most O(N*M) space.
