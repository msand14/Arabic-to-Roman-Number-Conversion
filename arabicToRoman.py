def digitConversion(auxNum: str, middleNum: str, endNum: str, arabNum: int):
    """
    Converts an Arabic Number(Units, Tens or Hundreds) into a Roman Number.
    :param auxNum: Iterative Roman letter to add for numbers 1-3, around
                   middleNum or before endNum.
        Example: auxNum = I: (1-3) I, II, III
                             (around middleNum: V) (4) IV, (6-8) VI, VII, VIII
                             (before endNum: X) (9) IX
    :param middleNum: Roman number that represents the middle of the range
                    (5:V, 50:L, 500:D)
    :param endNum: Roman number that represents the end of the range
                    (10:X, 100:C, 1000:M)
    :param arabNum: Arabic number that represents Units,
                     Tens or Hundreds and that will be transformed.
    :return strRomanNum: Roman number to return, that represents Units,
                         Tens or Hundreds.
    """
    strRomanNum = ''
    if 4 > arabNum > 0:
        for i in range(0, arabNum):
            strRomanNum += auxNum
    elif arabNum == 5:
        strRomanNum += middleNum
    elif arabNum == 4:
        strRomanNum += auxNum + middleNum
    elif 5 < arabNum < 9:
        strRomanNum = middleNum
        for i in range(5, arabNum):
            strRomanNum += auxNum
    elif arabNum == 9:
        strRomanNum += auxNum + endNum
    return strRomanNum


def arabToRoman(arab_number: int, bPrintable=False):
    """
    Converts the Arabic Number into a Roman Number and return the Roman Number
    It can also be printed with bPrintable flag as True.
    :param arab_number: Number in Arabic format you want to convert.
    :param bPrintable: True in order to print Input and Output numbers.
    :return roman_number, str: Number written in Roman format which comes from
                               the Arabic input number.
    """
    roman_number = ''
    units = 0
    tens = 0
    # Checking if Units conversion is necessary
    if arab_number % 10 != 0:
        units = int(str(arab_number)[-1])
        roman_number = digitConversion(auxNum='I', middleNum='V', endNum='X',
                                       arabNum=units)
    # Checking if tens conversion is necessary
    if (arab_number - units) % 100 != 0:
        tens = int(str(arab_number)[-2])
        roman_number = digitConversion(auxNum='X', middleNum='L', endNum='C',
                                       arabNum=tens) + roman_number
    # Checking if Hundreds conversion is necessary
    if (arab_number >= 100) and (arab_number - units - tens) % 1000 != 0:
        hundreds = int(str(arab_number)[-3])
        roman_number = digitConversion(auxNum='C', middleNum='D', endNum='M',
                                       arabNum=hundreds) + roman_number
    # Checking if Thousends conversion is necessary
    if 1000 <= arab_number <= 3000:
        thousands = int(str(arab_number)[-4])
        for i in range(0, thousands):
            roman_number = 'M' + roman_number
    if bPrintable:
        print('Arabic number: ' + str(arab_number) +
              ', Roman number: ' + roman_number)
    return roman_number
