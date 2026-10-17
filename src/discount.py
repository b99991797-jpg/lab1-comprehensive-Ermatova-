   import os

   def calculate_discount(price, discount_rate):
       # Эта строка специально сделана очень длинной, чтобы нарушить правило max-line-length = 80 в файле .flake8
       final_price = price - (price * discount_rate)
       return final_price
