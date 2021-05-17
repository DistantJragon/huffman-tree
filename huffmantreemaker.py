class Character:
    def __init__(self, charcter):
        self.name = charcter
        self.ascii = ord(self.name)
        self.binaryASCII = bin(self.ascii)
        self.compressedASCII = ''
        self.frequency = 0

class Branch:
    def __init__(self, branch1, branch2):
        self.trunk = [branch1, branch2]
        self.frequency = branch1.frequency + branch2.frequency
        self.name = 'branch'


def make_character_list(givenList, string):
    firstCharacter = string[0]
    givenList.append(Character(firstCharacter)) 
    givenList[-1].frequency = string.count(firstCharacter)
    newString = string.replace(firstCharacter, '')
    if len(newString) > 0:
        givenList = make_character_list(givenList, newString)
    return givenList

def organize_tree(givenList):
    givenList.sort(reverse=True, key=frequency_sort)
    tempBranch = Branch(givenList[-1], givenList[-2])
    givenList.pop()
    givenList.pop()
    givenList.append(tempBranch)
    if len(givenList) > 2:
        organize_tree(givenList)
    return

def calculate_binaries(givenList, binaryRep = ''):
    if givenList[0].name != 'branch':
        givenList[0].compressedASCII = binaryRep + '0'
        print(givenList[0].name, binaryRep + '0')
    else:
        calculate_binaries(givenList[0].trunk, binaryRep + '0')
    if givenList[1].name != 'branch':
        givenList[1].compressedASCII = binaryRep + '1'
        print(givenList[1].name, binaryRep + '1')
    else:
        calculate_binaries(givenList[1].trunk, binaryRep + '1')
    return

def frequency_sort(item):
    return item.frequency
    
inputText = 'the quick brown fox jumps over the lazy dog'
characterList = []
characterList = make_character_list(characterList, inputText)
characterList.sort(reverse=True, key=frequency_sort)
huffmanTree = characterList.copy()
organize_tree(huffmanTree)
calculate_binaries(huffmanTree)
breakpoint()
x = 1