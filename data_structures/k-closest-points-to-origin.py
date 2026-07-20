class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store each point along with its squared distance from the origin
        minHeap = []

        # Calculate the squared distance for every point
        for i in range(len(points)):
            # Squared Euclidean distance (no need for sqrt since we're only comparing distances)
            dist = (points[i][0] ** 2) + (points[i][1] ** 2)

            # Store distance followed by the point's coordinates
            minHeap.append([dist, points[i][0], points[i][1]])

        # Convert the list into a min-heap based on the distance value
        heapq.heapify(minHeap)

        # List to store the k closest points
        res = []

        # Extract the closest point k times
        while k > 0:
            # Remove and return the point with the smallest distance
            dist, x, y = heapq.heappop(minHeap)

            # Add the coordinates to the result
            res.append([x, y])

            # Decrease the remaining number of points to retrieve
            k -= 1

        # Return the k closest points
        return res
