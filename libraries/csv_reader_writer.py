import csv

if __name__ == '__main__':
  # read in a *.csv file
  with open("foo.csv", 'r') as fin:
      for row in csv.reader(fin): # ['',           'A',              'B',              'C',              'D'             ]
          print(row)              # ['2016-07-01', '0.858490705656', '-1.13613367816', '-1.35393014638', '-0.46613600423'] 

  with open('foo2.csv', 'wb') as fout:
    writer = csv.writer(fout, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['', 'A', 'B', 'C', 'D'])
    writer.writerow(['2016-07-01', '0.858490705656', '-1.13613367816', '-1.35393014638', '-0.46613600423'])
