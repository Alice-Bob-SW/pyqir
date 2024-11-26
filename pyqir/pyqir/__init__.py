# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pyqir._native import (
    ArrayType,
    Attribute,
    AttributeList,
    AttributeSet,
    BasicBlock,
    Builder,
    Call,
    Constant,
    ConstantAsMetadata,
    Context,
    FCmp,
    FloatConstant,
    FloatPredicate,
    Function,
    FunctionType,
    ICmp,
    Instruction,
    IntConstant,
    IntPredicate,
    IntType,
    Linkage,
    Metadata,
    MetadataString,
    Module,
    ModuleFlagBehavior,
    Opcode,
    Phi,
    PointerType,
    StructType,
    Switch,
    Type,
    Value,
    add_string_attribute,
    const,
    dynamic_qubit_management,
    dynamic_result_management,
    extract_byte_string,
    global_byte_string,
    is_entry_point,
    is_interop_friendly,
    is_qubit_type,
    is_result_type,
    max_qubit_index,
    max_result_index,
    qubit,
    qubit_id,
    qubit_type,
    qir_major_version,
    qir_minor_version,
    qir_module,
    required_num_qubits,
    required_num_results,
    result,
    result_id,
    result_type,
)
from pyqir._simple import SimpleModule
from pyqir._entry_point import entry_point
from pyqir._basicqis import BasicQisBuilder
from pyqir._constants import ATTR_FUNCTION_INDEX, ATTR_RETURN_INDEX

__all__ = [
    "ArrayType",
    "Attribute",
    "AttributeList",
    "AttributeSet",
    "BasicBlock",
    "BasicQisBuilder",
    "Builder",
    "Call",
    "Constant",
    "ConstantAsMetadata",
    "Context",
    "FCmp",
    "FloatConstant",
    "FloatPredicate",
    "Function",
    "FunctionType",
    "ICmp",
    "Instruction",
    "IntConstant",
    "IntPredicate",
    "IntType",
    "Linkage",
    "Metadata",
    "MetadataString",
    "Module",
    "ModuleFlagBehavior",
    "Opcode",
    "Phi",
    "PointerType",
    "SimpleModule",
    "StructType",
    "Switch",
    "Type",
    "Value",
    "add_string_attribute",
    "const",
    "dynamic_qubit_management",
    "dynamic_result_management",
    "entry_point",
    "extract_byte_string",
    "global_byte_string",
    "is_entry_point",
    "is_interop_friendly",
    "is_qubit_type",
    "is_result_type",
    "max_qubit_index",
    "max_result_index",
    "qubit_id",
    "qubit_type",
    "qubit",
    "qir_major_version",
    "qir_minor_version",
    "qir_module",
    "required_num_qubits",
    "required_num_results",
    "result_id",
    "result_type",
    "result",
    "ATTR_FUNCTION_INDEX",
    "ATTR_RETURN_INDEX",
]
