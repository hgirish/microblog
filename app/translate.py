import json
import requests
import uuid
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if "MS_TRANSLATOR_KEY" not in app.config or not app.config["MS_TRANSLATOR_KEY"]:
        return _("Error: the translation service is not configured.")
    auth = {
        "Ocp-Apim-Subscription-Key": app.config["MS_TRANSLATOR_KEY"],
        "Ocp-Apim-Subscription-Region": "westus2",
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    r = requests.post(
        "https://api.cognitive.microsofttranslator.com"
        "/translate?api-version=3.0&from={}&to={}".format(
            source_language, dest_language
        ),
        headers=auth,
        json=[{"Text": text}],
    )
    print(r.status_code)
    if r.status_code != requests.codes.ok:
        print(r.reason)
        return _("Error: the translation service failed.")
    response = r.json()
    print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
    return response[0]["translations"][0]["text"]
