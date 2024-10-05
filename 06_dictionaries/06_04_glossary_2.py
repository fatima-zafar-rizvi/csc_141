# Adding to the glossary dictionary with more Python terms and their meanings:
glossary = {
    'variable': 'Refers to a value in a program.',
    'loop': 'Structure that repeats a block of code.',
    'list': 'Collection of items, which can be different.',
    'dictionary': 'Collection of key-value pairs. Each key is unique.',
    'function': 'Block of code that performs a specific task.',
    'integer': 'A whole number, positive or negative, without fractions or'
    ' decimals.',
    'boolean expression': 'An expression that evaluates to either True or'
    ' False.',
    'output': 'The data produced by a program or function after processing'
    ' input.',
    'constant': 'A value that cannot be altered when the program is being'
    ' executed.',
    'debugger': 'A tool used to test and debug code by stepping through it'
    ' and inspecting variables.'
}

# Loop through the glossary dictionary and print each term and its meaning:
for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")