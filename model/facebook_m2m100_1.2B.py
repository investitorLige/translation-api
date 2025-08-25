
model_name = "facebook/m2m100_1.2B"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)


def get_translation(src, tgt, text, tokenizer=tokenizer, model=model):
    model.to('cuda')

    tokenizer.src_lang = src
    target_lang = tgt

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to('cuda')

    generated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.get_lang_id(target_lang)
    )

    translations = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    for en, sr in zip(sentences, translations):
        output_latin = translit(sr, 'sr', reversed=True)  # Cyrillic → Latin
        print(f"EN: {en}\nSRC: {sr}\nSRL: {output_latin}\n")
    return output_latin
