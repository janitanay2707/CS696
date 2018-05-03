class Node:
    def __init__(self, word):
        self.word = word
        self.children = []
    def __str__(self):
        return "word is {}, there are {} children".format(self.word, len(self.children))

if __name__ == '__main__':

    beatles = """She says she loves you
       And you know that cant be bad
       Yes she loves you
       And you know you should be glad
       """
    # In this following example of list comprehension, we process the text above into a list.
    # The "if word" check at the end, will return false if word is an empty string
    word_list = [word.lower().replace('\n', '') for word in beatles.split(' ') if word]

    #previously node_dict was a class/static varible, here it is part of our main method
    node_dict = {}

    prev_word = None
    for word in word_list:
        if word not in node_dict:
            node_dict[word] = Node(word)
        if prev_word:
            node_dict[prev_word].children.append(word)
        prev_word = word

    # for k,v in node_dict.items():
    #     print(k,v)
