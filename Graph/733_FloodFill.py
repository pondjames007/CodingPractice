# TIPS:
# put a stack to go through the image
# remember to put a visit list to store the visited pixel so that it won't go to infinite loop 
# if the newColor is the same as the source color

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return []
        
        color = image[sr][sc]
        stack = [(sr, sc)]
        visited = []
        while stack:
            r,c = stack.pop()
            image[r][c] = newColor
            visited.append((r,c))
            if r > 0 and image[r-1][c] == color and (r-1,c) not in visited: stack.append((r-1, c))
            if r < len(image)-1 and image[r+1][c] == color and (r+1,c) not in visited: stack.append((r+1, c))
            if c > 0 and image[r][c-1] == color and (r,c-1) not in visited: stack.append((r, c-1))
            if c < len(image[r])-1 and image[r][c+1] == color and (r,c+1) not in visited: stack.append((r, c+1))
        
        return image
                