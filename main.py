import sys
import glob
import time
import os

fromPath = sys.argv[1]
toPath = sys.argv[2]
sleepTime = float(sys.argv[3])
byteSize = int(sys.argv[4])

fromList = glob.glob(fromPath + '/*')

with open( 'checklist.txt' , 'r+') as file:
    checkList = file.readlines()
    try:        
        for item in checkList:
            fromList.remove(item[:-1])
    except:
        pass

    for fromfilePath in fromList:
        tofilePath = toPath + fromfilePath[fromfilePath.rfind('/'):]
        print(tofilePath)
        sys.stdout.flush()

        try:        
            with open(fromfilePath, 'rb') as fromFile:
                with open( tofilePath , 'wb+') as toFile:
                    fileSize = os.path.getsize(fromfilePath)

                    while fileSize >= byteSize:
                        toFile.write( fromFile.read(byteSize) )
                        print(fileSize)
                        sys.stdout.flush()

                        time.sleep(sleepTime)

                        fileSize -= byteSize
                    
                    toFile.write( fromFile.read(fileSize) )
        except Exception as e:
            print(e)
            sys.stdout.flush()
        file.write(fromfilePath + '\n')
        file.flush()