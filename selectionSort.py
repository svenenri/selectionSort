import random, datetime

# A function that generates a random 100 integers between 0 and 10,000
def randomList(emptyList):

	count = 100
	for i in range(count):
		emptyList.append(random.randint(0, 10000))

	return emptyList

# Selection sort function that returns a sorted list 
def selSort(list):
	count = -1

	for i in range (len(list)- 1):
		count += 1
		minNum = list[count]
		carry = list[count]
		flag = 0
		for j in range(count, len(list)):
			if (list[j] < minNum):
				flag = j
				minNum = list[j]
		# Control for when multiple indicies have the same value
		if i != 0 and flag == 0:
			continue
		else:
			list[count] = minNum
			list[flag] = carry

	return list


# Used to calculate program runtime
start = datetime.datetime.now()

# Create list that will hold a random 100 integers
newList = []

# Grab list of random integers
randomList(newList)

# Sort list of random integers with select sort
print selSort(newList)

# Calculate and printe protram runtime
print "Time to complete:", datetime.datetime.now() - start
