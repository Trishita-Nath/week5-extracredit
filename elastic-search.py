from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc1 = {
    'author': 'Trishita',
    'text': 'Document1 text data goes here. Allow search for cycle',
    'timestamp': datetime.now(),
}
doc2 = {
    'author': 'John',
    'text': 'Document2 text data goes here. Allow search for pen',
    'timestamp': datetime.now(),
}
doc3 = {
    'author': 'Thomas',
    'text': 'Document3 text data goes here. Allow search for cycle',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=41, body=doc1)
print(res['created'])
res = es.index(index="test-index", doc_type='tweet', id=42, body=doc2)
print(res['created'])
res = es.index(index="test-index", doc_type='tweet', id=43, body=doc3)
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=41)
print(res['_source'])
res = es.get(index="test-index", doc_type='tweet', id=42)
print(res['_source'])
res = es.get(index="test-index", doc_type='tweet', id=43)
print(res['_source'])
es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match": {"text": "cycle"}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])