def search_video(arr, target):
    low = 0 #low pointer starts at first index 0

    high = len(arr) - 1 # starting our high pointer at the last index of the list
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
    
    # If we reach here, the target is not in the list
    return -1




# Video List sort ussing bubble sort
def sort_titles(video_list):

    x = len(video_list)

    for i in range(x):
        swapped = False

        for j in range(0, x-i-1):
        
            if video_list[j] > video_list[j+1]: 
                video_list[j], video_list[j+1] = video_list[j+1], video_list[j]
                swapped = True

        if not swapped:
            break
        
    return video_list

video_list = [
    "The Art of Coding", 
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]


sort_titles(video_list)

print("\n".join(video_list))