# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/rpc/mempool/mempool_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2
from koinos.protocol import protocol_pb2 as koinos_dot_protocol_dot_protocol__pb2
from koinos.rpc import rpc_pb2 as koinos_dot_rpc_dot_rpc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/rpc/mempool/mempool_rpc.proto',
  package='koinos.rpc.mempool',
  syntax='proto3',
  serialized_options=b'Z;github.com/koinos/koinos-proto-golang/v2/koinos/rpc/mempool',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$koinos/rpc/mempool/mempool_rpc.proto\x12\x12koinos.rpc.mempool\x1a\x14koinos/options.proto\x1a\x1ekoinos/protocol/protocol.proto\x1a\x14koinos/rpc/rpc.proto\"\xaf\x01\n\x13pending_transaction\x12\x31\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1c.koinos.protocol.transaction\x12\x1d\n\x11\x64isk_storage_used\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\"\n\x16network_bandwidth_used\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\"\n\x16\x63ompute_bandwidth_used\x18\x04 \x01(\x04\x42\x02\x30\x01\"\x98\x01\n\'check_pending_account_resources_request\x12\x13\n\x05payer\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\x18\n\x0cmax_payer_rc\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08rc_limit\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x1b\n\x08\x62lock_id\x18\x04 \x01(\x0c\x42\x04\x80\xb5\x18\x03H\x00\x88\x01\x01\x42\x0b\n\t_block_id\";\n(check_pending_account_resources_response\x12\x0f\n\x07success\x18\x01 \x01(\x08\"_\n get_pending_transactions_request\x12\x11\n\x05limit\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x1b\n\x08\x62lock_id\x18\x02 \x01(\x0c\x42\x04\x80\xb5\x18\x03H\x00\x88\x01\x01\x42\x0b\n\t_block_id\"j\n!get_pending_transactions_response\x12\x45\n\x14pending_transactions\x18\x01 \x03(\x0b\x32\'.koinos.rpc.mempool.pending_transaction\"k\n\x1b\x63heck_account_nonce_request\x12\x13\n\x05payee\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\x12\r\n\x05nonce\x18\x02 \x01(\x0c\x12\x1b\n\x08\x62lock_id\x18\x03 \x01(\x0c\x42\x04\x80\xb5\x18\x03H\x00\x88\x01\x01\x42\x0b\n\t_block_id\"/\n\x1c\x63heck_account_nonce_response\x12\x0f\n\x07success\x18\x01 \x01(\x08\"8\n\x1fget_reserved_account_rc_request\x12\x15\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x06\".\n get_reserved_account_rc_response\x12\n\n\x02rc\x18\x01 \x01(\x04\"\xb4\x03\n\x0fmempool_request\x12,\n\x08reserved\x18\x01 \x01(\x0b\x32\x18.koinos.rpc.reserved_rpcH\x00\x12\x66\n\x1f\x63heck_pending_account_resources\x18\x02 \x01(\x0b\x32;.koinos.rpc.mempool.check_pending_account_resources_requestH\x00\x12X\n\x18get_pending_transactions\x18\x03 \x01(\x0b\x32\x34.koinos.rpc.mempool.get_pending_transactions_requestH\x00\x12N\n\x13\x63heck_account_nonce\x18\x04 \x01(\x0b\x32/.koinos.rpc.mempool.check_account_nonce_requestH\x00\x12V\n\x17get_reserved_account_rc\x18\x05 \x01(\x0b\x32\x33.koinos.rpc.mempool.get_reserved_account_rc_requestH\x00\x42\t\n\x07request\"\xe5\x03\n\x10mempool_response\x12,\n\x08reserved\x18\x01 \x01(\x0b\x32\x18.koinos.rpc.reserved_rpcH\x00\x12)\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x18.koinos.rpc.error_statusH\x00\x12g\n\x1f\x63heck_pending_account_resources\x18\x03 \x01(\x0b\x32<.koinos.rpc.mempool.check_pending_account_resources_responseH\x00\x12Y\n\x18get_pending_transactions\x18\x04 \x01(\x0b\x32\x35.koinos.rpc.mempool.get_pending_transactions_responseH\x00\x12O\n\x13\x63heck_account_nonce\x18\x05 \x01(\x0b\x32\x30.koinos.rpc.mempool.check_account_nonce_responseH\x00\x12W\n\x17get_reserved_account_rc\x18\x06 \x01(\x0b\x32\x34.koinos.rpc.mempool.get_reserved_account_rc_responseH\x00\x42\n\n\x08responseB=Z;github.com/koinos/koinos-proto-golang/v2/koinos/rpc/mempoolb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,koinos_dot_protocol_dot_protocol__pb2.DESCRIPTOR,koinos_dot_rpc_dot_rpc__pb2.DESCRIPTOR,])




