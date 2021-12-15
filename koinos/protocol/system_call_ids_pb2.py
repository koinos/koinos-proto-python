# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/protocol/system_call_ids.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/protocol/system_call_ids.proto',
  package='koinos.protocol',
  syntax='proto3',
  serialized_options=b'Z5github.com/koinos/koinos-proto-golang/koinos/protocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%koinos/protocol/system_call_ids.proto\x12\x0fkoinos.protocol*\x93\x07\n\x0esystem_call_id\x12\x0f\n\x0breserved_id\x10\x00\x12\x11\n\rget_head_info\x10\x01\x12\x0f\n\x0b\x61pply_block\x10\x02\x12\x15\n\x11\x61pply_transaction\x10\x03\x12#\n\x1f\x61pply_upload_contract_operation\x10\x04\x12!\n\x1d\x61pply_call_contract_operation\x10\x05\x12#\n\x1f\x61pply_set_system_call_operation\x10\x06\x12\'\n#apply_set_system_contract_operation\x10\x07\x12\x1b\n\x17process_block_signature\x10\x65\x12\x19\n\x15get_transaction_payer\x10\x66\x12\x1c\n\x18get_transaction_rc_limit\x10g\x12\x1d\n\x19get_transaction_signature\x10h\x12\x1f\n\x1bget_last_irreversible_block\x10i\x12\x15\n\x11get_account_nonce\x10j\x12\x13\n\x0eget_account_rc\x10\xc9\x01\x12\x17\n\x12\x63onsume_account_rc\x10\xca\x01\x12\x18\n\x13get_resource_limits\x10\xcb\x01\x12\x1c\n\x17\x63onsume_block_resources\x10\xcc\x01\x12\x0f\n\nput_object\x10\xad\x02\x12\x12\n\rremove_object\x10\xae\x02\x12\x0f\n\nget_object\x10\xaf\x02\x12\x14\n\x0fget_next_object\x10\xb0\x02\x12\x14\n\x0fget_prev_object\x10\xb1\x02\x12\x0b\n\x06prints\x10\x91\x03\x12\n\n\x05\x65vent\x10\x92\x03\x12\t\n\x04hash\x10\xf5\x03\x12\x17\n\x12recover_public_key\x10\xf6\x03\x12\x17\n\x12verify_merkle_root\x10\xf7\x03\x12\x12\n\rcall_contract\x10\xd9\x04\x12\x14\n\x0fget_entry_point\x10\xda\x04\x12 \n\x1bget_contract_arguments_size\x10\xdb\x04\x12\x1b\n\x16get_contract_arguments\x10\xdc\x04\x12\x18\n\x13set_contract_result\x10\xdd\x04\x12\x12\n\rexit_contract\x10\xde\x04\x12\x14\n\x0fget_contract_id\x10\xdf\x04\x12\x0f\n\nget_caller\x10\xe0\x04\x12\x16\n\x11require_authority\x10\xe1\x04\x42\x37Z5github.com/koinos/koinos-proto-golang/koinos/protocolb\x06proto3'
)

_SYSTEM_CALL_ID = _descriptor.EnumDescriptor(
  name='system_call_id',
  full_name='koinos.protocol.system_call_id',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='reserved_id', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_head_info', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_block', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_transaction', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_upload_contract_operation', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_call_contract_operation', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_set_system_call_operation', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='apply_set_system_contract_operation', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='process_block_signature', index=8, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_transaction_payer', index=9, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_transaction_rc_limit', index=10, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_transaction_signature', index=11, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_last_irreversible_block', index=12, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_account_nonce', index=13, number=106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_account_rc', index=14, number=201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='consume_account_rc', index=15, number=202,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_resource_limits', index=16, number=203,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='consume_block_resources', index=17, number=204,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='put_object', index=18, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='remove_object', index=19, number=302,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_object', index=20, number=303,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_next_object', index=21, number=304,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_prev_object', index=22, number=305,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='prints', index=23, number=401,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='event', index=24, number=402,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='hash', index=25, number=501,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='recover_public_key', index=26, number=502,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='verify_merkle_root', index=27, number=503,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='call_contract', index=28, number=601,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_entry_point', index=29, number=602,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_contract_arguments_size', index=30, number=603,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_contract_arguments', index=31, number=604,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='set_contract_result', index=32, number=605,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='exit_contract', index=33, number=606,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_contract_id', index=34, number=607,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='get_caller', index=35, number=608,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='require_authority', index=36, number=609,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=974,
)
_sym_db.RegisterEnumDescriptor(_SYSTEM_CALL_ID)

system_call_id = enum_type_wrapper.EnumTypeWrapper(_SYSTEM_CALL_ID)
reserved_id = 0
get_head_info = 1
apply_block = 2
apply_transaction = 3
apply_upload_contract_operation = 4
apply_call_contract_operation = 5
apply_set_system_call_operation = 6
apply_set_system_contract_operation = 7
process_block_signature = 101
get_transaction_payer = 102
get_transaction_rc_limit = 103
get_transaction_signature = 104
get_last_irreversible_block = 105
get_account_nonce = 106
get_account_rc = 201
consume_account_rc = 202
get_resource_limits = 203
consume_block_resources = 204
put_object = 301
remove_object = 302
get_object = 303
get_next_object = 304
get_prev_object = 305
prints = 401
event = 402
hash = 501
recover_public_key = 502
verify_merkle_root = 503
call_contract = 601
get_entry_point = 602
get_contract_arguments_size = 603
get_contract_arguments = 604
set_contract_result = 605
exit_contract = 606
get_contract_id = 607
get_caller = 608
require_authority = 609


DESCRIPTOR.enum_types_by_name['system_call_id'] = _SYSTEM_CALL_ID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
