class QueryResults:

    def __init__(self, doc_id, doc_name, weight) -> None:
        super().__init__()
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.weight = weight

    def __str__(self) -> str:
        return "id:{0} - name:{1}  - weight:{2}".format(str(self.doc_id), self.doc_name, self.weight)
