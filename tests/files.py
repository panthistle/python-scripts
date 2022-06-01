
# ------------------------------------------------------------------------------
#
# -------------------------- file objects --------------------------------------

#f = open("files_test.txt", "r")		# read only
#f = open("files_test.txt", "w")		# write only
#f = open("files_test.txt", "a")		# append
#f = open("files_test.txt", "r+")	    	# read and write
#print(f.name)
#print(f.mode)
#f.close()


# ------------------------------------------------------------------------------
#
# ------------------------- reading files --------------------------------------

with open("files_test_read.txt", "r") as f:

    # use read() for small files
    f_out = f.read()
    print(f_out)

    # set the cursor at specific position 
    f.seek(0)

    # use readlines() for bigger files - returns a list of lines
    f_out = f.readlines()
    print(f_out)

    # use readline() for single line - includes extra newline feed (\n)
    f.seek(0)
    f_out = f.readline()
    print(f_out)
    f_out = f.readline()
    print(f_out)

    # use readline() for single line - without extra newline feed (\n)
    f.seek(0)
    f_out = f.readline()
    print(f_out, end='')
    f_out = f.readline()
    print(f_out, end='')

    # iterate through lines
    f.seek(0)
    for line in f:
        print(line, end='')
    print()

    # read specific number of characters
    f.seek(0)
    f_out = f.read(10)
    print(f_out, end='')
    f_out = f.read(30)
    print(f_out)

    # iterate through small chunks
    f.seek(0)
    size_to_read = 100
    f_out = f.read(size_to_read)
    while len(f_out) > 0:
        print(f_out)
        f_out = f.read(size_to_read)

    # get current cursor position
    print(f.tell())

# after 'with open' block
print(f.mode)
print(f.closed)
# print(f.read())	# throws error


# ------------------------------------------------------------------------------
#
# ------------------------- writing files --------------------------------------

with open("files_test_write.txt", "w") as f:

	f.write("Test")
	f.seek(0)
	f.write("R")


# ------------------------------------------------------------------------------
#
# ------------------------- copying files --------------------------------------

# # TEXT FILES
# with open("files_test_write.txt", "r") as rf:
# 	with open("files_test_write_copy.txt", "w") as wf:
# 		for line in rf:
# 			wf.write(line)


# # IMAGE FILES (binary data) - without chunks
# with open("files_test_image.jpg", "rb") as rf:
# 	with open("files_test_image_copy.jpg", "wb") as wf:
# 		for line in rf:
# 			wf.write(line)

# # IMAGE FILES (binary data) - with chunks
# chunk_size = 4096
# with open("files_test_image.jpg", "rb") as rf:
#     with open("files_test_image_copy.jpg", "wb") as wf:
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)

