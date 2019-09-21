# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import os

# https://regex101.com/r/ezekzs/1
regex = r"\n\n( {4}[\w\S]+[\w\S ]*((\n {4}([\w \S]*))|(\n {4})){0,})\n"

# TODO this regex will fail if the ``` is not preceded by a newline
py_regex = r"```python\n((^(?!```).+\n)|([\n ]+)){1,}```"


if __name__ == "__main__":
    # requires nbconvert
    os.system('jupyter nbconvert --to MARKDOWN README.ipynb')

    with open('README.md', 'r+') as f:
        all_text = f.read()

        matches = re.finditer(regex, all_text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            temp = "\n\n\n<details><summary>Python Print-out</summary>\n\n\n```text\n{}\n```\n\n\n</details>\n\n".format(
                match.group(1))
            all_text = all_text.replace(match.group(0), temp)

        matches = re.finditer(py_regex, all_text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            temp = "\n\n\n<details><summary>Python Code Sample</summary>\n\n\n{}\n\n\n</details>\n\n".format(
                match.group(0))
            all_text = all_text.replace(match.group(0), temp)

        f.seek(0)
        f.write(all_text)
        f.truncate()