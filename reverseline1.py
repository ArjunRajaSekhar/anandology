f = open("sample.txt", "rb")
s = f.read()
f.close()
f = open("sample_output.txt", "wb")
f.write(s[::-1])
f.close()
