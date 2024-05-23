from dataclasses import dataclass, field


class Parent:
    parent_name = 'alibaba'

@dataclass
class My_data(Parent):
    name: str
    age: int
    likes: list = field(default_factory=list)
    
my = My_data('DARREN', 11, [1,2])