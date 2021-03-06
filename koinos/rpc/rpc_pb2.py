# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/rpc/rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/rpc/rpc.proto',
  package='koinos.rpc',
  syntax='proto3',
  serialized_options=b'Z0github.com/koinos/koinos-proto-golang/koinos/rpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14koinos/rpc/rpc.proto\x12\nkoinos.rpc\"\x0e\n\x0creserved_rpc\"/\n\x0e\x65rror_response\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\tB2Z0github.com/koinos/koinos-proto-golang/koinos/rpcb\x06proto3'
)




_RESERVED_RPC = _descriptor.Descriptor(
  name='reserved_rpc',
  full_name='koinos.rpc.reserved_rpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=36,
  serialized_end=50,
)


_ERROR_RESPONSE = _descriptor.Descriptor(
  name='error_response',
  full_name='koinos.rpc.error_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='koinos.rpc.error_response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='koinos.rpc.error_response.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=52,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['reserved_rpc'] = _RESERVED_RPC
DESCRIPTOR.message_types_by_name['error_response'] = _ERROR_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

reserved_rpc = _reflection.GeneratedProtocolMessageType('reserved_rpc', (_message.Message,), {
  'DESCRIPTOR' : _RESERVED_RPC,
  '__module__' : 'koinos.rpc.rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.reserved_rpc)
  })
_sym_db.RegisterMessage(reserved_rpc)

error_response = _reflection.GeneratedProtocolMessageType('error_response', (_message.Message,), {
  'DESCRIPTOR' : _ERROR_RESPONSE,
  '__module__' : 'koinos.rpc.rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.error_response)
  })
_sym_db.RegisterMessage(error_response)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
