# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/contracts/name_service/name_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/contracts/name_service/name_service.proto',
  package='koinos.contracts.name_service',
  syntax='proto3',
  serialized_options=b'ZCgithub.com/koinos/koinos-proto-golang/koinos/contracts/name-service',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0koinos/contracts/name_service/name_service.proto\x12\x1dkoinos.contracts.name_service\x1a\x14koinos/options.proto\"\x1b\n\x0bname_record\x12\x0c\n\x04name\x18\x01 \x01(\t\"\'\n\x0e\x61\x64\x64ress_record\x12\x15\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\"%\n\x15get_address_arguments\x12\x0c\n\x04name\x18\x01 \x01(\t\"R\n\x12get_address_result\x12<\n\x05value\x18\x01 \x01(\x0b\x32-.koinos.contracts.name_service.address_record\"+\n\x12get_name_arguments\x12\x15\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\"L\n\x0fget_name_result\x12\x39\n\x05value\x18\x01 \x01(\x0b\x32*.koinos.contracts.name_service.name_record\";\n\x14set_record_arguments\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x42\x04\x80\xb5\x18\x06\"\x13\n\x11set_record_result\":\n\x13record_update_event\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x42\x45ZCgithub.com/koinos/koinos-proto-golang/koinos/contracts/name-serviceb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,])




_NAME_RECORD = _descriptor.Descriptor(
  name='name_record',
  full_name='koinos.contracts.name_service.name_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='koinos.contracts.name_service.name_record.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=105,
  serialized_end=132,
)


_ADDRESS_RECORD = _descriptor.Descriptor(
  name='address_record',
  full_name='koinos.contracts.name_service.address_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='koinos.contracts.name_service.address_record.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=134,
  serialized_end=173,
)


_GET_ADDRESS_ARGUMENTS = _descriptor.Descriptor(
  name='get_address_arguments',
  full_name='koinos.contracts.name_service.get_address_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='koinos.contracts.name_service.get_address_arguments.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=175,
  serialized_end=212,
)


_GET_ADDRESS_RESULT = _descriptor.Descriptor(
  name='get_address_result',
  full_name='koinos.contracts.name_service.get_address_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.name_service.get_address_result.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=214,
  serialized_end=296,
)


_GET_NAME_ARGUMENTS = _descriptor.Descriptor(
  name='get_name_arguments',
  full_name='koinos.contracts.name_service.get_name_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='koinos.contracts.name_service.get_name_arguments.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=298,
  serialized_end=341,
)


_GET_NAME_RESULT = _descriptor.Descriptor(
  name='get_name_result',
  full_name='koinos.contracts.name_service.get_name_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.name_service.get_name_result.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=343,
  serialized_end=419,
)


_SET_RECORD_ARGUMENTS = _descriptor.Descriptor(
  name='set_record_arguments',
  full_name='koinos.contracts.name_service.set_record_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='koinos.contracts.name_service.set_record_arguments.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='koinos.contracts.name_service.set_record_arguments.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=421,
  serialized_end=480,
)


_SET_RECORD_RESULT = _descriptor.Descriptor(
  name='set_record_result',
  full_name='koinos.contracts.name_service.set_record_result',
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
  serialized_start=482,
  serialized_end=501,
)


_RECORD_UPDATE_EVENT = _descriptor.Descriptor(
  name='record_update_event',
  full_name='koinos.contracts.name_service.record_update_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='koinos.contracts.name_service.record_update_event.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='koinos.contracts.name_service.record_update_event.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=503,
  serialized_end=561,
)

_GET_ADDRESS_RESULT.fields_by_name['value'].message_type = _ADDRESS_RECORD
_GET_NAME_RESULT.fields_by_name['value'].message_type = _NAME_RECORD
DESCRIPTOR.message_types_by_name['name_record'] = _NAME_RECORD
DESCRIPTOR.message_types_by_name['address_record'] = _ADDRESS_RECORD
DESCRIPTOR.message_types_by_name['get_address_arguments'] = _GET_ADDRESS_ARGUMENTS
DESCRIPTOR.message_types_by_name['get_address_result'] = _GET_ADDRESS_RESULT
DESCRIPTOR.message_types_by_name['get_name_arguments'] = _GET_NAME_ARGUMENTS
DESCRIPTOR.message_types_by_name['get_name_result'] = _GET_NAME_RESULT
DESCRIPTOR.message_types_by_name['set_record_arguments'] = _SET_RECORD_ARGUMENTS
DESCRIPTOR.message_types_by_name['set_record_result'] = _SET_RECORD_RESULT
DESCRIPTOR.message_types_by_name['record_update_event'] = _RECORD_UPDATE_EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

name_record = _reflection.GeneratedProtocolMessageType('name_record', (_message.Message,), {
  'DESCRIPTOR' : _NAME_RECORD,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.name_record)
  })
_sym_db.RegisterMessage(name_record)

address_record = _reflection.GeneratedProtocolMessageType('address_record', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS_RECORD,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.address_record)
  })
_sym_db.RegisterMessage(address_record)

get_address_arguments = _reflection.GeneratedProtocolMessageType('get_address_arguments', (_message.Message,), {
  'DESCRIPTOR' : _GET_ADDRESS_ARGUMENTS,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.get_address_arguments)
  })
_sym_db.RegisterMessage(get_address_arguments)

get_address_result = _reflection.GeneratedProtocolMessageType('get_address_result', (_message.Message,), {
  'DESCRIPTOR' : _GET_ADDRESS_RESULT,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.get_address_result)
  })
_sym_db.RegisterMessage(get_address_result)

get_name_arguments = _reflection.GeneratedProtocolMessageType('get_name_arguments', (_message.Message,), {
  'DESCRIPTOR' : _GET_NAME_ARGUMENTS,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.get_name_arguments)
  })
_sym_db.RegisterMessage(get_name_arguments)

get_name_result = _reflection.GeneratedProtocolMessageType('get_name_result', (_message.Message,), {
  'DESCRIPTOR' : _GET_NAME_RESULT,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.get_name_result)
  })
_sym_db.RegisterMessage(get_name_result)

set_record_arguments = _reflection.GeneratedProtocolMessageType('set_record_arguments', (_message.Message,), {
  'DESCRIPTOR' : _SET_RECORD_ARGUMENTS,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.set_record_arguments)
  })
_sym_db.RegisterMessage(set_record_arguments)

set_record_result = _reflection.GeneratedProtocolMessageType('set_record_result', (_message.Message,), {
  'DESCRIPTOR' : _SET_RECORD_RESULT,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.set_record_result)
  })
_sym_db.RegisterMessage(set_record_result)

record_update_event = _reflection.GeneratedProtocolMessageType('record_update_event', (_message.Message,), {
  'DESCRIPTOR' : _RECORD_UPDATE_EVENT,
  '__module__' : 'koinos.contracts.name_service.name_service_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.name_service.record_update_event)
  })
_sym_db.RegisterMessage(record_update_event)


DESCRIPTOR._options = None
_ADDRESS_RECORD.fields_by_name['address']._options = None
_GET_NAME_ARGUMENTS.fields_by_name['address']._options = None
_SET_RECORD_ARGUMENTS.fields_by_name['address']._options = None
_RECORD_UPDATE_EVENT.fields_by_name['address']._options = None
# @@protoc_insertion_point(module_scope)
