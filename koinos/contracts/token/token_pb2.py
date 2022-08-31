# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/contracts/token/token.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/contracts/token/token.proto',
  package='koinos.contracts.token',
  syntax='proto3',
  serialized_options=b'Z<github.com/koinos/koinos-proto-golang/koinos/contracts/token',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"koinos/contracts/token/token.proto\x12\x16koinos.contracts.token\x1a\x14koinos/options.proto\"\x10\n\x0ename_arguments\"\x1c\n\x0bname_result\x12\r\n\x05value\x18\x01 \x01(\t\"\x12\n\x10symbol_arguments\"\x1e\n\rsymbol_result\x12\r\n\x05value\x18\x01 \x01(\t\"\x14\n\x12\x64\x65\x63imals_arguments\" \n\x0f\x64\x65\x63imals_result\x12\r\n\x05value\x18\x01 \x01(\r\"\x18\n\x16total_supply_arguments\"(\n\x13total_supply_result\x12\x11\n\x05value\x18\x01 \x01(\x04\x42\x02\x30\x01\"+\n\x14\x62\x61lance_of_arguments\x12\x13\n\x05owner\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\"&\n\x11\x62\x61lance_of_result\x12\x11\n\x05value\x18\x01 \x01(\x04\x42\x02\x30\x01\"M\n\x12transfer_arguments\x12\x12\n\x04\x66rom\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x10\n\x02to\x18\x02 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x03 \x01(\x04\x42\x02\x30\x01\"\x11\n\x0ftransfer_result\"5\n\x0emint_arguments\x12\x10\n\x02to\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x02 \x01(\x04\x42\x02\x30\x01\"\r\n\x0bmint_result\"7\n\x0e\x62urn_arguments\x12\x12\n\x04\x66rom\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x02 \x01(\x04\x42\x02\x30\x01\"\r\n\x0b\x62urn_result\"#\n\x0e\x62\x61lance_object\x12\x11\n\x05value\x18\x01 \x01(\x04\x42\x02\x30\x01\"3\n\nburn_event\x12\x12\n\x04\x66rom\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x02 \x01(\x04\x42\x02\x30\x01\"1\n\nmint_event\x12\x10\n\x02to\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x02 \x01(\x04\x42\x02\x30\x01\"I\n\x0etransfer_event\x12\x12\n\x04\x66rom\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x10\n\x02to\x18\x02 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x11\n\x05value\x18\x03 \x01(\x04\x42\x02\x30\x01\x42>Z<github.com/koinos/koinos-proto-golang/koinos/contracts/tokenb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,])




_NAME_ARGUMENTS = _descriptor.Descriptor(
  name='name_arguments',
  full_name='koinos.contracts.token.name_arguments',
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
  serialized_start=84,
  serialized_end=100,
)


_NAME_RESULT = _descriptor.Descriptor(
  name='name_result',
  full_name='koinos.contracts.token.name_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.name_result.value', index=0,
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
  serialized_start=102,
  serialized_end=130,
)


_SYMBOL_ARGUMENTS = _descriptor.Descriptor(
  name='symbol_arguments',
  full_name='koinos.contracts.token.symbol_arguments',
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
  serialized_start=132,
  serialized_end=150,
)


_SYMBOL_RESULT = _descriptor.Descriptor(
  name='symbol_result',
  full_name='koinos.contracts.token.symbol_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.symbol_result.value', index=0,
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
  serialized_start=152,
  serialized_end=182,
)


_DECIMALS_ARGUMENTS = _descriptor.Descriptor(
  name='decimals_arguments',
  full_name='koinos.contracts.token.decimals_arguments',
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
  serialized_start=184,
  serialized_end=204,
)


_DECIMALS_RESULT = _descriptor.Descriptor(
  name='decimals_result',
  full_name='koinos.contracts.token.decimals_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.decimals_result.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=206,
  serialized_end=238,
)


_TOTAL_SUPPLY_ARGUMENTS = _descriptor.Descriptor(
  name='total_supply_arguments',
  full_name='koinos.contracts.token.total_supply_arguments',
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
  serialized_start=240,
  serialized_end=264,
)


_TOTAL_SUPPLY_RESULT = _descriptor.Descriptor(
  name='total_supply_result',
  full_name='koinos.contracts.token.total_supply_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.total_supply_result.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=266,
  serialized_end=306,
)


_BALANCE_OF_ARGUMENTS = _descriptor.Descriptor(
  name='balance_of_arguments',
  full_name='koinos.contracts.token.balance_of_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='koinos.contracts.token.balance_of_arguments.owner', index=0,
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
  serialized_start=308,
  serialized_end=351,
)


_BALANCE_OF_RESULT = _descriptor.Descriptor(
  name='balance_of_result',
  full_name='koinos.contracts.token.balance_of_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.balance_of_result.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=353,
  serialized_end=391,
)


_TRANSFER_ARGUMENTS = _descriptor.Descriptor(
  name='transfer_arguments',
  full_name='koinos.contracts.token.transfer_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='koinos.contracts.token.transfer_arguments.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='koinos.contracts.token.transfer_arguments.to', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.transfer_arguments.value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=393,
  serialized_end=470,
)


