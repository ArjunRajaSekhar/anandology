with open('sample.txt') as f,  open('sample_output.txt', 'w') as fout:
    fout.writelines(reversed(f.readlines()))
