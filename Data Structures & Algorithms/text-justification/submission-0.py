class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        lines = []
        i = 0

        while i < len(words):
            # Step 1: greedily pick words for this line
            line_words = [words[i]]
            letters = len(words[i])
            i += 1
            while i < len(words) and letters + len(words[i]) + len(line_words) <= max_width:
                line_words.append(words[i])
                letters += len(words[i])
                i += 1

            # Step 2: build the line
            is_last_line = i == len(words)
            if is_last_line or len(line_words) == 1:
                lines.append(self.left_justify(line_words, max_width))
            else:
                lines.append(self.normal_justify(line_words, letters, max_width))

        return lines


    def left_justify(self, line_words: list[str], max_width: int) -> str:
        line = " ".join(line_words)
        return line + " " * (max_width - len(line))


    def normal_justify(self, line_words: list[str], letters: int, max_width: int) -> str:
        gaps = len(line_words) - 1
        base, extra = divmod(max_width - letters, gaps)

        parts = []
        for idx, word in enumerate(line_words[:-1]):
            spaces = base + (1 if idx < extra else 0)  # leftmost gaps get the extras
            parts.append(word + " " * spaces)
        parts.append(line_words[-1])
        return "".join(parts)