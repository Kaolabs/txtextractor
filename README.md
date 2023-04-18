paste text to extract from into "input_file.txt"

edit what text you want to extract here 
matches = re.findall(r'0\.0\.\d+', text)

currently set to extract wallet addresses from a body of text

run
python extractor.py

exports as .csv 
