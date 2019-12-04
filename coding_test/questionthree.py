
class TextInput(object):
    """a.	Create a Base class called Text Input"""

    def  __init__(self):
        self.value = ''

    def add(self, xter):
        """b.
        Inside the TextInput class,
        create a method called “Add” that adds a character to a value property
        in the class"""
        self.value = f"""{self.value}{xter}"""

    def get_value(self):
        """c.
        Create another method
        that gets the total character that has been added to the Value property
        and prints it to the screen"""
        return self.value

class NumberInput(TextInput):
    """d.
    Create another Class called NumberInput, this should inherit from TextInput
    """

    def add(self, xter):
        """e.
        Override the “Add” method so that it removes number characters
        when it is been added with the add function."""
        self.value = f"""{self.value}{xter}"""
        self.value = "".join([x for x in list(self.value) if not x.isdigit()])
        input = NumberInput()
        input.add('a')
        input.add('b')
        input.add('c')
        input.add('1')
        input.add('0')

        print(input.get_value())