_PENDING_TRANSACTION = _descriptor.Descriptor(
  name='pending_transaction',
  full_name='koinos.rpc.mempool.pending_transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='koinos.rpc.mempool.pending_transaction.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disk_storage_used', full_name='koinos.rpc.mempool.pending_transaction.disk_storage_used', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_bandwidth_used', full_name='koinos.rpc.mempool.pending_transaction.network_bandwidth_used', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_bandwidth_used', full_name='koinos.rpc.mempool.pending_transaction.compute_bandwidth_used', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=137,
  serialized_end=312,
)


_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST = _descriptor.Descriptor(
  name='check_pending_account_resources_request',
  full_name='koinos.rpc.mempool.check_pending_account_resources_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payer', full_name='koinos.rpc.mempool.check_pending_account_resources_request.payer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_payer_rc', full_name='koinos.rpc.mempool.check_pending_account_resources_request.max_payer_rc', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rc_limit', full_name='koinos.rpc.mempool.check_pending_account_resources_request.rc_limit', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.rpc.mempool.check_pending_account_resources_request.block_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_block_id', full_name='koinos.rpc.mempool.check_pending_account_resources_request._block_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=315,
  serialized_end=467,
)


_CHECK_PENDING_ACCOUNT_RESOURCES_RESPONSE = _descriptor.Descriptor(
  name='check_pending_account_resources_response',
  full_name='koinos.rpc.mempool.check_pending_account_resources_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='koinos.rpc.mempool.check_pending_account_resources_response.success', index=0,
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
  serialized_start=469,
  serialized_end=528,
)


_GET_PENDING_TRANSACTIONS_REQUEST = _descriptor.Descriptor(
  name='get_pending_transactions_request',
  full_name='koinos.rpc.mempool.get_pending_transactions_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='koinos.rpc.mempool.get_pending_transactions_request.limit', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'0\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.rpc.mempool.get_pending_transactions_request.block_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_block_id', full_name='koinos.rpc.mempool.get_pending_transactions_request._block_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=530,
  serialized_end=625,
)


_GET_PENDING_TRANSACTIONS_RESPONSE = _descriptor.Descriptor(
  name='get_pending_transactions_response',
  full_name='koinos.rpc.mempool.get_pending_transactions_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending_transactions', full_name='koinos.rpc.mempool.get_pending_transactions_response.pending_transactions', index=0,
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
  serialized_start=627,
  serialized_end=733,
)


