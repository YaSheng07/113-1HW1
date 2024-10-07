def celsius_to_fahrenheit(celsius: float) -> float:
    # 定義一個函數，名稱為 celsius_to_fahrenheit，接收一個浮點數參數 celsius，並返回一個浮點數。
    
    """將攝氏溫度轉換為華氏溫度"""
    
    return (celsius * 9/5) + 32
    # 編入攝氏轉華氏的公式計算並返回華氏溫度


import unittest
# 導入 Python 的單元測試框架，提供測試功能。

class TestTemperatureConversion(unittest.TestCase):
    """
    測試攝氏轉華氏的功能。
    單元測試是對最小可測試單元的驗證，確保它按預期工作。
    通常包括獨立函數或方法，確保其輸入和輸出符合預期。
    """
    
    def test_conversion(self):
        # 測試各種攝氏溫度
        
        self.assertEqual(celsius_to_fahrenheit(0), 32)      # 測試將 0°C 轉換為 32°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)    # 測試水的沸點將 100°C 轉換為 212°F。
        self.assertEqual(celsius_to_fahrenheit(-40), -40)    # 測試攝氏和華氏溫度是否相等 -40°C 轉換為 -40°F
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)     # 測試人體正常體溫 37°C 是否約等於 98.6°F
        self.assertEqual(celsius_to_fahrenheit(-273.15), -459.67)  # 測試絕對零度 -273.15°C 是否約等於 -459.67°F

if __name__ == '__main__':
    unittest.main()  # 當程式作為主程式執行時，啟動單元測試，執行所有以 test_ 開頭的方法。