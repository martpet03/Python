with open('zadacha3.txt', 'r') as f:

  line_count = 0
  word_count = 0
  symbol_count = 0
  
  for line in f:
    line_count += 1
    
    for word in line.split():
      word_count += 1
      
      for symbol in word:
        symbol_count += 1


print(f'Number of lines: {line_count}')
print(f'Number of words: {word_count}')
print(f'Number of symbols: {symbol_count}')
