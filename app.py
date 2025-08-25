from model import facebook_m2m100_1.2B as model
#Example
sentences = [
    "The party shall deliver the goods within 10 days.",
    "This contract is governed by the laws of the Republic of Serbia.",
    "The supplier guarantees the quality of the service."
]

app = FastAPI(title="English-Serbian Translation API")


# Request body
class TranslationRequest(BaseModel):
    text: str
    source_lang: str  # "en" or "sr"
    target_lang: str  # "en" or "sr"


@app.post("/translate")
def translate(req: TranslationRequest):
    translation = model.get_translation(req.source_lang, req.target_lang, req.text)
    return {"translation": translation}
