import tempfile
import os



filesize_required = 100000000 #in MB


with tempfile.NamedTemporaryFile(mode='w+b', prefix='test', suffix='.txt', delete=False) as fp:
    file_path = fp.name
    min_unit = 1024    # 1 KB
    #min_unit = 1024*1024    # 1 MB
    
    for inner in range(filesize_required):
        #print(f'{outer}_{inner}')
        fp.write(b'\xAA')    
        #fp.write(b'\xAA' * min_unit)    
        #print(f'written {(1 + inner) * min_unit} Bytes')

    
    print(file_path)
    fp.seek(0)
    file_size = os.stat(file_path).st_size # in bytes
    print(f'Final filesize is {file_size} bytes / {file_size/1024} KB / {file_size/(1024*1024)} MB ')
    print('Done!')
    
