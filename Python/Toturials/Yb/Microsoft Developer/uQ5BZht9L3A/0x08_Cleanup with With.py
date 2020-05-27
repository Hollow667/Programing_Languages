## Writing to a file
stream = open('demo.txt', 'wt')
stream.write('Lorem ipsum dolar')
stream.close() # THIS IS REALLY IMPROTANT!!

## Re-weriting with a try/finally
try:
    stream = open('demo.txt', 'wt')
    stream.write('Lorem ipsum dolar')
finally:
    stream.close() # THIS IS REALLY IMPORYANT!!
    
## Simplifing with With
with open('demo.txt', 'wt') as stream:
    stream.write('Lorem ipsum dolar')
