# pip3 install pyarrow
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
buf = pa.py_buffer(data) # a Buffer
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
# b) memory_map([filepath]):
mmap = pa.memory_map('example3.dat')
print(mmap.read(4))     # b'some': this DOES NOT allocate new memory, as it references the maaped memory when read

# read() vs. read_buffer()
# read(): this implements the standard Python file read API
# read_buffer(): this reads into an Arrow Buffer object
print(mmap.seek(0)) # 0
buf = mmap.read_buffer(4)
print(buf) # <pyarrow.lib.Buffer object at 0x10cfc3960>
print(buf.to_pybytes()) # b'some'

# 4) In-Memory Reading and Writing
#   for serialization and deserialization of in-memory data
writer = pa.BufferOutputStream() # for in-memory writing
print(writer.write(b'hello, friends')) # 14
buf = writer.getvalue()
print(buf) # <pyarrow.lib.Buffer object at 0x10b6bdea0>
print(buf.size) # 14
reader = pa.BufferReader(buf) # for in-memory reading
print(reader.seek(7)) # 7
print(reader.read(7)) # b'friends'
