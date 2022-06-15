import ast as python_ast
from typing import Any, Optional, Sequence, Type, Union

from .natspec import parse_natspec as parse_natspec
from .utils import ast_to_dict as ast_to_dict
from .utils import parse_to_ast as parse_to_ast

NODE_BASE_ATTRIBUTES: Any
NODE_SRC_ATTRIBUTES: Any
DICT_AST_SKIPLIST: Any

def get_node(
    ast_struct: Union[dict, python_ast.AST], parent: Optional[VyperNode] = ...
) -> VyperNode: ...
def compare_nodes(left_node: VyperNode, right_node: VyperNode) -> bool: ...

class VyperNode:
    full_source_code: str = ...
    node_source_code: str = ...
    _metadata: dict = ...
    def __init__(self, parent: Optional[VyperNode] = ..., **kwargs: Any) -> None: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    @property
    def description(self): ...
    @classmethod
    def get_fields(cls: Any) -> set: ...
    def evaluate(self) -> VyperNode: ...
    @classmethod
    def from_node(cls, node: VyperNode, **kwargs: Any) -> Any: ...
    def to_dict(self) -> dict: ...
    def get_children(
        self,
        node_type: Union[Type[VyperNode], Sequence[Type[VyperNode]], None] = ...,
        filters: Optional[dict] = ...,
        reverse: bool = ...,
    ) -> Sequence: ...
    def get_descendants(
        self,
        node_type: Union[Type[VyperNode], Sequence[Type[VyperNode]], None] = ...,
        filters: Optional[dict] = ...,
        include_self: bool = ...,
        reverse: bool = ...,
    ) -> Sequence: ...
    def get_ancestor(
        self, node_type: Union[Type[VyperNode], Sequence[Type[VyperNode]], None] = ...
    ) -> VyperNode: ...
    def get(self, field_str: str) -> Any: ...

class TopLevel(VyperNode):
    doc_string: Str = ...
    body: list = ...
    name: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __contains__(self, obj: Any) -> bool: ...

class Module(TopLevel):
    def replace_in_tree(self, old_node: VyperNode, new_node: VyperNode) -> None: ...
    def add_to_body(self, node: VyperNode) -> None: ...
    def remove_from_body(self, node: VyperNode) -> None: ...

class FunctionDef(TopLevel):
    args: arguments = ...
    decorator_list: list = ...
    returns: VyperNode = ...

class arguments(VyperNode):
    args: list = ...
    defaults: list = ...

class arg(VyperNode): ...
class Return(VyperNode): ...

class Log(VyperNode):
    value: VyperNode = ...

class EnumDef(VyperNode):
    body: list = ...
    name: str = ...

class EventDef(VyperNode):
    body: list = ...
    name: str = ...

class InterfaceDef(VyperNode):
    body: list = ...
    name: str = ...

class StructDef(VyperNode):
    body: list = ...
    name: str = ...

class Constant(VyperNode):
    value: Any = ...

class Num(Constant):
    @property
    def n(self): ...

class Int(Num):
    value: int = ...

class Decimal(Num): ...
class Hex(Num): ...

class Str(Constant):
    @property
    def s(self): ...

class Bytes(Constant):
    @property
    def s(self): ...

class List(VyperNode):
    elements: list = ...

class Tuple(VyperNode):
    elements: list = ...

class Dict(VyperNode):
    keys: list = ...
    values: list = ...

class NameConstant(Constant): ...

class Name(VyperNode):
    id: str = ...
    _type: str = ...

class Expr(VyperNode):
    value: VyperNode = ...

class UnaryOp(VyperNode):
    op: VyperNode = ...

class USub(VyperNode): ...
class Not(VyperNode): ...

class BinOp(VyperNode):
    left: VyperNode = ...
    op: VyperNode = ...
    right: VyperNode = ...

class Add(VyperNode): ...
class Sub(VyperNode): ...
class Mult(VyperNode): ...
class Div(VyperNode): ...
class Mod(VyperNode): ...
class Pow(VyperNode): ...
class BoolOp(VyperNode): ...
class And(VyperNode): ...
class Or(VyperNode): ...

class Compare(VyperNode):
    op: VyperNode = ...

class Eq(VyperNode): ...
class NotEq(VyperNode): ...
class Lt(VyperNode): ...
class LtE(VyperNode): ...
class Gt(VyperNode): ...
class GtE(VyperNode): ...
class In(VyperNode): ...

class Call(VyperNode):
    args: list = ...
    keywords: list = ...
    func: Name = ...

class keyword(VyperNode): ...

class Attribute(VyperNode):
    attr: str = ...
    value: VyperNode = ...

class Subscript(VyperNode):
    slice: Index = ...
    value: VyperNode = ...

class Index(VyperNode):
    value: Constant = ...

class Assign(VyperNode): ...

class AnnAssign(VyperNode):
    target: Name = ...
    value: VyperNode = ...
    annotation: VyperNode = ...

class AugAssign(VyperNode):
    op: VyperNode = ...
    target: VyperNode = ...
    value: VyperNode = ...

class Raise(VyperNode): ...
class Assert(VyperNode): ...
class Pass(VyperNode): ...

class Import(VyperNode):
    alias: str = ...
    name: str = ...

class ImportFrom(VyperNode):
    alias: str = ...
    level: int = ...
    module: str = ...
    name: str = ...

class If(VyperNode):
    body: list = ...
    orelse: list = ...

class For(VyperNode): ...
class Break(VyperNode): ...
class Continue(VyperNode): ...
