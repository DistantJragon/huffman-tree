class Character:
    def __init__(self, charcter):
        self.name = charcter
        self.ascii = ord(self.name)
        self.binaryASCII = str(bin(self.ascii))
        self.binaryASCII = self.binaryASCII[2:]
        self.compressedASCII = ''
        self.frequency = 0

class Branch:
    def __init__(self, branch1, branch2):
        self.trunk = [branch1, branch2]
        self.frequency = branch1.frequency + branch2.frequency
        self.name = 'branch'

def make_character_list(givenList, givenString):
    firstCharacter = givenString[0]
    givenList.append(Character(firstCharacter)) 
    givenList[-1].frequency = givenString.count(firstCharacter)
    newString = givenString.replace(firstCharacter, '')
    if len(newString) > 0:
        givenList = make_character_list(givenList, newString)
    return givenList

def organize_tree(givenList):
    while len(givenList) > 2:
        givenList.sort(reverse=True, key=frequency_sort)
        tempBranch = Branch(givenList[-1], givenList[-2])
        givenList.pop()
        givenList.pop()
        givenList.append(tempBranch)
    return

def calculate_binaries(givenList, charTable, cmpATable, binaryRep = ''):
    left = givenList[0]
    right = givenList[1]
    if left.name != 'branch':
        left.compressedASCII = binaryRep + '0'
        charTable.update({left.name: left})
        cmpATable.update({left.compressedASCII: left})
    else:
        calculate_binaries(left.trunk, charTable, cmpATable, binaryRep + '0')
    if right.name != 'branch':
        right.compressedASCII = binaryRep + '1'
        charTable.update({right.name: right})
        cmpATable.update({right.compressedASCII: right})
    else:
        calculate_binaries(right.trunk, charTable, cmpATable, binaryRep + '1')
    return

def frequency_sort(item):
    return item.frequency
    
def make_string_binary(givenString, givenTable, compress = False):
    finalString = ''
    if compress:
        for char in givenString:
            finalString = finalString + givenTable[char].compressedASCII
    else:
        for char in givenString:
            finalString = finalString + givenTable[char].binaryASCII
    return finalString

def uncompress_string(givenString, givenTable):
    currentBinary = ''
    finalString = ''
    keyList = givenTable.keys()
    for char in givenString:
        currentBinary = currentBinary + char
        if currentBinary in keyList:
            finalString = finalString + givenTable[currentBinary].name
            currentBinary = ''
    return finalString

def make_flow_chart():
    return

inputText = "[Verse 1]\nI don't feel it when they talk on me, I won't take it\nGet the fuck from 'round me, let's face it\nYou can't dive in this back in my basement\nIf you don't get what I'm saying, I'm not changing for you\nProblems, I got too many of 'em\nSo I'm running through the days to catch up on 'em, I got plenty of 'em\nNo one hates me more than I do So I'm the only one that decidin' when the end is coming\n\n[Pre-Chorus]\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\nI push myself to the edge\nFeel it in my chest\nNone of y'all can stand in my way\n\n[Chorus]\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\nI push myself to the edge\nFeel it in my chest\nNone of y'all can stand in my way\nI push myself to the edge\nBetter come correct when you stand up in my face\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\n\n[Verse 2]\nN-Nah you, fuck that you aimin', we bust back\nWon't do representin', we bombin' and trust that\nOn my mama, it's a problem whenever we come back\nY'all don't want that precision, with this it is unmatched, I\nNotice how they look at me\nI run myself right through the walls, I don't worry 'bout that at all\nUnderstand I'm everything that you couldn't be\nBecause I put myself through hell, I'm guessin' that you can tell\n\n[Pre-Chorus]\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\nI push myself to the edge\nFeel it in my chest\nNone of y'all can stand in my way\n\n[Chorus]\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\nI push myself to the edge\nFeel it in my chest\nNone of y'all can stand in my way\nI push myself to the edge\nBetter come correct when you stand up in my face\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\n\n[Bridge]\nHolding myself back\nHoping I don't crash\nFor the last time my hands on my brakes\nNone of this shit was planned as my fate\nRun your mouth, get you into your grave\nAnd none of y'all can stand in my way\n\n[Chorus]\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\nI push myself to the edge\nFeel it in my chest\nNone of y'all can stand in my way\nI push myself to the edge\nBetter come correct when you stand up in my face\nI push myself to the edge\nLookin' for the end, hopin' this time I won't break\n\n[Outro]\nHoping this time I won't break"
characterList = []
characterList = make_character_list(characterList, inputText)
characterList.sort(reverse=True, key=frequency_sort)
huffmanTree = characterList.copy()
del characterList
organize_tree(huffmanTree)
characterTable = {}
compressedASCIITable = {}
calculate_binaries(huffmanTree, characterTable, compressedASCIITable)
uncompressedBinaryString = make_string_binary(inputText, characterTable)
compressedBinaryString = make_string_binary(inputText, characterTable, True)
englishOutput = uncompress_string(compressedBinaryString, compressedASCIITable)
print(100 * (1 - len(compressedBinaryString)/len(uncompressedBinaryString)))
breakpoint()
x = 1