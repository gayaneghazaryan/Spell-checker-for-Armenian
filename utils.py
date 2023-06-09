import pandas as pd

def import_text():
    data = pd.concat(map(pd.read_csv, [r'train.csv', r'test.csv']), ignore_index=True)['target']
    data2 = pd.concat(map(pd.read_csv, [r'train_arpa.csv', r'test_arpa.csv']), ignore_index=True)[['Sentence1', 'Sentence2']]
    data2 = pd.concat([data2['Sentence1'],data2['Sentence2']], ignore_index = True)
    final_data = pd.concat([data, data2], ignore_index=True)
    return ' '.join(final_data)