_TRANSFER_RESULT = _descriptor.Descriptor(
  name='transfer_result',
  full_name='koinos.contracts.token.transfer_result',
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
  serialized_start=472,
  serialized_end=489,
)


_MINT_ARGUMENTS = _descriptor.Descriptor(
  name='mint_arguments',
  full_name='koinos.contracts.token.mint_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='koinos.contracts.token.mint_arguments.to', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.mint_arguments.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=491,
  serialized_end=544,
)


_MINT_RESULT = _descriptor.Descriptor(
  name='mint_result',
  full_name='koinos.contracts.token.mint_result',
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
  serialized_start=546,
  serialized_end=559,
)


_BURN_ARGUMENTS = _descriptor.Descriptor(
  name='burn_arguments',
  full_name='koinos.contracts.token.burn_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='koinos.contracts.token.burn_arguments.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.burn_arguments.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=561,
  serialized_end=616,
)


_BURN_RESULT = _descriptor.Descriptor(
  name='burn_result',
  full_name='koinos.contracts.token.burn_result',
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
  serialized_start=618,
  serialized_end=631,
)


_BALANCE_OBJECT = _descriptor.Descriptor(
  name='balance_object',
  full_name='koinos.contracts.token.balance_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.balance_object.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=633,
  serialized_end=668,
)


_BURN_EVENT = _descriptor.Descriptor(
  name='burn_event',
  full_name='koinos.contracts.token.burn_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='koinos.contracts.token.burn_event.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.burn_event.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=670,
  serialized_end=721,
)


_MINT_EVENT = _descriptor.Descriptor(
  name='mint_event',
  full_name='koinos.contracts.token.mint_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='koinos.contracts.token.mint_event.to', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.mint_event.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=723,
  serialized_end=772,
)


_TRANSFER_EVENT = _descriptor.Descriptor(
  name='transfer_event',
  full_name='koinos.contracts.token.transfer_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='koinos.contracts.token.transfer_event.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='koinos.contracts.token.transfer_event.to', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.token.transfer_event.value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=774,
  serialized_end=847,
)

DESCRIPTOR.message_types_by_name['name_arguments'] = _NAME_ARGUMENTS
DESCRIPTOR.message_types_by_name['name_result'] = _NAME_RESULT
DESCRIPTOR.message_types_by_name['symbol_arguments'] = _SYMBOL_ARGUMENTS
DESCRIPTOR.message_types_by_name['symbol_result'] = _SYMBOL_RESULT
DESCRIPTOR.message_types_by_name['decimals_arguments'] = _DECIMALS_ARGUMENTS
DESCRIPTOR.message_types_by_name['decimals_result'] = _DECIMALS_RESULT
DESCRIPTOR.message_types_by_name['total_supply_arguments'] = _TOTAL_SUPPLY_ARGUMENTS
DESCRIPTOR.message_types_by_name['total_supply_result'] = _TOTAL_SUPPLY_RESULT
DESCRIPTOR.message_types_by_name['balance_of_arguments'] = _BALANCE_OF_ARGUMENTS
DESCRIPTOR.message_types_by_name['balance_of_result'] = _BALANCE_OF_RESULT
DESCRIPTOR.message_types_by_name['transfer_arguments'] = _TRANSFER_ARGUMENTS
DESCRIPTOR.message_types_by_name['transfer_result'] = _TRANSFER_RESULT
DESCRIPTOR.message_types_by_name['mint_arguments'] = _MINT_ARGUMENTS
DESCRIPTOR.message_types_by_name['mint_result'] = _MINT_RESULT
DESCRIPTOR.message_types_by_name['burn_arguments'] = _BURN_ARGUMENTS
DESCRIPTOR.message_types_by_name['burn_result'] = _BURN_RESULT
DESCRIPTOR.message_types_by_name['balance_object'] = _BALANCE_OBJECT
DESCRIPTOR.message_types_by_name['burn_event'] = _BURN_EVENT
DESCRIPTOR.message_types_by_name['mint_event'] = _MINT_EVENT
DESCRIPTOR.message_types_by_name['transfer_event'] = _TRANSFER_EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

name_arguments = _reflection.GeneratedProtocolMessageType('name_arguments', (_message.Message,), {
  'DESCRIPTOR' : _NAME_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.name_arguments)
  })
_sym_db.RegisterMessage(name_arguments)

name_result = _reflection.GeneratedProtocolMessageType('name_result', (_message.Message,), {
  'DESCRIPTOR' : _NAME_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.name_result)
  })
_sym_db.RegisterMessage(name_result)

symbol_arguments = _reflection.GeneratedProtocolMessageType('symbol_arguments', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOL_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.symbol_arguments)
  })
_sym_db.RegisterMessage(symbol_arguments)

symbol_result = _reflection.GeneratedProtocolMessageType('symbol_result', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOL_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.symbol_result)
  })
_sym_db.RegisterMessage(symbol_result)

