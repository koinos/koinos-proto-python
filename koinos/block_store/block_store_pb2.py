# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/block_store/block_store.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2
from koinos.protocol import protocol_pb2 as koinos_dot_protocol_dot_protocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/block_store/block_store.proto',
  package='koinos.block_store',
  syntax='proto3',
  serialized_options=b'Z?github.com/koinos/koinos-proto-golang/v2/koinos/rpc/block_store',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$koinos/block_store/block_store.proto\x12\x12koinos.block_store\x1a\x14koinos/options.proto\x1a\x1ekoinos/protocol/protocol.proto\"\x96\x01\n\nblock_item\x12\x16\n\x08\x62lock_id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x03\x12\x18\n\x0c\x62lock_height\x18\x02 \x01(\x04\x42\x02\x30\x01\x12%\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x16.koinos.protocol.block\x12/\n\x07receipt\x18\x04 \x01(\x0b\x32\x1e.koinos.protocol.block_receipt\"\xba\x01\n\x0c\x62lock_record\x12\x16\n\x08\x62lock_id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x03\x12\x18\n\x0c\x62lock_height\x18\x02 \x01(\x04\x42\x02\x30\x01\x12%\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x16.koinos.protocol.block\x12/\n\x07receipt\x18\x04 \x01(\x0b\x32\x1e.koinos.protocol.block_receipt\x12 \n\x12previous_block_ids\x18\x05 \x03(\x0c\x42\x04\x80\xb5\x18\x03\x42\x41Z?github.com/koinos/koinos-proto-golang/v2/koinos/rpc/block_storeb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,koinos_dot_protocol_dot_protocol__pb2.DESCRIPTOR,])




_BLOCK_ITEM = _descriptor.Descriptor(
  name='block_item',
  full_name='koinos.block_store.block_item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.block_store.block_item.block_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='koinos.block_store.block_item.block_height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block', full_name='koinos.block_store.block_item.block', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='koinos.block_store.block_item.receipt', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=115,
  serialized_end=265,
)


_BLOCK_RECORD = _descriptor.Descriptor(
  name='block_record',
  full_name='koinos.block_store.block_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.block_store.block_record.block_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='koinos.block_store.block_record.block_height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block', full_name='koinos.block_store.block_record.block', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='koinos.block_store.block_record.receipt', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_block_ids', full_name='koinos.block_store.block_record.previous_block_ids', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=454,
)

_BLOCK_ITEM.fields_by_name['block'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK
_BLOCK_ITEM.fields_by_name['receipt'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK_RECEIPT
_BLOCK_RECORD.fields_by_name['block'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK
_BLOCK_RECORD.fields_by_name['receipt'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK_RECEIPT
DESCRIPTOR.message_types_by_name['block_item'] = _BLOCK_ITEM
DESCRIPTOR.message_types_by_name['block_record'] = _BLOCK_RECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

block_item = _reflection.GeneratedProtocolMessageType('block_item', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK_ITEM,
  '__module__' : 'koinos.block_store.block_store_pb2'
  # @@protoc_insertion_point(class_scope:koinos.block_store.block_item)
  })
_sym_db.RegisterMessage(block_item)

block_record = _reflection.GeneratedProtocolMessageType('block_record', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK_RECORD,
  '__module__' : 'koinos.block_store.block_store_pb2'
  # @@protoc_insertion_point(class_scope:koinos.block_store.block_record)
  })
_sym_db.RegisterMessage(block_record)


DESCRIPTOR._options = None
_BLOCK_ITEM.fields_by_name['block_id']._options = None
_BLOCK_ITEM.fields_by_name['block_height']._options = None
_BLOCK_RECORD.fields_by_name['block_id']._options = None
_BLOCK_RECORD.fields_by_name['block_height']._options = None
_BLOCK_RECORD.fields_by_name['previous_block_ids']._options = None
# @@protoc_insertion_point(module_scope)
