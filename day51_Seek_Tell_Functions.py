# Open an existing file "day50_myfile.txt" in read mode
f = open("day50_myfile.txt", "r")

# Move the file pointer to the 10th byte in the file (0-based index)
f.seek(10)

# Print the current position of the file pointer
print("Current pointer position:", f.tell())  # Output: 10

# Read the next 6 characters (bytes) from the file starting from byte 10
print("Reading 6 characters from current position:", f.read(6))

# Print the position of the pointer after reading 6 characters
print("Pointer position after reading:", f.tell())

# Close the first file
f.close()


# Open a new file "myfile2.txt" in write mode
f = open("myfile2.txt", "w")

# Write "Hello World" to the file (11 characters including space)
f.write("Hello World")

# Truncate the file to only keep the first 5 bytes
f.truncate(5)  # Now file contains only "Hello"

# Close the file after truncating
f.close()


# Open the truncated file again to read its contents
f = open("myfile2.txt", "r")
print("Contents of truncated file:", f.read())  # Output: "Hello"
f.close()


# seek(offset)
# Moves the file pointer to a specific position.

# f.seek(10) moves the pointer to the 10th byte in the file.

# Useful for skipping parts of the file or jumping to a specific section before reading/writing.

# 🔹 tell()
# Returns the current position of the file pointer (as a byte offset from the beginning).

# Example: If f.tell() returns 10, it means you are at the 10th byte in the file.

# 🔹 read(n)
# Reads the next n characters (or bytes in binary mode) from the current pointer position.

# After reading, the pointer automatically moves forward by n bytes.

# 🔹 truncate(size)
# Cuts the file content down to the first size bytes.

# Example: truncate(5) keeps only the first 5 bytes of the file and deletes the rest.

# If you don’t pass a size, it truncates at the current pointer position (f.truncate()).
