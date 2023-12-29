#Tiktoken Tokenizer 50k vocabulary
#SentencePiece Tokenizer

import torch

with open(r'C:\Users\Artificial\Documents\xxPython\projects\GPTBuild\input.txt','r') as f:
    text=f.read()

    chars=sorted(list(set(text))) #Set of all characters in text, list on this, sort it
    vocab_size=len(chars)

    print(f"Length of Dataset: {len(text)}")
    print(f"First 100 lines of characters: {text[:100]}")

    print(f"Unique characters: {''.join(chars)}") #Unique characters in text
    print(f"Vocabulary size, elements: {vocab_size}") #Unique characters in text

#Mapping from characters to integers, Character Level Tokenizer
stoi={ch:i for i,ch in enumerate(chars)}
itos={i:ch for i,ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s] #Take string, output list of integers
decode = lambda l: ''.join([itos[i] for i in l])#Take list of integers, output string

print(encode("ello"))
print(decode(encode("ello")))

data=torch.tensor(encode(text),dtype=torch.long) #Encode entire dataset and store as integers in torch.Tensor
print(data.shape,data.dtype)
print(data[:50])

n=int(0.9*len(data)) #Split data into Train and Validation sets, 90% train, rest Validation
train_data=data[:n]
val_data=data[n:]

block_size = 8
print(train_data[:block_size+1]) #All these characters follow each other, prediction of next token

x=train_data[:block_size]
y=train_data[1:block_size+1]
for t in range(block_size):
    context=x[:t+1] #Up to t including t
    target=y[t]
    print(f"When input is {context} the target is: {target}") #All these characters follow each other, prediction of next token