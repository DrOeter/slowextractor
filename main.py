import sys
import glob
import time
import os

fromPath = sys.argv[1]
toPath = sys.argv[2]
sleepTime = float(sys.argv[3])
byteSize = int(sys.argv[4])

fromList = glob.glob(fromPath + '/*')

for fromfilePath in fromList:
    tofilePath = toPath + fromfilePath[fromfilePath.rfind('/'):]
    print(tofilePath)

    with open(fromfilePath, 'rb') as fromFile:
        with open( tofilePath , 'wb+') as toFile:
            fileSize = os.path.getsize(fromfilePath)

            while fileSize >= byteSize:
                toFile.write( fromFile.read(byteSize) )
                print(fileSize)

                time.sleep(sleepTime)

                fileSize -= byteSize
            
            toFile.write( fromFile.read(fileSize) )