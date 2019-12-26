# Apache Arrow is an in-memory data structure mainly for use by engineers for building data systems
#   it facilitates communication between many components: ex. read file -> Python pandas -> Spark data frame
#   it provides fast data interchange between systems without the serialization costs of systems like Thrift and Protocol Buffers
# Installation
#   pip3 install pyarrow
import pyarrow as pa

# py_buffer([data]):
#   creating a Buffer in this way does not allocate any memory
#   it is a zero-copy view on the memory exported from the data bytes object
#   this permits Buffers to cheaply reference other Buffers
#   it is similar to Python's built-in buffer protocol and memoryview objects (i.e. a data pointer and length)
data = b'abcdefghijklmnopqrstuvwxyz'
buf = pa.py_buffer(data)
print(buf)      # <pyarrow.lib.Buffer object at 0x10633af10>
print(buf.size) # 26

# [buf].to_pybytes():
#   this converts the Buffer's data to a Python bytestring (thus making a copy of the data)
print(buf.to_pybytes()) # b'abcdefghijklmnopqrstuvwxyz' (the data is copied when coverted to a bytestring)

# memoryview([obj]):
#   this creates a memoryview that references obj (obj must support the buffer protocol, ex. built-in objects such as bytes and bytearray)
#   a memoryview object allow Python code to access the internal data of an object that supports the buffer protocol without copying
#     ex. unlike bytes or str objects, the underlying data are copied when sliced
v = memoryview(buf)
print(v) # <memory at 0x11dec6648>
print(v[0:2].tobytes()) # b'ab': no copying to the underlying data

# Memory Pools
# allocate_buffer([size], [resizable]):
#   this allocates a resizable Buffer from the default memory pool (just like malloc and free in C)
buf = pa.allocate_buffer(1024, resizable=True)
print(pa.total_allocated_bytes()) # 1024
buf.resize(2048)
print(pa.total_allocated_bytes()) # 2048 
buf = None # the buffer will be garbaged-collected, and all of the memory is freed
print(pa.total_allocated_bytes()) # 0

# High-Level API for instantiating streams
# 1) Input Streams: input_stream([buf]):
#   this allows creating a readable NativeFile from various kinds of sources
# a) if passed a Buffer or a memoryview object:
data = b'some data'
buf = pa.py_buffer(data) # a Buffer: this does not allocate any memory
#buf = memoryview(b"some data") # a memoryview object
stream = pa.input_stream(buf)
print(stream.read(4)) # b'some'
# b) if passed a string or file path, it will open the given file on disk for reading, creating a OSFile
import gzip
with gzip.open('example.gz', 'wb') as fout:
    fout.write(b'some data\n' * 3)
stream = pa.input_stream('example.gz')
print(stream.read()) # b'some data\nsome data\nsome data\n'

# 2) Output Streams: output_stream([]):
#   this is the equivalent function for output streams and allows creating a writable NativeFile
#   just like input_stream(), it is able to write to buffers or do on-the-fly compression
with pa.output_stream('example1.dat') as stream:
    stream.write(b'some data')
fin = open('example1.dat', 'rb')
print(fin.read()) # b'some data'
fin.close()

# What is Memory-mapping?
#   it is a way for a process to access the file
#   a process can map a file's contents (or its subset) into its address space
#   this makes it easier to read from and write to the file, by reading and writing in memory
#   the file itself, on disk, is just the same as any other file

# 3) On-Disk and Memory Mapped Files: OSFile([filepath], wb):
#      this allows to interact with data on disk
# a) using standard operating system-level file APIs:
with open('example2.dat', 'wb') as fout:
    fout.write(b'some example data')
# b) using sing pyarrow's OSFile class:
with pa.OSFile('example3.dat', 'wb') as fout:
    fout.write(b'some example data')
# For reading files, you can use OSFile or MemoryMappedFile:
#   for OSFile, it allocates new memory on each read, like Python file objects
#   for memory maps, the library constructs a buffer referencing the mapped memory without any memory allocation or copying
# a) OSFile([filepath]):
file_obj = pa.OSFile('example2.dat')
print(file_obj.read(4)) # b'some': this allocates new memory when read
# note:
#   using OSFile for read() & write() is more efficient than using standard operating system-level file APIs

# b) memory_map([filepath]): this opens the memory map at file path
mmap = pa.memory_map('example3.dat')
print(mmap.read(4))        # b'some': this DOES NOT allocate new memory, as it references the maaped memory when read

# read() vs. read_buffer()
# read(): this implements the standard Python file read API
# read_buffer(): this reads into an Arrow Buffer object
print(mmap.seek(0)) # 0
buf = mmap.read_buffer(4) # <pyarrow.lib.Buffer object at 0x10cfc3960>: this does not allocate any memory
print(buf.to_pybytes()) # b'some': this allocates new memory

# 4) In-Memory Reading and Writing
#   for serialization and deserialization of in-memory data (arrow is more efficient than pickle)
writer = pa.BufferOutputStream() # for in-memory writing
print(writer.write(b'hello, friends')) # 14
buf = writer.getvalue()
print(buf) # <pyarrow.lib.Buffer object at 0x10b6bdea0>
print(buf.size) # 14
reader = pa.BufferReader(buf) # for in-memory reading
print(reader.seek(7)) # 7
print(reader.read(7)) # b'friends'

# 5) arrow + numpy
import numpy as np
data = np.random.random((3, 2))
print(data)
# [[0.3346962  0.25842736]
#  [0.37600096 0.71404968]
#  [0.1538029  0.63056035]]
data = data.reshape(-1)
print(data)
# [0.3346962  0.25842736 0.37600096 0.71404968 0.1538029  0.63056035]
pa_array = pa.array(data) # <pyarrow.lib.DoubleArray object at 0x7f467b68aea8>
print(pa_array)
# [
#   0.863989,
#   0.964546,
#   0.711622,
#   0.282656,
#   0.383822,
#   0.0271719
# ]
np_array = pa_array.to_numpy()
print(np_array)
# [0.86004504 0.53987214 0.56330477 0.72354143 0.25070862 0.00563462]

# 6) arrow + pandas
#    drawbacks of Pandas are overcome by Arrow:
#    a) no support for memory-mapped data items
#       in Pandas, data must be loaded entirely into RAM to be processed
#    b) poor performance in file ingest or export
#       Arrow is an ideal container for inbound columnar storage formats like Apache Parquet
#    c) lack of memory use, RAM management
#       in pandas, all memory is owned by NumPy or by Python interpreter (difficult to measure the memory use)
#    d) appending data to a Data frame is costly
#       in pandas, all data in a column in a Data Frame must be calculated in the same NumPy array (too restrictive)
#       in Arrow, appending a table is a zero copy operation, requiring no memory allocation
import pandas as pd
df = pd.DataFrame(data=np.random.randint(1, 2, (2, 4)), columns=["column_a", "column_b", "column_c", "column_d"])
print(df)
#     column_a  column_b  column_c  column_d
#  0         1         1         1         1
#  1         1         1         1         1
pa_df = pa.Table.from_pandas(df) # pyarrow.Table
print(pa_df) # pyarrow.Table
pd_df = pa_df.to_pandas()
print(pd_df)
#     column_a  column_b  column_c  column_d
#  0         1         1         1         1
#  1         1         1         1         1

# 7) arrow + csv
from pyarrow import csv
table = csv.read_csv('py_arrow.csv') # pyarrow.Table
print(table)
pd_df = pa_df.to_pandas()
print(pd_df)
#     column_a  column_b  column_c  column_d
#  0         1         1         1         1
#  1         1         1         1         1

