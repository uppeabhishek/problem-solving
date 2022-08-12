class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        dic = {
            10: ('Billion', 1),
            9: ('Million', 3),
            8: ('Million', 2),
            7: ('Million', 1),
            6: ('Hundred', 1),
            5: ('Thousand', 2),
            4: ('Thousand', 1)
        }
        
        ones = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        
        tens = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred'
        }
        
        def getTensHundreds(cnt, key):
            return 10 ** (cnt - 1) * key
    
        def getLength():
            nonlocal tempNum
            cnt = 0
            while tempNum:
                numArray.append(tempNum % 10)
                tempNum = tempNum // 10
                cnt += 1
            
            return cnt
        
        tempNum = num
        numArray = deque([])
        
        length = getLength()
        
        result = []
        
        while length > 0:
                    
            key = numArray[length - 1]
            
            if key == 0:
                length -= 1
                continue
            
            if length > 3:
                value, cnt = dic[length]
                tens_hundreds_value = getTensHundreds(cnt, key)
                if cnt == 1:
                    result.append(ones[key])
                    result.append(value)
                    if numArray[length - 2] == 0 and numArray[length - 3] == 0 and length == 6:
                        result.append("Thousand")
                elif cnt == 2:
                    if key == 1:
                        result.append(tens[key * 10 + numArray[length - 2]])
                        result.append(value)
                        length -= 1
                    else:
                        result.append(tens[tens_hundreds_value])
                        if numArray[length - 2] == 0:
                            result.append(value)
                else:
                    result.append(ones[key])
                    result.append(tens[tens_hundreds_value // key])
                    
                    if numArray[length - 2] == 0 and numArray[length - 3] == 0:
                        result.append("Million")
                        
            elif length == 3:
                result.append(ones[key])
                result.append(tens[100])
                
            elif length == 2:
                if key == 1:
                    result.append(tens[key * 10 + numArray[0]])
                    break
                tens_hundreds_value = getTensHundreds(2, key)
                result.append(tens[tens_hundreds_value])
            else:
                result.append(ones[key])

            length -= 1
        
        return " ".join(result)
        
        
        