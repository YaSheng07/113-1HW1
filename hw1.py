from typing import List
    # 從 typing 模組中導入 List 類型，用於類型提示。
    
def countLetters(sentence: str) -> List[int]:
    # 定義函數，接收一個字符串，返回一個整數列表，表示每個字母的計數。
    
    letterCount: List[int] = [0] * 26
    # 初始化一個長度為26的列表，對應於英文字母a到z的計數

    for char in sentence:
        # 遍歷輸入的句子中的每個字符
        
        if char.isalpha():
            # 檢查字符是否為字母
            
            index = ord(char) - ord('a')
            # 計算字母在字母表中的索引（a=0, b=1, ..., z=25）
            
            letterCount[index] += 1
             # 增加對應字母的計數

    return letterCount
    # 返回字母計數的列表
pass

def printLetterCount(letterCount: List[int]) -> None:
    # 定義函數，接收一個整數列表，無返回值，目的是打印字母及其計數。

    for i in range(26):
        # 遍歷0到25的數字，對應於字母表中的每個字母。
        
        if letterCount[i] > 0:
            # 檢查該字母的計數是否大於0。
            
            print(f"{chr(i + ord('a'))}: {letterCount[i]}")
            # 如果計數大於0，則打印該字母及其計數
pass

inputSentence: str = "this is an apple"
# 定義輸入的句子

letterCount: List[int] = countLetters(inputSentence)
# 調用函數計算字母計數

printLetterCount(letterCount)
# 打印字母計數