_CHECK_ACCOUNT_NONCE_REQUEST = _descriptor.Descriptor(
  name='check_account_nonce_request',
  full_name='koinos.rpc.mempool.check_account_nonce_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payee', full_name='koinos.rpc.mempool.check_account_nonce_request.payee', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='koinos.rpc.mempool.check_account_nonce_request.nonce', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.rpc.mempool.check_account_nonce_request.block_id', index=2,
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
    _descriptor.OneofDescriptor(
      name='_block_id', full_name='koinos.rpc.mempool.check_account_nonce_request._block_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=735,
  serialized_end=842,
)


_CHECK_ACCOUNT_NONCE_RESPONSE = _descriptor.Descriptor(
  name='check_account_nonce_response',
  full_name='koinos.rpc.mempool.check_account_nonce_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='koinos.rpc.mempool.check_account_nonce_response.success', index=0,
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
  serialized_start=844,
  serialized_end=891,
)


_GET_RESERVED_ACCOUNT_RC_REQUEST = _descriptor.Descriptor(
  name='get_reserved_account_rc_request',
  full_name='koinos.rpc.mempool.get_reserved_account_rc_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='koinos.rpc.mempool.get_reserved_account_rc_request.account', index=0,
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
  serialized_start=893,
  serialized_end=949,
)


_GET_RESERVED_ACCOUNT_RC_RESPONSE = _descriptor.Descriptor(
  name='get_reserved_account_rc_response',
  full_name='koinos.rpc.mempool.get_reserved_account_rc_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='koinos.rpc.mempool.get_reserved_account_rc_response.rc', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=951,
  serialized_end=997,
)


_MEMPOOL_REQUEST = _descriptor.Descriptor(
  name='mempool_request',
  full_name='koinos.rpc.mempool.mempool_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reserved', full_name='koinos.rpc.mempool.mempool_request.reserved', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check_pending_account_resources', full_name='koinos.rpc.mempool.mempool_request.check_pending_account_resources', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_pending_transactions', full_name='koinos.rpc.mempool.mempool_request.get_pending_transactions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check_account_nonce', full_name='koinos.rpc.mempool.mempool_request.check_account_nonce', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_reserved_account_rc', full_name='koinos.rpc.mempool.mempool_request.get_reserved_account_rc', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
      name='request', full_name='koinos.rpc.mempool.mempool_request.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1000,
  serialized_end=1436,
)


_MEMPOOL_RESPONSE = _descriptor.Descriptor(
  name='mempool_response',
  full_name='koinos.rpc.mempool.mempool_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reserved', full_name='koinos.rpc.mempool.mempool_response.reserved', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='koinos.rpc.mempool.mempool_response.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check_pending_account_resources', full_name='koinos.rpc.mempool.mempool_response.check_pending_account_resources', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_pending_transactions', full_name='koinos.rpc.mempool.mempool_response.get_pending_transactions', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check_account_nonce', full_name='koinos.rpc.mempool.mempool_response.check_account_nonce', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_reserved_account_rc', full_name='koinos.rpc.mempool.mempool_response.get_reserved_account_rc', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
      name='response', full_name='koinos.rpc.mempool.mempool_response.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1439,
  serialized_end=1924,
)

_PENDING_TRANSACTION.fields_by_name['transaction'].message_type = koinos_dot_protocol_dot_protocol__pb2._TRANSACTION
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.oneofs_by_name['_block_id'].fields.append(
  _CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['block_id'])
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['block_id'].containing_oneof = _CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.oneofs_by_name['_block_id']
_GET_PENDING_TRANSACTIONS_REQUEST.oneofs_by_name['_block_id'].fields.append(
  _GET_PENDING_TRANSACTIONS_REQUEST.fields_by_name['block_id'])
_GET_PENDING_TRANSACTIONS_REQUEST.fields_by_name['block_id'].containing_oneof = _GET_PENDING_TRANSACTIONS_REQUEST.oneofs_by_name['_block_id']
_GET_PENDING_TRANSACTIONS_RESPONSE.fields_by_name['pending_transactions'].message_type = _PENDING_TRANSACTION
_CHECK_ACCOUNT_NONCE_REQUEST.oneofs_by_name['_block_id'].fields.append(
  _CHECK_ACCOUNT_NONCE_REQUEST.fields_by_name['block_id'])
_CHECK_ACCOUNT_NONCE_REQUEST.fields_by_name['block_id'].containing_oneof = _CHECK_ACCOUNT_NONCE_REQUEST.oneofs_by_name['_block_id']
_MEMPOOL_REQUEST.fields_by_name['reserved'].message_type = koinos_dot_rpc_dot_rpc__pb2._RESERVED_RPC
_MEMPOOL_REQUEST.fields_by_name['check_pending_account_resources'].message_type = _CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST
_MEMPOOL_REQUEST.fields_by_name['get_pending_transactions'].message_type = _GET_PENDING_TRANSACTIONS_REQUEST
_MEMPOOL_REQUEST.fields_by_name['check_account_nonce'].message_type = _CHECK_ACCOUNT_NONCE_REQUEST
_MEMPOOL_REQUEST.fields_by_name['get_reserved_account_rc'].message_type = _GET_RESERVED_ACCOUNT_RC_REQUEST
_MEMPOOL_REQUEST.oneofs_by_name['request'].fields.append(
  _MEMPOOL_REQUEST.fields_by_name['reserved'])
_MEMPOOL_REQUEST.fields_by_name['reserved'].containing_oneof = _MEMPOOL_REQUEST.oneofs_by_name['request']
_MEMPOOL_REQUEST.oneofs_by_name['request'].fields.append(
  _MEMPOOL_REQUEST.fields_by_name['check_pending_account_resources'])
_MEMPOOL_REQUEST.fields_by_name['check_pending_account_resources'].containing_oneof = _MEMPOOL_REQUEST.oneofs_by_name['request']
_MEMPOOL_REQUEST.oneofs_by_name['request'].fields.append(
  _MEMPOOL_REQUEST.fields_by_name['get_pending_transactions'])
_MEMPOOL_REQUEST.fields_by_name['get_pending_transactions'].containing_oneof = _MEMPOOL_REQUEST.oneofs_by_name['request']
_MEMPOOL_REQUEST.oneofs_by_name['request'].fields.append(
  _MEMPOOL_REQUEST.fields_by_name['check_account_nonce'])
_MEMPOOL_REQUEST.fields_by_name['check_account_nonce'].containing_oneof = _MEMPOOL_REQUEST.oneofs_by_name['request']
_MEMPOOL_REQUEST.oneofs_by_name['request'].fields.append(
  _MEMPOOL_REQUEST.fields_by_name['get_reserved_account_rc'])
_MEMPOOL_REQUEST.fields_by_name['get_reserved_account_rc'].containing_oneof = _MEMPOOL_REQUEST.oneofs_by_name['request']
_MEMPOOL_RESPONSE.fields_by_name['reserved'].message_type = koinos_dot_rpc_dot_rpc__pb2._RESERVED_RPC
_MEMPOOL_RESPONSE.fields_by_name['error'].message_type = koinos_dot_rpc_dot_rpc__pb2._ERROR_STATUS
_MEMPOOL_RESPONSE.fields_by_name['check_pending_account_resources'].message_type = _CHECK_PENDING_ACCOUNT_RESOURCES_RESPONSE
_MEMPOOL_RESPONSE.fields_by_name['get_pending_transactions'].message_type = _GET_PENDING_TRANSACTIONS_RESPONSE
_MEMPOOL_RESPONSE.fields_by_name['check_account_nonce'].message_type = _CHECK_ACCOUNT_NONCE_RESPONSE
_MEMPOOL_RESPONSE.fields_by_name['get_reserved_account_rc'].message_type = _GET_RESERVED_ACCOUNT_RC_RESPONSE
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['reserved'])
_MEMPOOL_RESPONSE.fields_by_name['reserved'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['error'])
_MEMPOOL_RESPONSE.fields_by_name['error'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['check_pending_account_resources'])
_MEMPOOL_RESPONSE.fields_by_name['check_pending_account_resources'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['get_pending_transactions'])
_MEMPOOL_RESPONSE.fields_by_name['get_pending_transactions'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['check_account_nonce'])
_MEMPOOL_RESPONSE.fields_by_name['check_account_nonce'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
_MEMPOOL_RESPONSE.oneofs_by_name['response'].fields.append(
  _MEMPOOL_RESPONSE.fields_by_name['get_reserved_account_rc'])
_MEMPOOL_RESPONSE.fields_by_name['get_reserved_account_rc'].containing_oneof = _MEMPOOL_RESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['pending_transaction'] = _PENDING_TRANSACTION
DESCRIPTOR.message_types_by_name['check_pending_account_resources_request'] = _CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST
DESCRIPTOR.message_types_by_name['check_pending_account_resources_response'] = _CHECK_PENDING_ACCOUNT_RESOURCES_RESPONSE
DESCRIPTOR.message_types_by_name['get_pending_transactions_request'] = _GET_PENDING_TRANSACTIONS_REQUEST
DESCRIPTOR.message_types_by_name['get_pending_transactions_response'] = _GET_PENDING_TRANSACTIONS_RESPONSE
DESCRIPTOR.message_types_by_name['check_account_nonce_request'] = _CHECK_ACCOUNT_NONCE_REQUEST
DESCRIPTOR.message_types_by_name['check_account_nonce_response'] = _CHECK_ACCOUNT_NONCE_RESPONSE
DESCRIPTOR.message_types_by_name['get_reserved_account_rc_request'] = _GET_RESERVED_ACCOUNT_RC_REQUEST
DESCRIPTOR.message_types_by_name['get_reserved_account_rc_response'] = _GET_RESERVED_ACCOUNT_RC_RESPONSE
DESCRIPTOR.message_types_by_name['mempool_request'] = _MEMPOOL_REQUEST
DESCRIPTOR.message_types_by_name['mempool_response'] = _MEMPOOL_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

pending_transaction = _reflection.GeneratedProtocolMessageType('pending_transaction', (_message.Message,), {
  'DESCRIPTOR' : _PENDING_TRANSACTION,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.pending_transaction)
  })
