from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc1 = {
    'author': 'Trishita',
    'text': 'Document1 text data goes here. Allow search for car',
    'timestamp': datetime.now(),
}
doc2 = {
    'author': 'John',
    'text': 'Document2 text data goes here. Allow search for fan',
    'timestamp': datetime.now(),
}
doc3 = {
    'author': 'Thomas',
    'text': 'Document3 text data goes here. Allow search for car',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc1)
print(res['created'])
res = es.index(index="test-index", doc_type='tweet', id=2, body=doc2)
print(res['created'])
res = es.index(index="test-index", doc_type='tweet', id=3, body=doc3)
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])
res = es.get(index="test-index", doc_type='tweet', id=2)
print(res['_source'])
res = es.get(index="test-index", doc_type='tweet', id=3)
print(res['_source'])
es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match": {"text": "car"}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])