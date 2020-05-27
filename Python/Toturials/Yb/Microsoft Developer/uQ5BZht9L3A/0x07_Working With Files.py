## Writing ti a file
stream = open('demo.txt', 'wt') # Write text
stream.write('H') # write a single string
stream.writelines(['ello', ' ', 'world'])
stream.write('\n')

stream.close() # Close the stream (and flush data)

## Managing the stream
stream = open('demo.txt', 'wt')
stream.write('demo!')
stream.seek(0) # Put the cursor back to the start
stream.write('cool')
stream.flush() # Write the data to file
stream.close() # Flush and close the stream

## Reading from a file
stream = open('demo.txt')

print(stream.readable()) # Can we read?
print(stream.read(1)) # Read the first character
print(stream.readline()) # Read a line
stream.close()
