'''
Python’s bytearray is a mutable sequence of bytes that allows you to manipulate binary data efficiently.
You can create a bytearray using the bytearray() constructor with various arguments.

'''
# To specify an empty array of bytes, you can leverage one of these equivalent techniques:
bytearray()     # >> bytearray(b'')
bytearray(0)    # >> bytearray(b'')
bytearray([])   # >> bytearray(b'')
bytearray(b"")  # >> bytearray(b'')

''' When you call bytearray() with a positive integer as an argument, you create a zero-filled byte array of 
   the specified size, initialized with null bytes (b"\x00"). '''

bytearray(5)        # >> bytearray(b'\x00\x00\x00\x00\x00')
list(bytearray(5))  # >> [0, 0, 0, 0, 0]


# You can also pass an iterable of small integers into bytearray() to treat them as standalone byte values.
bytearray(range(65, 91))                                          # >> bytearray(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
bytearray([82, 101, 97, 108, 32, 80, 121, 116, 104, 111, 110])    # >> bytearray(b'Real Python')

'''   The last single-argument invocation of bytearray() involves passing a bytes-like object or an object implementing 
the so-called buffer protocol as a parameter. It could be another bytearray or bytes object, for example: '''

binary_data = b"This is a bytes literal"  
bytearray(binary_data)                    # >> bytearray(b'This is a bytes literal')


"""
Public Methods

The bytearray type includes all the methods of bytes but, being mutable, also provides eight additional methods designed for in-place modifications:
   Method 	   Description
   .append() 	 Append a single item to the end of the bytearray.
   .copy() 	    Return a copy of the bytearray.
   .remove() 	 Remove the first occurrence of a value in the bytearray.
   .reverse() 	 Reverse the order of the values in the bytearray in place.
   .pop() 	    Remove and return a single item from the bytearray at the given index.
   .insert() 	 Insert a single item into the bytearray before the given index.
   .extend() 	 Append all the items from the iterator or sequence to the end of the bytearray.
   .clear() 	 Remove all items from the bytearray.

"""
