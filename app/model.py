class InferenceModel:

    def predict(self, prompt):

        return {
            "prompt": prompt,
            "response": "inference completed"
        }


model = InferenceModel()