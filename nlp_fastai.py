# -*- coding: utf-8 -*-
"""nlp_fastai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CSvF1wiXoAR_NBwrMPVXuU8bEbkvG3Dz
"""

from fastai.text.all import *
path = untar_data(URLs.IMDB)

path.ls()

files = get_text_files(path, folders=['train', 'test', 'unsup'])

txt = files[0].open().read(); txt[:75]

spacy = WordTokenizer()
toks = first(spacy([txt]))
print(coll_repr(toks, 30))

first(spacy(['The U.S. dollar $1 is $1.00.']))

tkn = Tokenizer(spacy)
print(coll_repr(tkn(txt), 31))

defaults.text_proc_rules

coll_repr(tkn('&copy; Fast.ai www.fast.ai/INDEX'), 31)

tkn('&copy; Fast.ai www.fast.ai/INDEX')

txts = L(o.open().read() for o in files[:2000])

txt

sp = SubwordTokenizer(vocab_sz=129)
sp.setup(txts)

vocab_size = sp.tok.vocab_size()

# Print the subwords in the vocabulary
print("Chosen Subwords:")
for i in range(vocab_size):
    subword = sp.tok.IdToPiece(i)
    print(f"ID: {i}, Subword: {subword}")

len(txts)

sp_result = list(sp([txt]))
sp_result

len(sp_result[0])

sumation_of_tokens = sum([len(o) for o in txts[:200]])
sumation_of_tokens

toks200 = txts[:200].map(tkn)
toks200[0]

len(toks200)

len(toks200[0])

sumation_of_tokens = sum([len(o) for o in toks200])
sumation_of_tokens

num = Numericalize()
num.setup(toks200)

nums = L([num.encodes(o) for o in toks200])[:20]; nums

' '.join(num.vocab[o] for o in nums[0])

len(num.vocab)

num.vocab[0], num.vocab[1619]

num.vocab[926], num.vocab[14]

num.o2i["campbell"]

num("campbell"), num.encodes("campbell")

print(num.vocab)

### now going for the language model

num200 = toks200.map(num)
dl = LMDataLoader(num200)

x, y = first(dl)
x.shape, y.shape

' '.join(num.vocab[o] for o in x[0][:20])

get_imdb = partial(get_text_files, folders=['train', 'test', 'unsup'])

dls_lm = DataBlock(
    blocks=TextBlock.from_folder(path, is_lm=True),
    get_items=get_imdb, splitter=RandomSplitter(0.1)
).dataloaders(path, path=path, bs=128, seq_len=80)

dls_lm.show_batch(max_n=2)

learn = language_model_learner(
    dls_lm, AWD_LSTM, drop_mult=0.3,
    metrics=[accuracy, Perplexity()]).to_fp16()

learn.fit_one_cycle(1, 2e-2)

learn.unfreeze()
learn.fit_one_cycle(10, 2e-3)

learn.save_encoder('finetuned')

TEXT = "I liked this movie because"
N_WORDS = 40
N_SENTENCES = 2
preds = [learn.predict(TEXT, N_WORDS, temperature=0.75)
 for _ in range(N_SENTENCES)]
print("\n".join(preds))

dls_clas = DataBlock(
    blocks=(TextBlock.from_folder(path, vocab=dls_lm.vocab), CategoryBlock),
    get_y=parent_label,
    get_items=partial(get_text_files, folders=['train', 'test']),
    splitter=GrandparentSplitter(valid_name='test')
).dataloaders(path, path=path, bs=128, seq_len=72)

num_samp = toks200[:10].map(num)

num_samp.map(len)

learn = text_classifier_learner(dls_clas, AWD_LSTM, drop_mult=0.5,
                             metrics=accuracy).to_fp16()

learn = learn.load_encoder('finetuned')

learn.fit_one_cycle(1, 2e-2)

learn.freeze_to(-2)
learn.fit_one_cycle(1, slice(1e-2/(2.6**4), 1e-2))

learn.freeze_to(-3)
learn.fit_one_cycle(1, slice(5e-3/(2.6**4),5e-3))

learn.unfreeze()
learn.fit_one_cycle(2, slice(1e-3/(2.6**4),1e-3))

