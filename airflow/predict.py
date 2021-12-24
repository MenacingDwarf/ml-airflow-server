import mlflow
import pickle

mlflow.set_tracking_uri("http://localhost:5000")

def predict(review):
    with open("/home/stanislav/Hadoop/run_id.txt", "r") as f:
        run_id = f.read()
    logged_model = "runs:/" + run_id + "/sklearn-model"
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    
    vectorizer = pickle.load(open("/home/stanislav/Hadoop/tfidf.pickle", "rb"))
    return loaded_model.predict(vectorizer.transform(review))

if __name__ == "__main__":
    print(predict(['the best movie']))
