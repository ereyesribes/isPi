
def isPi():
    try:
        modelFile = open('/sys/firmware/devicetree/base/model', 'r')
        modelText = modelFile.read()[:-1]

        if "raspberry" in modelText.lower():
            return True
        return False
    except:
        return False


def piModel():
    try:
        modelFile = open('/sys/firmware/devicetree/base/model', 'r')
        modelText = modelFile.read()[:-1]

        return modelText
    except:
        return False


if __name__ == "__main__":
    print ("isPi" + str(isPi()))
    print ("piModel" + piModel())
