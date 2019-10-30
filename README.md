# BLEU for Japanese
This project is subject to calculation of BLEU score for Japanese NLP tasks in an easy-to-use and comprehensive manner.
## Getting Started
### Prerequisites
* [MeCab](http://taku910.github.io/mecab/)
### Dependencies
* Mecab-bindings according to your environment
** mecab-python
** mecab-python3
** mecab-python-windows
* [NLTK](https://www.nltk.org/)
## How to use
1. Tokenization of Japanese text
* Save text you want to tokenize as "owakati.txt" in the folder where this repository is cloned.
* Execute owakati.py.
* the text will be tokenized in the same file.
2. Preparation of reference and hypothesis files
* Put reference and hypothesis text as separate two utf-8 encoded text files as named "txt1.txt" and "txt2.txt" in the cloned folder.
* hypothesis means a resource to be compared with reference, e.g. output from machine translation.
* Both text resources should be tokenized as described in the previous step.
3. Calculation of BLEU
* Execute sbleu.py.
* BLEU scores of each sentence pair will be output in "bleu.txt".
## Version
1.0.0
## Author
[Takeshi Hayakawa](https://github.com/taquecih)
## References
* [NLTK 3.4.5 documentation](NLTK 3.4.5 documentation)
* Taku Kudo, Kaoru Yamamoto, Yuji Matsumoto: Applying Conditional Random Fields to Japanese Morphological Analysis, Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing (EMNLP-2004), pp.230-237 (2004.)
