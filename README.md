# 🐍 NLP with Fastai

## 📝 Description
This Python script demonstrates **Natural Language Processing (NLP)** using the **Fastai** library. It covers text tokenization, language modeling, and text classification. The script includes examples of training a language model and fine-tuning it for text classification tasks.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/navidfalah/nlp-fastai.git
   cd nlp-fastai
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install additional libraries:
   ```bash
   pip install fastai
   ```

## 🚀 Usage
1. Run the script:
   ```bash
   python nlp_fastai.py
   ```
2. The script will:
   - Tokenize text data using Fastai's tokenizer.
   - Train a language model on the IMDB dataset.
   - Fine-tune the language model for text classification.
   - Generate text predictions using the trained model.

## 📂 File Structure
```
nlp-fastai/
├── nlp_fastai.py  # Main script
├── README.md      # This file
├── requirements.txt  # Dependencies
└── data/          # (Optional) Data folder for local inputs
```

## 🧩 Key Features
- **Text Tokenization**:
  - Tokenize text using Fastai's `Tokenizer` and `SubwordTokenizer`.
- **Language Modeling**:
  - Train a language model using the AWD-LSTM architecture.
  - Generate text predictions using the trained model.
- **Text Classification**:
  - Fine-tune the language model for text classification tasks.
  - Evaluate the model using accuracy and perplexity metrics.

## 📊 Example Outputs
1. **Tokenization**:
   - Tokenized text: `['The', 'U.S.', 'dollar', '$1', 'is', '$1.00', '.']`.
2. **Language Model**:
   - Text generation: `"I liked this movie because..."`.
3. **Text Classification**:
   - Model accuracy: `0.92`.

## 🤖 Libraries Used
- **Fastai**: For NLP tasks, including tokenization, language modeling, and text classification.

## 📈 Performance Metrics
- **Accuracy**: Measures the proportion of correct predictions in text classification.
- **Perplexity**: Measures the performance of the language model.

## 🛠️ Dependencies
- Python 3.x
- Libraries:
  - `fastai`

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author
- **Name**: Navid Falah
- **GitHub**: [navidfalah](https://github.com/navidfalah)
- **Email**: navid.falah7@gmail.com
