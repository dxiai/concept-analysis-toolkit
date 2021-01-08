from json import load
from html.parser import HTMLParser
from re import sub
from sklearn.feature_extraction.text import CountVectorizer


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += sub(r'<.*?>', '', data)


def print_str_scalar_dict_sorted(dict_to_print,key_name = 'key',val_name = 'value'):
    ordered_counts = sorted(dict_to_print.items(), key=lambda kv: kv[1])
    print("{:<30} {:<5}".format(key_name, val_name))
    for key, value in ordered_counts[::-1]:
        print("{:<30} {:<5}".format(key, str(value)))


class TermCounter():
    def __init__(self, fields, programming, frameworks, skills):
        self.fields = fields
        self.programming = programming
        self.frameworks = frameworks
        self.skills = skills

        vocabulary_topics = [field, programming, frameworks, skills]
        vocabulary = list()
        self.terms_map = dict()
        self.terms_count = dict()
        ind = 0
        for topic in vocabulary_topics:
            for term in topic:
                vocabulary.extend(term)
                self.terms_count[term[0]] = 0
                for _ in term:
                    self.terms_map[ind] = term[0]
                    ind += 1
        self.vectorizer = CountVectorizer(ngram_range=(1, 2), vocabulary=vocabulary,
                                          token_pattern=r'(?u)\b\w[A-Za-z0-9_+#]+|\br,|\br\b|\br.')

    def clear_counts(self):
        for key in self.terms_count.keys():
            self.terms_count[key] = 0

    def extract_counts(self, strings):
        if isinstance(strings, str):
            strings = [strings]
        occurrence_matrix = self.vectorizer.transform(strings)
        occurrences = list()
        for ind in range(occurrence_matrix.shape[0]):
            occs = dict()
            for entry in range(occurrence_matrix.indptr[ind], occurrence_matrix.indptr[ind + 1]):
                term = self.terms_map[occurrence_matrix.indices[entry]]
                count = occurrence_matrix.data[entry]
                if term in occs:
                    occs[term] += count
                else:
                    occs[term] = count
                self.terms_count[term] += count
            occurrences.append(occs.items())
        return occurrences

    def print_counts(self):
        print_str_scalar_dict_sorted(self.terms_count,'keyword','nb_occurrences')


field = [['mathematics', 'mathematik', 'math'],
         ['wirtschaftsinformatik'],
         ['physics', 'physik'],
         ['computer science', 'informatik', 'cs'],
         ['operations research', 'operational research'],
         ['engineering'],
         ['data science'],
         ['statistics', 'statistik'],
         ['economics', 'econometrics', 'quantitative finance'],
         ['bioinformatics', 'bioinformatik', 'computational biology'],
         ['genomics', 'genetik']
         ]

programming = [['c++', 'c,', 'c/c++'],
               ['python'],
               ['matlab'],
               ['R', 'r,'],
               ['java'],
               ['c#'],
               ['sql'],
               ['nosql'],
               ['go']
               ]

frameworks = [['tensorflow'],
              ['scikit', 'scikit-learn'],
              ['scipy'],
              ['keras'],
              ['theano'],
              ['hadoop'],
              ['spark'],
              ['pytorch']
              ]

skills = [['machine learning', 'maschinelles lernen', 'ml'],
          ['artificial inteligence', 'ai'],
          ['deep learning'],
          ['stochastic modeling'],
          ['data analysis'],
          ['time series'],
          ['large datasets', 'big data', 'grosse datenmengen'],
          ['optimization', 'optimierung'],
          ['programming', 'programmieren'],
          ['scripting', 'skripten'],
          ['database', 'databases', 'datenbank', 'datenbanken'],
          ['visualization', 'visualisierung'],
          ['language processing', 'NLP'],
          ['visual computing', 'computer vision', 'cv'],
          ['linux', 'unix'],
          ['windows'],
          ['finances', 'investment management', 'financial data'],
          ['life science', 'life sciences'],
          ['internet of things', 'of things', 'iot']
          ]

if __name__ == '__main__':

    counter = TermCounter(field, programming, frameworks, skills)

    with open("Jobs27-09-19.json", "r") as read_file:
        data = load(read_file)
        companies = dict()
        industries = dict()
        print('-------------------------   job offers  -----------------------------')
        for item in data:
            html_filter = HTMLFilter()
            html_filter.feed(item['description'])
            vector = counter.extract_counts(html_filter.text)
            if item['company'] in companies:
                companies[item['company']] += 1
            else:
                companies[item['company']] = 1
            if item['industry'] in industries:
                industries[item['industry']] += 1
            else:
                industries[item['industry']] = 1
            print('title: {:<30} company: {:<30} industry: {:<30}'.format(item['title'], item['company'],
                                                                          item['industry']))
            for key, value in vector[0]:
                print("{:<30} {:<5}".format(key, str(value)))
            print('\n')
        print('-------------------------   data size   -----------------------------')
        print('Number of job offers: ' + str(len(data)) + '\n')
        print('\n-----------------------   companies   -----------------------------')
        print_str_scalar_dict_sorted(companies,'company','nb_offers')
        print('\n-----------------------   industries  -----------------------------')
        print_str_scalar_dict_sorted(industries,'industry','nb_companies')
        print('\n-----------------------   keyword counts --------------------------')
        counter.print_counts()
