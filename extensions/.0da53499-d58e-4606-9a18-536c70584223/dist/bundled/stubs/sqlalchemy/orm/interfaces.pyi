from typing import Any, Optional
from .. import util
from ..sql import operators
from .base import (
    ONETOMANY as ONETOMANY,
    MANYTOONE as MANYTOONE,
    MANYTOMANY as MANYTOMANY,
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_STOP as EXT_STOP,
    NOT_EXTENSION as NOT_EXTENSION,
    InspectionAttrInfo as InspectionAttrInfo
)
from .base import InspectionAttr as InspectionAttr, _MappedAttribute as _MappedAttribute

MapperExtension: Any = ...
SessionExtension: Any = ...
AttributeExtension: Any = ...

class MapperProperty(_MappedAttribute, InspectionAttr, util.MemoizedSlots):
    cascade: Any = ...
    is_property: bool = ...
    def setup(self, context, entity, path, adapter, **kwargs): ...
    def create_row_processor(self, context, path, mapper, result, adapter, populators): ...
    def cascade_iterator(self, type_, state, visited_instances: Optional[Any] = ...,
                         halt_on: Optional[Any] = ...): ...
    parent: Any = ...
    def set_parent(self, parent, init): ...
    def instrument_class(self, mapper): ...
    def __init__(self) -> None: ...
    def init(self): ...
    @property
    def class_attribute(self): ...
    def do_init(self): ...
    def post_instrument_class(self, mapper): ...
    def merge(self, session, source_state, source_dict, dest_state, dest_dict, load,
              _recursive, _resolve_conflict_map): ...

class PropComparator(operators.ColumnOperators):
    prop: Any = ...
    def __init__(self, prop, parentmapper, adapt_to_entity: Optional[Any] = ...) -> None: ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity): ...
    @property
    def adapter(self): ...
    @property
    def info(self): ...
    @staticmethod
    def any_op(a, b, **kwargs): ...
    @staticmethod
    def has_op(a, b, **kwargs): ...
    @staticmethod
    def of_type_op(a, class_): ...
    def of_type(self, class_): ...
    def any(self, criterion: Optional[Any] = ..., **kwargs): ...
    def has(self, criterion: Optional[Any] = ..., **kwargs): ...

class StrategizedProperty(MapperProperty):
    strategy_wildcard_key: Any = ...
    def setup(self, context, entity, path, adapter, **kwargs): ...
    def create_row_processor(self, context, path, mapper, result, adapter, populators): ...
    strategy: Any = ...
    def do_init(self): ...
    def post_instrument_class(self, mapper): ...
    @classmethod
    def strategy_for(cls, **kw): ...

class MapperOption(object):
    propagate_to_loaders: bool = ...
    def process_query(self, query): ...
    def process_query_conditionally(self, query): ...

class LoaderStrategy(object):
    parent_property: Any = ...
    is_class_level: bool = ...
    parent: Any = ...
    key: Any = ...
    strategy_key: Any = ...
    strategy_opts: Any = ...
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper): ...
    def setup_query(self, context, entity, path, loadopt, adapter, **kwargs): ...
    def create_row_processor(self, context, path, loadopt, mapper, result, adapter, populators): ...
