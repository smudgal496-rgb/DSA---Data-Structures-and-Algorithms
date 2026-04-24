#Count Frequency of Elements
def count_frequency(arr):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print("Frequency of Elements:")
    print (frequency)

count_frequency([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])