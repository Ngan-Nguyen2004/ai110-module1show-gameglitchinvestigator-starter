# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
If I renew the game midway, it will not refresh the history. Instead, it will add up the history and make it look like the game is going on forever.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1/ The game history was not refreshing when I renewed the game, causing it to accumulate indefinitely.
2/ The game don't have a correct number. Even if I input the number higher than allowed range (1 -100) like 139, it will show "go higher".
3/ The games does not have a clear answer. It says "go higher" when I put 99 but then "go lower" when I put 100. It is very confusing for the players.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used ChatGPT (Copilot-style guidance in this VS Code workflow).
- Correct suggestion: AI pointed out state reset and range validation. I then implemented:
+ if st.session_state.difficulty != difficulty: reset secret, attempts, score, history
+ is_guess_in_range to reject >100/ <1 guesses.
Verified with pytest -q (5 passed) and manual streamlit run.
Incorrect/misleading: first AI reply had a broken indentation block (if outcome == "Win": not indented), causing IndentationError; fixed by re-indenting and re-running tests.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I decided a bug was fixed when the behavior matched expected outcomes and all tests passed. For example, after implementing the state reset on new game, I ran pytest -q and got 5 passed, confirming the logic worked as intended. I also did manual testing by running streamlit and verifying that starting a new game cleared the history and reset attempts/score. AI helped me understand the importance of state management in Streamlit and suggested specific code changes to implement it, which guided my testing focus on those areas.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- I would say Streamlit reruns the whole page every time you click or type something, like refreshing the whole screen from scratch. To keep track of things across those refreshes, you use session state, which is like a special storage that remembers values (like score, attempts) even when the page reloads. So instead of losing all your data every time, you can save it in session state and it will be there when the page reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I want to reuse the habit of writing clear, specific prompts for AI and then verifying the suggestions with both automated tests and manual testing. This helps ensure that the AI's code changes actually work as intended.
- Next time, I would be more cautious about accepting AI suggestions without first checking for syntax errors.