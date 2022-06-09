import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api', methods=["GET"])
def health_check():
    """Confirms service is running"""
    return "Machine translation service is up and running."


from transformers import MarianTokenizer, MarianMTModel
from typing import List
src = "en"
trg = "fr"
sample_text = ""
model_name = f'/home/chris_engineer/Desktop/TranslationAPI/opus-mt-en-fr-1/data/opus-mt-{src}-{trg}'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

@app.route("/", methods=["POST"])
def api_translate():
    content_type = flask.request.headers.get('Content-Type')
    res = []
    if (content_type == 'application/json'):
        text_input = flask.request.get_json(silent=True)
        text = text_input['text']
        generated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
        res.append({"translation": str([tokenizer.decode(t, skip_special_tokens=True) for t in generated][0])})
        return (flask.jsonify(res[0]) if len(res)>=1 else "Nothing found with this id"), content_type
    elif (content_type == 'multipart/form-data'):
        text = flask.request.form
        text = text["text"]
        generated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
        res.append({"translation": str([tokenizer.decode(t, skip_special_tokens=True) for t in generated][0])})
        return flask.jsonify(res[0]) if len(res)>=1 else "Nothing found with this id"
    else:
        try:
            text = json.loads(request.data)
            generated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
            res.append({"translation": str([tokenizer.decode(t, skip_special_tokens=True) for t in generated][0])})
            return flask.jsonify(res[0]) if len(res)>=1 else "Nothing found with this id"
        except:
            return f"<center>Nothing to process! </center> content: {content_type}"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)



