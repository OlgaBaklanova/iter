import json
import hashlib

class My_iterator:

    def __init__(self, file_name: str):
        self.start = -1
        with open(file_name, 'r', encoding='utf8') as file:
            self.countries = json.load(file)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.countries):
            raise StopIteration
        return self.countries[self.start]['name']['common']

if __name__ == '__main__':
    list_countries = My_iterator('countries.json')
    with open('res.txt', 'w', encoding='utf8') as file:
        count = 0
        for country in list_countries:
            count += 1
            file.write(f'{country} - https://ru.wikipedia.org/wiki/{country.replace(" ", "_")}\n')

def LineReader(filename: str):

    with open(filename, 'r', encoding='utf8') as my_file:
        while True:
            line = my_file.readline()
            if line:
                yield hashlib.md5(line.encode('utf8')).hexdigest()
            else:
                break



for item in LineReader('res.txt'):
    print(item)