decimals_arguments = _reflection.GeneratedProtocolMessageType('decimals_arguments', (_message.Message,), {
  'DESCRIPTOR' : _DECIMALS_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.decimals_arguments)
  })
_sym_db.RegisterMessage(decimals_arguments)

decimals_result = _reflection.GeneratedProtocolMessageType('decimals_result', (_message.Message,), {
  'DESCRIPTOR' : _DECIMALS_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.decimals_result)
  })
_sym_db.RegisterMessage(decimals_result)

total_supply_arguments = _reflection.GeneratedProtocolMessageType('total_supply_arguments', (_message.Message,), {
  'DESCRIPTOR' : _TOTAL_SUPPLY_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.total_supply_arguments)
  })
_sym_db.RegisterMessage(total_supply_arguments)

total_supply_result = _reflection.GeneratedProtocolMessageType('total_supply_result', (_message.Message,), {
  'DESCRIPTOR' : _TOTAL_SUPPLY_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.total_supply_result)
  })
_sym_db.RegisterMessage(total_supply_result)

balance_of_arguments = _reflection.GeneratedProtocolMessageType('balance_of_arguments', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE_OF_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.balance_of_arguments)
  })
_sym_db.RegisterMessage(balance_of_arguments)

balance_of_result = _reflection.GeneratedProtocolMessageType('balance_of_result', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE_OF_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.balance_of_result)
  })
_sym_db.RegisterMessage(balance_of_result)

transfer_arguments = _reflection.GeneratedProtocolMessageType('transfer_arguments', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFER_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.transfer_arguments)
  })
_sym_db.RegisterMessage(transfer_arguments)

transfer_result = _reflection.GeneratedProtocolMessageType('transfer_result', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFER_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.transfer_result)
  })
_sym_db.RegisterMessage(transfer_result)

mint_arguments = _reflection.GeneratedProtocolMessageType('mint_arguments', (_message.Message,), {
  'DESCRIPTOR' : _MINT_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.mint_arguments)
  })
_sym_db.RegisterMessage(mint_arguments)

mint_result = _reflection.GeneratedProtocolMessageType('mint_result', (_message.Message,), {
  'DESCRIPTOR' : _MINT_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.mint_result)
  })
_sym_db.RegisterMessage(mint_result)

burn_arguments = _reflection.GeneratedProtocolMessageType('burn_arguments', (_message.Message,), {
  'DESCRIPTOR' : _BURN_ARGUMENTS,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.burn_arguments)
  })
_sym_db.RegisterMessage(burn_arguments)

burn_result = _reflection.GeneratedProtocolMessageType('burn_result', (_message.Message,), {
  'DESCRIPTOR' : _BURN_RESULT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.burn_result)
  })
_sym_db.RegisterMessage(burn_result)

balance_object = _reflection.GeneratedProtocolMessageType('balance_object', (_message.Message,), {
  'DESCRIPTOR' : _BALANCE_OBJECT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.balance_object)
  })
_sym_db.RegisterMessage(balance_object)

burn_event = _reflection.GeneratedProtocolMessageType('burn_event', (_message.Message,), {
  'DESCRIPTOR' : _BURN_EVENT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.burn_event)
  })
_sym_db.RegisterMessage(burn_event)

mint_event = _reflection.GeneratedProtocolMessageType('mint_event', (_message.Message,), {
  'DESCRIPTOR' : _MINT_EVENT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.mint_event)
  })
_sym_db.RegisterMessage(mint_event)

transfer_event = _reflection.GeneratedProtocolMessageType('transfer_event', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFER_EVENT,
  '__module__' : 'koinos.contracts.token.token_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.token.transfer_event)
  })
_sym_db.RegisterMessage(transfer_event)


DESCRIPTOR._options = None
_TOTAL_SUPPLY_RESULT.fields_by_name['value']._options = None
_BALANCE_OF_ARGUMENTS.fields_by_name['owner']._options = None
_BALANCE_OF_RESULT.fields_by_name['value']._options = None
_TRANSFER_ARGUMENTS.fields_by_name['from']._options = None
_TRANSFER_ARGUMENTS.fields_by_name['to']._options = None
_TRANSFER_ARGUMENTS.fields_by_name['value']._options = None
_MINT_ARGUMENTS.fields_by_name['to']._options = None
_MINT_ARGUMENTS.fields_by_name['value']._options = None
_BURN_ARGUMENTS.fields_by_name['from']._options = None
_BURN_ARGUMENTS.fields_by_name['value']._options = None
_BALANCE_OBJECT.fields_by_name['value']._options = None
_BURN_EVENT.fields_by_name['from']._options = None
_BURN_EVENT.fields_by_name['value']._options = None
_MINT_EVENT.fields_by_name['to']._options = None
_MINT_EVENT.fields_by_name['value']._options = None
_TRANSFER_EVENT.fields_by_name['from']._options = None
_TRANSFER_EVENT.fields_by_name['to']._options = None
_TRANSFER_EVENT.fields_by_name['value']._options = None
# @@protoc_insertion_point(module_scope)
