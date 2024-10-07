n = input("請輸入一個正整數: ")
    # 輸入一個正整數並反轉

if n.isdigit() and int(n) > 0:
    # 確保輸入為正整數
    
    reversed_n = int(n[::-1])
    # 反轉字符串並轉回整數
    
    print(f"反轉後的數字是: {reversed_n}") # 輸出反轉後的數字
else:
    print("請輸入一個正整數！") # 如果輸入的數值不正確，顯示錯誤訊息