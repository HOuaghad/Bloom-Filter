# Bloom-Filter

This implementation that was inspired by tarunsharma1/Bloom-Filter.
This implementation makes his implemention into a class and makes use of files.

You can save your bloom filter to a file and load it later.

I had to implement this for python3 since the other libraries did not support files for python3.

Also added automatic size calculation and hash calculation. 

# Usage
```python
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']

	filepath = './files/words.bloom'
	
	bloomfilter = BloomFilter(len(items), 0.001, filepath) #0.001 allowed error rate
	
	bloomfilter.add(items)

	'glass' in bloomfilter
	True

	'Jackson' in bloomfilter
	False

```

# Usage with files
If you have an already stored file, just load it and work with it. However you can not copy it nor add to it (will implement this when free)
```python
	items = ['glass', 'moon', 'mouse', 'cat', 'extra', 'pot']

	filepath = './files/words.bloom' # the old file from the pervious example
	
	bloomfilter = BloomFilter(len(items), 0.001, filepath) #0.001 allowed error rate

	'glass' in bloomfilter
	True

	'Jackson' in bloomfilter
	False

```

##Hash Function 
For hashing, murmurhash3 in python was used. MurmurHash is a non-cryptographic hashing function which generates a 128bit hash value. Using an engineered hash function like Murmur will maximize the quality of the distribution, and minimize the number of collisions. A different seed value (value which specifies how many times the hash function should randomize and mix the data)
can be used. In the code given, the number hashcount is the number of hash functions are used by changing the seed value from 0 - hashcount. A bit array's size is calculcated in correspondance to the number of items provided and the allowed error rate.