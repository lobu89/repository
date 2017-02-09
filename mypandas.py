class DataFrame(object):
    @classmethod
    def from_csv(cls, file_path, delimiting_character=',', quote_character='"'):
        with open(file_path, 'rU') as infile:
            reader = csv.reader(infile, delimiter=delimiting_character, quotechar=quote_character)
            data = []

            for row in reader:
                data.append(row)

            return cls(list_of_lists=data)

        #Task 1:

    def __init__(self, list_of_lists, header=True):
        if header:
            self.header = list_of_lists[0]
        self.data = list_of_lists[1:]

        check_list = self.header

    result = len(check_list) != len(set(check_list))

    if result:
        raise TypeError('Duplicates detected in header, Please have a look')

else:
self.header = ['column' + str(index + 1) for index, column in enumerate(self.data[0])]
self.data = list_of_lists

check_list = self.header
result = len(check_list) != len(set(check_list))

if result:
    raise TypeError('Duplicates detected in header, Please have a look')

self.data = [OrderedDict(zip(self.header, row)) for row in self.data]

#Task2:
self.data = [map(lambda x:x.strip(),row) for row in self.data]
        self.data = [OrderedDict(zip(self.header,row)) for row in self.data]


    def __getitem__(self, item):
        if isinstance(item,(int,slice)):
            return self.data[item]

        elif isinstance(item,str):
            return [row[item] for row in self.data]

        elif isinstance(item,tuple):
            if isinstance(item[0],list) or isinstance(item[1],list):
                if isinstance(item[0],list):
                    rowz = [row for index,row in enumerate(self.data) if index in item[0]]
                else:
                    rowz = self.data[item[0]]

                if isinstance(item[1],list):
                    if all([isinstance(i,int) for i in item[1]]):
                        # python3 use values(),keys(),items() instead of itervalues()...
                        return [[column_value for index,column_value in enumerate(row.values()) if index in item[1]] for row in rowz]
                    elif all([isinstance(i,str) for i in item[1]]):
                        return [[row[col] for col in item[1]] for row in rowz]
                    else:
                        raise TypeError('type error')

                else:
                    return rowz[item[1]]

            else:
                if isinstance(item[0],(int,slice)) and isinstance(item[1],(int,slice)):
                    # python3 use values(),keys(),items() instead of itervalues()...
                    return [list(row.values())[item[1]] for row in self.data[item[0]]]
                elif isinstance(item[1],str):
                    return [row[item[1]] for row in self.data[item[0]]]
                else:
                    raise TypeError('type error')

        elif isinstance(item,list):
             return [[ value for key ,value in row.items() if key in item] for row in self.data]

        #Task4:
        def add_rows(self, list_of_lists):
            col_count = len(self.header)
            # check the length of every new added row equals to len(header)
            if sum([len(row) == col_count for row in list_of_lists]) == len(list_of_lists):
                self.data = self.data + [OrderedDict(zip(self.header, row)) for row in list_of_lists]
                return self
            else:
                raise Exception('incorrect number of columns')

        #task5:
        def add_columns(self, list_of_values，

            columnn_name):
        if len(list_of_values) == len(self.data):
            self.header = self.header + column_name
            self.data = [OrderedDict(zip(list(old_row.keys()) + column_name, list(old_row.values()) + added_values))
                         for old_row, added_values in zip(self.data, list_of_values)]
            return self
        else:
            raise Exception('incorrect number of rows')
