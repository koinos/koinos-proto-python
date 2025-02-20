# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/chain/error.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/chain/error.proto',
  package='koinos.chain',
  syntax='proto3',
  serialized_options=b'Z5github.com/koinos/koinos-proto-golang/v2/koinos/chain',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18koinos/chain/error.proto\x12\x0ckoinos.chain\"+\n\rerror_details\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04logs\x18\x02 \x03(\t*\xf1\t\n\nerror_code\x12\x0b\n\x07success\x10\x00\x12\r\n\treversion\x10\x01\x12\x12\n\x0einternal_error\x10\x64\x12 \n\x1csystem_authorization_failure\x10\x65\x12\x14\n\x10invalid_contract\x10\x66\x12\x1b\n\x17insufficient_privileges\x10g\x12\x13\n\x0finsufficient_rc\x10h\x12\x1e\n\x1ainsufficient_return_buffer\x10i\x12\x11\n\runknown_thunk\x10j\x12\x15\n\x11unknown_operation\x10k\x12\x15\n\x11read_only_context\x10l\x12\x14\n\x07\x66\x61ilure\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0f\x66ield_not_found\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x11unknown_hash_code\x10\x9b\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x0bunknown_dsa\x10\x9a\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13unknown_system_call\x10\x99\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13operation_not_found\x10\x98\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\"\n\x15\x61uthorization_failure\x10\xb8\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\rinvalid_nonce\x10\xb7\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x11invalid_signature\x10\xb6\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fmalformed_block\x10\xb5\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\"\n\x15malformed_transaction\x10\xb4\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x16\x62lock_resource_failure\x10\xb3\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12/\n\"pending_transaction_limit_exceeded\x10\xb2\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0funknown_backend\x10\x98\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1d\n\x10unexpected_state\x10\x97\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\'\n\x1amissing_required_arguments\x10\x96\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x16unknown_previous_block\x10\x95\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x11unexpected_height\x10\x94\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x11\x62lock_state_error\x10\x93\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\"\n\x15state_merkle_mismatch\x10\x92\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12unexpected_receipt\x10\x91\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x0brpc_failure\x10\x90\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13pending_state_error\x10\x8f\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17timestamp_out_of_bounds\x10\x8e\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0findexer_failure\x10\x8d\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12-\n network_bandwidth_limit_exceeded\x10\x8c\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12-\n compute_bandwidth_limit_exceeded\x10\x8b\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n\x1b\x64isk_storage_limit_exceeded\x10\x8a\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x12&\n\x19pre_irreversibility_block\x10\x89\xf8\xff\xff\xff\xff\xff\xff\xff\x01\x42\x37Z5github.com/koinos/koinos-proto-golang/v2/koinos/chainb\x06proto3'
)

_ERROR_CODE = _descriptor.EnumDescriptor(
  name='error_code',
  full_name='koinos.chain.error_code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='success', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='reversion', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='internal_error', index=2, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='system_authorization_failure', index=3, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='invalid_contract', index=4, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='insufficient_privileges', index=5, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='insufficient_rc', index=6, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='insufficient_return_buffer', index=7, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_thunk', index=8, number=106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_operation', index=9, number=107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='read_only_context', index=10, number=108,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='failure', index=11, number=-1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='field_not_found', index=12, number=-100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_hash_code', index=13, number=-101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_dsa', index=14, number=-102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_system_call', index=15, number=-103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='operation_not_found', index=16, number=-104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='authorization_failure', index=17, number=-200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='invalid_nonce', index=18, number=-201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='invalid_signature', index=19, number=-202,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='malformed_block', index=20, number=-203,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='malformed_transaction', index=21, number=-204,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='block_resource_failure', index=22, number=-205,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='pending_transaction_limit_exceeded', index=23, number=-206,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_backend', index=24, number=-1000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unexpected_state', index=25, number=-1001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='missing_required_arguments', index=26, number=-1002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown_previous_block', index=27, number=-1003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unexpected_height', index=28, number=-1004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='block_state_error', index=29, number=-1005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='state_merkle_mismatch', index=30, number=-1006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unexpected_receipt', index=31, number=-1007,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='rpc_failure', index=32, number=-1008,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='pending_state_error', index=33, number=-1009,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='timestamp_out_of_bounds', index=34, number=-1010,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='indexer_failure', index=35, number=-1011,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='network_bandwidth_limit_exceeded', index=36, number=-1012,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='compute_bandwidth_limit_exceeded', index=37, number=-1013,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='disk_storage_limit_exceeded', index=38, number=-1014,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='pre_irreversibility_block', index=39, number=-1015,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=88,
  serialized_end=1353,
)
_sym_db.RegisterEnumDescriptor(_ERROR_CODE)

error_code = enum_type_wrapper.EnumTypeWrapper(_ERROR_CODE)
success = 0
reversion = 1
internal_error = 100
system_authorization_failure = 101
invalid_contract = 102
insufficient_privileges = 103
insufficient_rc = 104
insufficient_return_buffer = 105
unknown_thunk = 106
unknown_operation = 107
read_only_context = 108
failure = -1
field_not_found = -100
unknown_hash_code = -101
unknown_dsa = -102
unknown_system_call = -103
operation_not_found = -104
authorization_failure = -200
invalid_nonce = -201
invalid_signature = -202
malformed_block = -203
malformed_transaction = -204
block_resource_failure = -205
pending_transaction_limit_exceeded = -206
unknown_backend = -1000
unexpected_state = -1001
missing_required_arguments = -1002
unknown_previous_block = -1003
unexpected_height = -1004
block_state_error = -1005
state_merkle_mismatch = -1006
unexpected_receipt = -1007
rpc_failure = -1008
pending_state_error = -1009
timestamp_out_of_bounds = -1010
indexer_failure = -1011
network_bandwidth_limit_exceeded = -1012
compute_bandwidth_limit_exceeded = -1013
disk_storage_limit_exceeded = -1014
pre_irreversibility_block = -1015



_ERROR_DETAILS = _descriptor.Descriptor(
  name='error_details',
  full_name='koinos.chain.error_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='koinos.chain.error_details.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='koinos.chain.error_details.logs', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=42,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['error_details'] = _ERROR_DETAILS
DESCRIPTOR.enum_types_by_name['error_code'] = _ERROR_CODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

error_details = _reflection.GeneratedProtocolMessageType('error_details', (_message.Message,), {
  'DESCRIPTOR' : _ERROR_DETAILS,
  '__module__' : 'koinos.chain.error_pb2'
  # @@protoc_insertion_point(class_scope:koinos.chain.error_details)
  })
_sym_db.RegisterMessage(error_details)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
