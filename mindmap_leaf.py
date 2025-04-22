from tkinter.font import names

class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}((",
        }
        return shapes.get(self.shape, '{}')

    def display(self, indent=0):
        print(' ' * indent + str(self))

    def __str__(self):
        return self.get_shape_representation().format(self.name)


# Step 4: Write the get_shape_representation method
# - Create a shapes dictionary with shape templates.
# - Use shapes.get to return the appropriate shape template.