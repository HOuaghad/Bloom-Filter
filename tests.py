from src.bloom_filter import BloomFilter

def print_success(message):
	print("\033[1m\033[0;32m %s \033[0m"  % message)

def print_failure(message):
	print("\033[1m\033[0;31m%s \033[0m"  % message)

def testFileCreation():
	path = './files/bands.bloom'
	try:
		BloomFilter(10, 0.00000001, path)
	except Exception as e:
		print_failure("Test failed with: %s" % str(e))
		raise e
	else:
		import os
		if os.path.exists(path):
			print_success("File created successfully")
		else:
			print_failure("Failed to crate file")

def testBloomFilter():
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']

	filepath = './files/words.bloom'
	
	bloomfilter = BloomFilter(len(items), 0.001, filepath)
	
	bloomfilter.add(items)

	nitems = ['Jackson', 'Ford', 'stuff']

	ci = 0
	for i in items:
		if i in bloomfilter:
			print_success("%s in bloomfilter" % i)
		else:
			ci += 1
			print_failure("%s not in bloomfilter" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented missed\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements of bloomfilter are found\n\n")



	ci = 0
	for i in nitems:
		if i in bloomfilter:
			ci += 1
			print_success("Found in bloomfilter: %s" % i)
		else:
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented found\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements that are not in the bloomfilter weren't found\n\n")

	# print(bloomfilter.bit_array)
	# bloomfilter = BloomFilter(len(items), 0.001, filepath)
	# print("Post reinit")
	# print(bloomfilter.bit_array)


def testOldBloomFilterFile():
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']
	nitems = ['Jackson', 'Ford', 'stuff']

	bloomfilter = BloomFilter(len(items), 0.001, './files/words.bloom')

	ci = 0
	for i in items:
		if i in bloomfilter:
			print_success("Found in bloomfilter: %s" % i)
		else:
			ci += 1
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented missed\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements of bloomfilter are found\n\n")



	ci = 0
	for i in nitems:
		if i in bloomfilter:
			ci += 1
			print_success("Found in bloomfilter: %s" % i)
		else:
			print_failure("Did not find in bloomfilter: %s" % i)

	if ci != 0 :
		print_failure("\nFirst part of test failed with %d elemented found\n\n" % ci)
	else:
		print_success("\nTest passed!, all elements that are not in the bloomfilter weren't found\n\n")

	# print(bloomfilter.bit_array)

if __name__ == "__main__":

	print("\033[1mTest file creation:\n\n \033[0m")
	testFileCreation()

	print("\n\n\033[1mTest Bloom Filter:\n\n \033[0m")
	testBloomFilter()

	print("\n\n\033[1mTest old bloom filter file:\n\n \033[0m")
	testOldBloomFilterFile()
