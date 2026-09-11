from components.elements.base_element import BaseElement

class Image(BaseElement):
    class Link(BaseElement):
        @property
        def type_of(self) -> str:
            return 'image'