_sym_db.RegisterMessage(pending_transaction)

check_pending_account_resources_request = _reflection.GeneratedProtocolMessageType('check_pending_account_resources_request', (_message.Message,), {
  'DESCRIPTOR' : _CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.check_pending_account_resources_request)
  })
_sym_db.RegisterMessage(check_pending_account_resources_request)

check_pending_account_resources_response = _reflection.GeneratedProtocolMessageType('check_pending_account_resources_response', (_message.Message,), {
  'DESCRIPTOR' : _CHECK_PENDING_ACCOUNT_RESOURCES_RESPONSE,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.check_pending_account_resources_response)
  })
_sym_db.RegisterMessage(check_pending_account_resources_response)

get_pending_transactions_request = _reflection.GeneratedProtocolMessageType('get_pending_transactions_request', (_message.Message,), {
  'DESCRIPTOR' : _GET_PENDING_TRANSACTIONS_REQUEST,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.get_pending_transactions_request)
  })
_sym_db.RegisterMessage(get_pending_transactions_request)

get_pending_transactions_response = _reflection.GeneratedProtocolMessageType('get_pending_transactions_response', (_message.Message,), {
  'DESCRIPTOR' : _GET_PENDING_TRANSACTIONS_RESPONSE,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.get_pending_transactions_response)
  })
