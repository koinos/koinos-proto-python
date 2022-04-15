# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/chain/authority.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/chain/authority.proto',
  package='koinos.chain',
  syntax='proto3',
  serialized_options=b'Z2github.com/koinos/koinos-proto-golang/koinos/chain',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ckoinos/chain/authority.proto\x12\x0ckoinos.chain\x1a\x14koinos/options.proto\"=\n\x0b\x63\x61ll_target\x12\x19\n\x0b\x63ontract_id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x13\n\x0b\x65ntry_point\x18\x02 \x01(\r\"|\n\x13\x61uthorize_arguments\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .koinos.chain.authorization_type\x12,\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x19.koinos.chain.call_targetH\x00\x88\x01\x01\x42\x07\n\x05_call\"!\n\x10\x61uthorize_result\x12\r\n\x05value\x18\x01 \x01(\x08*Y\n\x12\x61uthorization_type\x12\x11\n\rcontract_call\x10\x00\x12\x1b\n\x17transaction_application\x10\x01\x12\x13\n\x0f\x63ontract_upload\x10\x02\x42\x34Z2github.com/koinos/koinos-proto-golang/koinos/chainb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,])

_AUTHORIZATION_TYPE = _descriptor.EnumDescriptor(
  name='authorization_type',
  full_name='koinos.chain.authorization_type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='contract_call', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='transaction_application', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='contract_upload', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=292,
  serialized_end=381,
)
_sym_db.RegisterEnumDescriptor(_AUTHORIZATION_TYPE)

authorization_type = enum_type_wrapper.EnumTypeWrapper(_AUTHORIZATION_TYPE)
contract_call = 0
transaction_application = 1
contract_upload = 2



_CALL_TARGET = _descriptor.Descriptor(
  name='call_target',
  full_name='koinos.chain.call_target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='koinos.chain.call_target.contract_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entry_point', full_name='koinos.chain.call_target.entry_point', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=68,
  serialized_end=129,
)


_AUTHORIZE_ARGUMENTS = _descriptor.Descriptor(
  name='authorize_arguments',
  full_name='koinos.chain.authorize_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='koinos.chain.authorize_arguments.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call', full_name='koinos.chain.authorize_arguments.call', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='_call', full_name='koinos.chain.authorize_arguments._call',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=131,
  serialized_end=255,
)


_AUTHORIZE_RESULT = _descriptor.Descriptor(
  name='authorize_result',
  full_name='koinos.chain.authorize_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.chain.authorize_result.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=257,
  serialized_end=290,
)

_AUTHORIZE_ARGUMENTS.fields_by_name['type'].enum_type = _AUTHORIZATION_TYPE
_AUTHORIZE_ARGUMENTS.fields_by_name['call'].message_type = _CALL_TARGET
_AUTHORIZE_ARGUMENTS.oneofs_by_name['_call'].fields.append(
  _AUTHORIZE_ARGUMENTS.fields_by_name['call'])
_AUTHORIZE_ARGUMENTS.fields_by_name['call'].containing_oneof = _AUTHORIZE_ARGUMENTS.oneofs_by_name['_call']
DESCRIPTOR.message_types_by_name['call_target'] = _CALL_TARGET
DESCRIPTOR.message_types_by_name['authorize_arguments'] = _AUTHORIZE_ARGUMENTS
DESCRIPTOR.message_types_by_name['authorize_result'] = _AUTHORIZE_RESULT
DESCRIPTOR.enum_types_by_name['authorization_type'] = _AUTHORIZATION_TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

call_target = _reflection.GeneratedProtocolMessageType('call_target', (_message.Message,), {
  'DESCRIPTOR' : _CALL_TARGET,
  '__module__' : 'koinos.chain.authority_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.call_target)
  })
_sym_db.RegisterMessage(call_target)

authorize_arguments = _reflection.GeneratedProtocolMessageType('authorize_arguments', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZE_ARGUMENTS,
  '__module__' : 'koinos.chain.authority_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.authorize_arguments)
  })
_sym_db.RegisterMessage(authorize_arguments)

authorize_result = _reflection.GeneratedProtocolMessageType('authorize_result', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZE_RESULT,
  '__module__' : 'koinos.chain.authority_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.authorize_result)
  })
_sym_db.RegisterMessage(authorize_result)


DESCRIPTOR._options = None
_CALL_TARGET.fields_by_name['contract_id']._options = None
# @@protoc_insertion_point(module_scope)
