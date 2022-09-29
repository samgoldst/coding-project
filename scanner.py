import token_type


class Scanner:
    def __init__(self, filename):
        with open(filename) as source:
            self.lines = source.read().split('\n')
            for i in range(len(self.lines)):
                self.lines[i] += "\n"
            self.line_index = 0
            self.char_index = 0

    def s_0(self):  # starting state
        char = self.get_char()
        if char == " ":
            return self.s_0()
        elif char == "\n":
            return token_type.TokenType.EOL, char
        elif char == "a":
            return self.s_1(char)
        elif char == "r":
            return self.s_4(char)

    def s_1(self, word):  # a
        char = self.get_char()
        if char == "d":
            return self.s_2(word + char)

    def s_2(self, word):  # ad
        char = self.get_char()
        if char == "d":
            return self.s_3(word + char)

    def s_3(self, word):  # add
        return token_type.TokenType.ADD, word

    def s_4(self, word):
        char = self.get_char()
        if char != " " and char != "\n":
            return self.s_4(word + char)
        if char == "\n":
            self.char_index -= 1

        return token_type.TokenType.REG, word

    def get_char(self):
        char = self.lines[self.line_index][self.char_index]
        self.char_index += 1
        if self.char_index >= len(self.lines[self.line_index]):
            self.char_index = 0
            self.line_index += 1
        return char
