# PCR-Chain
a tool for partial code reuse.
# Attention
The python version we use is 3.6.1, and the openai version is 0.8.0. The version you use should be greater than this version as much as possible.
# Installation
To use OpenAI in your project, you need to install the OpenAI API.
Using ```pip install openai```
# Usage
In ```Unit.py``` file, you need to set the openai_key to use OpenAI API.
```
openai.api_key = "YOUR_API_KEY"
```
After setting, put the code to be repaired into ```java_code.txt```, and then run ```Assembler.py```
