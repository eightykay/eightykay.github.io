import glob

data = glob.glob('dat/*')
#data = ['20230306', '20230313', '20230320', '20230327',
        #'20230403']
data = sorted(data)[::-1]

with open('index.html', 'w') as fid:
    fid.write('<!DOCTYPE html>\n')
    fid.write('<html>\n')
    fid.write('<link rel="stylesheet" href="style.css" />\n')
    fid.write('<head>\n')
    fid.write('<meta http-Equiv="Cache-Control" Content="no-cache" />\n<meta http-Equiv="Pragma" Content="no-cache" />\n<meta http-Equiv="Expires" Content="0" />\n')
    fid.write('<title>eightykay</title>\n')
    fid.write('</head>\n')
    fid.write('<body>\n')
    for i0 in data:
        with open(i0, 'r') as fid1:
            x = fid1.read()
        fid.write(x)
        fid.write('<hr class="solid">\n')
    fid.write('</body>\n')
    fid.write('</html>')

    

