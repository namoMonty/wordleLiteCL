# **WordleLiteCL**

## **Overview**

**WorldeLiteCL** is a lightweight, heavily simplified clone of the very popular Worlde game It is a command-line implementation of the popular Wordle game with no real UI. The goal remains the same as the classic which is to guess a 5-letter word within 6 attempts, with hints provided after each guess:

* 🟩 **Green**: Correct letter in the correct position.  
* 🟨 **Yellow**: Correct letter but in the wrong position.  
* 🟥 **Red**: Incorrect letter.

The word selection is weighted using word frequency data to ensure that the random words chosen are words that are recognizable to the user and not just words that are technically a word but, nobody uses.

---

## **Features**

* **Interactive Gameplay**: Enjoy a Wordle-style experience directly in the terminal.  
* **Color Feedback**: Color-coded hints powered by `colorama`.  
* **Input Validation**: Rejects invalid guesses, ensuring only real words are used.  
* **Weighted Word Selection**: Chooses words based on their frequency for added difficulty.

---

## **Prerequisites**

* Python 3.6 or higher  
* Required libraries:  
  * `colorama` (for color-coded hints)  
  * `wordfreq` (for word frequency calculations)

Install these libraries using:

pip install colorama wordfreq

---

## **Installation**

1. **Clone the repository:**

   	git clone https://github.com/yourusername/WordleLiteCL.git cd WordleLiteCL

2. **Ensure the `valid-wordle-words.txt` file is in the same directory as the script.**  
3. **Run the game:**
---

## **How to Play**

1. Start the game and guess the secret 5-letter word.  
2. Enter valid words only. Invalid words will be rejected.  
3. Follow the color-coded hints to adjust your guesses:  
   * 🟩 Green for correct letter and position.  
   * 🟨 Yellow for correct letter but wrong position.  
   * 🟥 Red for incorrect letters.  
4. Guess the word within 6 attempts to win\!

---

## **License**

This project is licensed under the [MIT License](https://chatgpt.com/c/LICENSE).

---

## **Acknowledgments**

* Inspired by the original Wordle game by Josh Wardle.  
* Word frequency data provided by the `wordfreq` library.  
* The wordlist used in this project was sourced from [Dracos's GitHub Gist](https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93). Special thanks for sharing this resource.

Enjoy the challenge and have fun playing **CLI-Wordler**\! 🟩🟨🟥

