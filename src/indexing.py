from marqo import Client
import json
import math
import numpy as np
import copy
import pprint

def read_process_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
          entry['title'] = entry['title'].replace('- Wikipedia', '')
          entry['docDate'] = str(entry['docDate'])
    return data


def read_tsv_file(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()
    
def split_large_documents(documents, field='content', max_length= 5e4):
    new_data = []
    for dat in documents:
        content = dat[field]
        N = len(content)

        if N >= max_length:
            n_chunks = math.ceil(N / max_length)
            new_content = np.array_split(list(content), n_chunks)

            for _content in new_content:
                new_dat = copy.deepcopy(dat)
                new_dat[field] = ''.join(_content)
                new_data.append(new_dat)
        else:
            new_data.append(dat)
    return new_data

dataset = read_process_json_file("dataset/simplewiki.json")
data = split_large_documents(dataset)
print(f"loaded data with {len(data)} entries")


index_name = 'simplewiki'
client = Client(url='http://localhost:8882')

try:
    client.delete_index(index_name)
except:
    pass

client.create_index(index_name, model='onnx/all_datasets_v4_MiniLM-L6')

responses = client.index(index_name).add_documents(
    data, client_batch_size=100,
    tensor_fields=["title", "content"]
)

#pprint.pprint(responses)






