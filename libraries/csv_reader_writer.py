import csv

if __name__ == '__main__':
  # read in a *.csv file
  with open("foo.csv", 'r') as fin:
      reader = csv.reader(fin)
      headers = reader.next()
      print(headers)
      for row in reader: # ['',           'A',              'B',              'C',              'D'             ]
          print(row)     # ['2016-07-01', '0.858490705656', '-1.13613367816', '-1.35393014638', '-0.46613600423'] 

  # read in a *.csv file as DictReader
  with open("foo.csv", 'r') as fin:
      reader = csv.DictReader(fin)
      print(reader.fieldnames) # ['',           'A',              'B',              'C',              'D'             ]
      for row in reader:
          print(row['D'])      # -0.46613600423

  # write to a *.tsv file
  with open('foo.tsv', 'wb') as fout:
    headers = ['Date', 'A', 'B', 'C', 'D']
    writer = csv.writer(fout, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerow(['2016-07-01', '0.858490705656', '-1.13613367816', '-1.35393014638', '-0.46613600423'])

  # write to a *.tsv file via DictWriter
  with open('foo_dict.csv', 'wb') as fout:
      headers = ['Date', 'A', 'B', 'C', 'D']
      writer = csv.DictWriter(fout, fieldnames=headers)
      writer.writeheader()
      writer.writerow({'Date': '2016-07-01', 'A': '0.858490705656', 'B': '-1.13613367816', 'C': '-1.35393014638', 'D': '-0.46613600423'})
