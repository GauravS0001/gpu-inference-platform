class DummyModel:

    def predict(self, text):

        return {
            "input": text,
            "prediction": "healthy"
        }


model = DummyModel()