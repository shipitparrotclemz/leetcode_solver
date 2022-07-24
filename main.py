import os
import openai
from openai import Completion
from typing import List, Dict, Any

# vim ~/.bash_profile
# export OPENAI_SIP_KEY=''
from openai.openai_object import OpenAIObject

openai.api_key = os.getenv("OPENAI_SIP_KEY", "")

completion_object: Completion = Completion()

leetcode_question: str = """
9. Palindrome Number
Easy

6483

2226

Add to List

Share
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""

prompt: str = f"""
Give a Python Solution for the leetcode question below. Leave comments for exactly how the solution solves it step-wise.

Leetcode Question:
{leetcode_question}
Python Solution:
"""

response: OpenAIObject = completion_object.create(
  model="code-davinci-002",
  prompt=prompt,
  max_tokens=1000,
)
choices: List[Dict[str, Any]] = response["choices"]
first_choice: Dict[str, Any] = choices[0]
completion: str = first_choice["text"]

print(completion)