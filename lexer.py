# Modifying the lexer to include new token types: MUL, DIV, LPAREN, and RPAREN
lexer_code_updated = lexer_code.replace(
    'EOF = "EOF"  # Означає кінець вхідного рядка',
    'EOF = "EOF"  # Означає кінець вхідного рядка\n    MUL = "MUL"\n    DIV = "DIV"\n    LPAREN = "LPAREN"\n    RPAREN = "RPAREN"',
)

# Finding the location to insert the logic for recognizing new tokens in the Lexer class
lexer_class_start = lexer_code_updated.find("class Lexer:")
lexer_get_next_token_start = lexer_code_updated.find(
    "def get_next_token", lexer_class_start
)

# Now, I'll modify the get_next_token method to recognize the new tokens
insertion_point = lexer_code_updated.find(
    "else:", lexer_get_next_token_start
)  # finding the insertion point

# Preparing the code snippet to recognize '*', '/', '(', and ')'
new_token_logic = """
        elif self.current_char == '*':
            self.advance()
            return Token(TokenType.MUL, '*')

        elif self.current_char == '/':
            self.advance()
            return Token(TokenType.DIV, '/')

        elif self.current_char == '(':
            self.advance()
            return Token(TokenType.LPAREN, '(')

        elif self.current_char == ')':
            self.advance()
            return Token(TokenType.RPAREN, ')')
"""

# Inserting the new logic
lexer_code_updated = (
    lexer_code_updated[:insertion_point]
    + new_token_logic
    + lexer_code_updated[insertion_point:]
)

# Showing a part of the updated code for review
lexer_code_updated[
    lexer_get_next_token_start : lexer_get_next_token_start + 1000
]  # Displaying a relevant portion of the updated code
