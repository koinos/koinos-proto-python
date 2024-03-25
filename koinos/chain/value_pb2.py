# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/chain/value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/chain/value.proto',
  package='koinos.chain',
  syntax='proto3',
  serialized_options=b'Z5github.com/koinos/koinos-proto-golang/v2/koinos/chain',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18koinos/chain/value.proto\x12\x0ckoinos.chain\x1a\x19google/protobuf/any.proto\"\x90\x03\n\nvalue_type\x12-\n\rmessage_value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x15\n\x0bint32_value\x18\x02 \x01(\x05H\x00\x12\x19\n\x0bint64_value\x18\x03 \x01(\x03\x42\x02\x30\x01H\x00\x12\x16\n\x0cuint32_value\x18\x04 \x01(\rH\x00\x12\x1a\n\x0cuint64_value\x18\x05 \x01(\x04\x42\x02\x30\x01H\x00\x12\x16\n\x0csint32_value\x18\x06 \x01(\x11H\x00\x12\x1a\n\x0csint64_value\x18\x07 \x01(\x12\x42\x02\x30\x01H\x00\x12\x17\n\rfixed32_value\x18\x08 \x01(\x07H\x00\x12\x1b\n\rfixed64_value\x18\t \x01(\x06\x42\x02\x30\x01H\x00\x12\x18\n\x0esfixed32_value\x18\n \x01(\x0fH\x00\x12\x1c\n\x0esfixed64_value\x18\x0b \x01(\x10\x42\x02\x30\x01H\x00\x12\x14\n\nbool_value\x18\x0c \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\r \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x0e \x01(\x0cH\x00\x42\x06\n\x04kind\")\n\tenum_type\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\"5\n\tlist_type\x12(\n\x06values\x18\x01 \x03(\x0b\x32\x18.koinos.chain.value_typeB7Z5github.com/koinos/koinos-proto-golang/v2/koinos/chainb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_VALUE_TYPE = _descriptor.Descriptor(
  name='value_type',
  full_name='koinos.chain.value_type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_value', full_name='koinos.chain.value_type.message_value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='koinos.chain.value_type.int32_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='koinos.chain.value_type.int64_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='koinos.chain.value_type.uint32_value', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='koinos.chain.value_type.uint64_value', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint32_value', full_name='koinos.chain.value_type.sint32_value', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint64_value', full_name='koinos.chain.value_type.sint64_value', index=6,
      number=7, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed32_value', full_name='koinos.chain.value_type.fixed32_value', index=7,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed64_value', full_name='koinos.chain.value_type.fixed64_value', index=8,
      number=9, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed32_value', full_name='koinos.chain.value_type.sfixed32_value', index=9,
      number=10, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed64_value', full_name='koinos.chain.value_type.sfixed64_value', index=10,
      number=11, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='koinos.chain.value_type.bool_value', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='koinos.chain.value_type.string_value', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='koinos.chain.value_type.bytes_value', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
      name='kind', full_name='koinos.chain.value_type.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=70,
  serialized_end=470,
)


_ENUM_TYPE = _descriptor.Descriptor(
  name='enum_type',
  full_name='koinos.chain.enum_type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='koinos.chain.enum_type.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='koinos.chain.enum_type.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=472,
  serialized_end=513,
)


_LIST_TYPE = _descriptor.Descriptor(
  name='list_type',
  full_name='koinos.chain.list_type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='koinos.chain.list_type.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=515,
  serialized_end=568,
)

_VALUE_TYPE.fields_by_name['message_value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['message_value'])
_VALUE_TYPE.fields_by_name['message_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['int32_value'])
_VALUE_TYPE.fields_by_name['int32_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['int64_value'])
_VALUE_TYPE.fields_by_name['int64_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['uint32_value'])
_VALUE_TYPE.fields_by_name['uint32_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['uint64_value'])
_VALUE_TYPE.fields_by_name['uint64_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['sint32_value'])
_VALUE_TYPE.fields_by_name['sint32_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['sint64_value'])
_VALUE_TYPE.fields_by_name['sint64_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['fixed32_value'])
_VALUE_TYPE.fields_by_name['fixed32_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['fixed64_value'])
_VALUE_TYPE.fields_by_name['fixed64_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['sfixed32_value'])
_VALUE_TYPE.fields_by_name['sfixed32_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['sfixed64_value'])
_VALUE_TYPE.fields_by_name['sfixed64_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['bool_value'])
_VALUE_TYPE.fields_by_name['bool_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['string_value'])
_VALUE_TYPE.fields_by_name['string_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_VALUE_TYPE.oneofs_by_name['kind'].fields.append(
  _VALUE_TYPE.fields_by_name['bytes_value'])
_VALUE_TYPE.fields_by_name['bytes_value'].containing_oneof = _VALUE_TYPE.oneofs_by_name['kind']
_LIST_TYPE.fields_by_name['values'].message_type = _VALUE_TYPE
DESCRIPTOR.message_types_by_name['value_type'] = _VALUE_TYPE
DESCRIPTOR.message_types_by_name['enum_type'] = _ENUM_TYPE
DESCRIPTOR.message_types_by_name['list_type'] = _LIST_TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

value_type = _reflection.GeneratedProtocolMessageType('value_type', (_message.Message,), {
  'DESCRIPTOR' : _VALUE_TYPE,
  '__module__' : 'koinos.chain.value_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.value_type)
  })
_sym_db.RegisterMessage(value_type)

enum_type = _reflection.GeneratedProtocolMessageType('enum_type', (_message.Message,), {
  'DESCRIPTOR' : _ENUM_TYPE,
  '__module__' : 'koinos.chain.value_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.enum_type)
  })
_sym_db.RegisterMessage(enum_type)

list_type = _reflection.GeneratedProtocolMessageType('list_type', (_message.Message,), {
  'DESCRIPTOR' : _LIST_TYPE,
  '__module__' : 'koinos.chain.value_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.list_type)
  })
_sym_db.RegisterMessage(list_type)


DESCRIPTOR._options = None
_VALUE_TYPE.fields_by_name['int64_value']._options = None
_VALUE_TYPE.fields_by_name['uint64_value']._options = None
_VALUE_TYPE.fields_by_name['sint64_value']._options = None
_VALUE_TYPE.fields_by_name['fixed64_value']._options = None
_VALUE_TYPE.fields_by_name['sfixed64_value']._options = None
# @@protoc_insertion_point(module_scope)
