## [Stupid ~~Hack~~ Scam 2022](https://app.hackjunction.com/events/stupid-hack-2022)
organized by <b>Junction</b>

### About
Text encrypter <-> decrypter with human language crypter solution, NLP model trained with Romeo and Juliet by William Shakespeare

#### Why?

Due to the future need of quantum computer resistant cryptology, solution must be made to provide continuing for a secure communication.
Computers are good with numbers and random characters piled to togethor.

Computers having difficulties with:
- natural language
- <i>love</i>

This application uses the book Romeo and Juliet to find closest similar words for the encrypted text and process a procedure to match the input text words.

### Example

Input:
<code>Hello, where is the food hidden?</code>

Encrypted:

Output:
<code>rich peppered seems strangers eats drums</code>

### Preview
<img src="https://github.com/eherra/stupidhack2022/blob/main/docs/images/info.png" alt="reviewPhoto">


#### Application's known issues
- This cryptography approach not <i>really</i> secure. :)
- Bugs
- Spaghetti code

#### How to run the app

To run this project you will need Python3.

Start by cloning this project. Enter root and create file called ```.env``` and paste the following there:

```
SECRET_KEY=<your secret key>
```

then do the following commands:

```
python3 -m venv venv
source venv/bin/activate
```

install requirements with:

```pip install -r requirements.txt```

Start with:

```flask run```