def getInternetSpeed():
    path = sys.argv[0]
    path = list(path)
    while True: # Just cuts back from say C:\User\Example\File.txt to
        if path[len(path)-1] == chr(92) or path[len(path)-1] == '/':
            path = ('').join(path)
            break
        else:
            path.pop(len(path)-1)
    testInternet();
    start = str(datetime.datetime.now())
    x = urllib2.urlopen('https://google.com')
    end = str(datetime.datetime.now())
    x = x.read()
    start = list(start)
    end = list(end)
    for i in range(17):
        start.pop(0)
        end.pop(0)
    start = ('').join(start)
    end = ('').join(end)
    start = float(start)
    end = float(end)
    diff = end - start
    f = open(path+'TEMP.txt','w')
    f.write(x)
    f.close()
    size = os.path.getsize(path+'TEMP.txt')
    os.remove(path+'TEMP.txt')
    print 'It took ' + str(diff) + ' second(s)'
    print 'to get a file that was ' + str(size / 1000) + ' kilobytes large!'

    scale = 1 / diff
    size = size * scale
    size = size / 1000

    print 'Download speed of ' + str(int(size)) + ' kilobytes a second'
