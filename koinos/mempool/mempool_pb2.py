# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/mempool/mempool.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos.protocol import protocol_pb2 as koinos_dot_protocol_dot_protocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/mempool/mempool.proto',
  package='koinos.mempool',
  syntax='proto3',
  serialized_options=b'Z4github.com/koinos/koinos-proto-golang/koinos/mempool',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ckoinos/mempool/mempool.proto\x12\x0ekoinos.mempool\x1a\x1ekoinos/protocol/protocol.proto\"#\n\x10mempool_metadata\x12\x0f\n\x07seq_num\x18\x01 \x01(\x04\"=\n\x17\x61\x64\x64ress_resource_record\x12\x0e\n\x06max_rc\x18\x01 \x01(\x04\x12\x12\n\ncurrent_rc\x18\x02 \x01(\x04\"\xbd\x01\n\x1apending_transaction_record\x12\x31\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1c.koinos.protocol.transaction\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x19\n\x11\x64isk_storage_used\x18\x03 \x01(\x04\x12\x1e\n\x16network_bandwidth_used\x18\x04 \x01(\x04\x12\x1e\n\x16\x63ompute_bandwidth_used\x18\x05 \x01(\x04\x42\x36Z4github.com/koinos/koinos-proto-golang/koinos/mempoolb\x06proto3'
  ,
  dependencies=[koinos_dot_protocol_dot_protocol__pb2.DESCRIPTOR,])




_MEMPOOL_METADATA = _descriptor.Descriptor(
  name='mempool_metadata',
  full_name='koinos.mempool.mempool_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq_num', full_name='koinos.mempool.mempool_metadata.seq_num', index=0,
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
  serialized_start=80,
  serialized_end=115,
)


_ADDRESS_RESOURCE_RECORD = _descriptor.Descriptor(
  name='address_resource_record',
  full_name='koinos.mempool.address_resource_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_rc', full_name='koinos.mempool.address_resource_record.max_rc', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_rc', full_name='koinos.mempool.address_resource_record.current_rc', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=117,
  serialized_end=178,
)


_PENDING_TRANSACTION_RECORD = _descriptor.Descriptor(
  name='pending_transaction_record',
  full_name='koinos.mempool.pending_transaction_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='koinos.mempool.pending_transaction_record.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='koinos.mempool.pending_transaction_record.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disk_storage_used', full_name='koinos.mempool.pending_transaction_record.disk_storage_used', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_bandwidth_used', full_name='koinos.mempool.pending_transaction_record.network_bandwidth_used', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_bandwidth_used', full_name='koinos.mempool.pending_transaction_record.compute_bandwidth_used', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=181,
  serialized_end=370,
)

_PENDING_TRANSACTION_RECORD.fields_by_name['transaction'].message_type = koinos_dot_protocol_dot_protocol__pb2._TRANSACTION
DESCRIPTOR.message_types_by_name['mempool_metadata'] = _MEMPOOL_METADATA
DESCRIPTOR.message_types_by_name['address_resource_record'] = _ADDRESS_RESOURCE_RECORD
DESCRIPTOR.message_types_by_name['pending_transaction_record'] = _PENDING_TRANSACTION_RECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

mempool_metadata = _reflection.GeneratedProtocolMessageType('mempool_metadata', (_message.Message,), {
  'DESCRIPTOR' : _MEMPOOL_METADATA,
  '__module__' : 'koinos.mempool.mempool_pb2'
  # @@protoc_insertion_point(class_scope:koinos.mempool.mempool_metadata)
  })
_sym_db.RegisterMessage(mempool_metadata)

address_resource_record = _reflection.GeneratedProtocolMessageType('address_resource_record', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS_RESOURCE_RECORD,
  '__module__' : 'koinos.mempool.mempool_pb2'
  # @@protoc_insertion_point(class_scope:koinos.mempool.address_resource_record)
  })
_sym_db.RegisterMessage(address_resource_record)

pending_transaction_record = _reflection.GeneratedProtocolMessageType('pending_transaction_record', (_message.Message,), {
  'DESCRIPTOR' : _PENDING_TRANSACTION_RECORD,
  '__module__' : 'koinos.mempool.mempool_pb2'
  # @@protoc_insertion_point(class_scope:koinos.mempool.pending_transaction_record)
  })
_sym_db.RegisterMessage(pending_transaction_record)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)