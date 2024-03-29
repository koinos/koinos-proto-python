# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/common.proto',
  package='koinos',
  syntax='proto3',
  serialized_options=b'Z/github.com/koinos/koinos-proto-golang/v2/koinos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13koinos/common.proto\x12\x06koinos\x1a\x14koinos/options.proto\"N\n\x0e\x62lock_topology\x12\x10\n\x02id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x03\x12\x12\n\x06height\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x16\n\x08previous\x18\x03 \x01(\x0c\x42\x04\x80\xb5\x18\x03\x42\x31Z/github.com/koinos/koinos-proto-golang/v2/koinosb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,])




_BLOCK_TOPOLOGY = _descriptor.Descriptor(
  name='block_topology',
  full_name='koinos.block_topology',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='koinos.block_topology.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='koinos.block_topology.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous', full_name='koinos.block_topology.previous', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['block_topology'] = _BLOCK_TOPOLOGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

block_topology = _reflection.GeneratedProtocolMessageType('block_topology', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK_TOPOLOGY,
  '__module__' : 'koinos.common_pb2'
  # @@protoc_insertion_point(class_scope:koinos.block_topology)
  })
_sym_db.RegisterMessage(block_topology)


DESCRIPTOR._options = None
_BLOCK_TOPOLOGY.fields_by_name['id']._options = None
_BLOCK_TOPOLOGY.fields_by_name['height']._options = None
_BLOCK_TOPOLOGY.fields_by_name['previous']._options = None
# @@protoc_insertion_point(module_scope)
