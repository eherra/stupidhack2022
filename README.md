## [Stupid ~~Hack~~ Scam 2022](https://app.hackjunction.com/events/stupid-hack-2022)
This app was build during a 24-hour length hackathon organized by <b>Junction</b>

### About
Text encrypter <-> decrypter with human language cryptography solution, NLP model trained with Romeo and Juliet by William Shakespeare

### Why?

Due to the future need of quantum computer resistant cryptography, solution must be innovated in order to provide continuity for a secure communication.

### Case
Computers are good with numbers and random characters piled togethor.

Computers having difficulties with:
- natural language
- <i>love</i>

Therefore this application uses the book Romeo and Juliet to find closest similar words in order to encrypt input text, and then does a procedure with help of NLP and provides an encrypted result. 

<p float="left">
    <img src="https://github.com/eherra/stupidhack2022/blob/main/docs/images/meeting.jpeg" alt="meeting" width="49%" height="49%">
    <img src="https://github.com/eherra/stupidhack2022/blob/main/docs/images/homer.jpeg" alt="homerMeme" width="49%" height="49%">
</p>

### Example

Input:
<code>Hello, where is the food hidden?</code>

Encrypted:

Output:
<code>rich peppered seems strangers eats drums</code>

### Preview
<img src="https://github.com/eherra/stupidhack2022/blob/main/docs/images/info.png" alt="reviewPhoto">


### Application's known issues
- This cryptography approach not <i>really</i> secure. :)
- Bugs?
- Spaghetti code

### How to run the app

To run this project you will need Python.

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