_sym_db.RegisterMessage(get_pending_transactions_response)

check_account_nonce_request = _reflection.GeneratedProtocolMessageType('check_account_nonce_request', (_message.Message,), {
  'DESCRIPTOR' : _CHECK_ACCOUNT_NONCE_REQUEST,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.check_account_nonce_request)
  })
_sym_db.RegisterMessage(check_account_nonce_request)

check_account_nonce_response = _reflection.GeneratedProtocolMessageType('check_account_nonce_response', (_message.Message,), {
  'DESCRIPTOR' : _CHECK_ACCOUNT_NONCE_RESPONSE,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.check_account_nonce_response)
  })
_sym_db.RegisterMessage(check_account_nonce_response)

get_reserved_account_rc_request = _reflection.GeneratedProtocolMessageType('get_reserved_account_rc_request', (_message.Message,), {
  'DESCRIPTOR' : _GET_RESERVED_ACCOUNT_RC_REQUEST,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.get_reserved_account_rc_request)
  })
_sym_db.RegisterMessage(get_reserved_account_rc_request)

get_reserved_account_rc_response = _reflection.GeneratedProtocolMessageType('get_reserved_account_rc_response', (_message.Message,), {
  'DESCRIPTOR' : _GET_RESERVED_ACCOUNT_RC_RESPONSE,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.get_reserved_account_rc_response)
  })
_sym_db.RegisterMessage(get_reserved_account_rc_response)

mempool_request = _reflection.GeneratedProtocolMessageType('mempool_request', (_message.Message,), {
  'DESCRIPTOR' : _MEMPOOL_REQUEST,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.mempool_request)
  })
_sym_db.RegisterMessage(mempool_request)

mempool_response = _reflection.GeneratedProtocolMessageType('mempool_response', (_message.Message,), {
  'DESCRIPTOR' : _MEMPOOL_RESPONSE,
  '__module__' : 'koinos.rpc.mempool.mempool_rpc_pb2'
  # @@protoc_insertion_point(class_scope:koinos.rpc.mempool.mempool_response)
  })
_sym_db.RegisterMessage(mempool_response)


DESCRIPTOR._options = None
_PENDING_TRANSACTION.fields_by_name['disk_storage_used']._options = None
_PENDING_TRANSACTION.fields_by_name['network_bandwidth_used']._options = None
_PENDING_TRANSACTION.fields_by_name['compute_bandwidth_used']._options = None
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['payer']._options = None
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['max_payer_rc']._options = None
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['rc_limit']._options = None
_CHECK_PENDING_ACCOUNT_RESOURCES_REQUEST.fields_by_name['block_id']._options = None
_GET_PENDING_TRANSACTIONS_REQUEST.fields_by_name['limit']._options = None
_GET_PENDING_TRANSACTIONS_REQUEST.fields_by_name['block_id']._options = None
_CHECK_ACCOUNT_NONCE_REQUEST.fields_by_name['payee']._options = None
_CHECK_ACCOUNT_NONCE_REQUEST.fields_by_name['block_id']._options = None
_GET_RESERVED_ACCOUNT_RC_REQUEST.fields_by_name['account']._options = None
# @@protoc_insertion_point(module_scope)
