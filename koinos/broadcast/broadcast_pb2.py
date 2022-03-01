# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/broadcast/broadcast.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import common_pb2 as koinos_dot_common__pb2
from koinos import options_pb2 as koinos_dot_options__pb2
from koinos.protocol import protocol_pb2 as koinos_dot_protocol_dot_protocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/broadcast/broadcast.proto',
  package='koinos.broadcast',
  syntax='proto3',
  serialized_options=b'Z6github.com/koinos/koinos-proto-golang/koinos/broadcast',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n koinos/broadcast/broadcast.proto\x12\x10koinos.broadcast\x1a\x13koinos/common.proto\x1a\x14koinos/options.proto\x1a\x1ekoinos/protocol/protocol.proto\"\x94\x01\n\x14transaction_accepted\x12\x31\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1c.koinos.protocol.transaction\x12\x35\n\x07receipt\x18\x02 \x01(\x0b\x32$.koinos.protocol.transaction_receipt\x12\x12\n\x06height\x18\x03 \x01(\x04\x42\x02\x30\x01\"&\n\x12transaction_failed\x12\x10\n\x02id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\"v\n\x0e\x62lock_accepted\x12%\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x16.koinos.protocol.block\x12/\n\x07receipt\x18\x02 \x01(\x0b\x32\x1e.koinos.protocol.block_receipt\x12\x0c\n\x04live\x18\x03 \x01(\x08\">\n\x12\x62lock_irreversible\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.koinos.block_topology\"l\n\nfork_heads\x12\x37\n\x17last_irreversible_block\x18\x01 \x01(\x0b\x32\x16.koinos.block_topology\x12%\n\x05heads\x18\x02 \x03(\x0b\x32\x16.koinos.block_topology\" \n\rgossip_status\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\x98\x01\n\x0c\x65vent_parcel\x12\x16\n\x08\x62lock_id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x03\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12!\n\x0etransaction_id\x18\x03 \x01(\x0c\x42\x04\x80\xb5\x18\x04H\x00\x88\x01\x01\x12*\n\x05\x65vent\x18\x04 \x01(\x0b\x32\x1b.koinos.protocol.event_dataB\x11\n\x0f_transaction_idB8Z6github.com/koinos/koinos-proto-golang/koinos/broadcastb\x06proto3'
  ,
  dependencies=[koinos_dot_common__pb2.DESCRIPTOR,koinos_dot_options__pb2.DESCRIPTOR,koinos_dot_protocol_dot_protocol__pb2.DESCRIPTOR,])




_TRANSACTION_ACCEPTED = _descriptor.Descriptor(
  name='transaction_accepted',
  full_name='koinos.broadcast.transaction_accepted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='koinos.broadcast.transaction_accepted.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='koinos.broadcast.transaction_accepted.receipt', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='koinos.broadcast.transaction_accepted.height', index=2,
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
  serialized_start=130,
  serialized_end=278,
)


_TRANSACTION_FAILED = _descriptor.Descriptor(
  name='transaction_failed',
  full_name='koinos.broadcast.transaction_failed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='koinos.broadcast.transaction_failed.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=280,
  serialized_end=318,
)


_BLOCK_ACCEPTED = _descriptor.Descriptor(
  name='block_accepted',
  full_name='koinos.broadcast.block_accepted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='koinos.broadcast.block_accepted.block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='koinos.broadcast.block_accepted.receipt', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='live', full_name='koinos.broadcast.block_accepted.live', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=320,
  serialized_end=438,
)


_BLOCK_IRREVERSIBLE = _descriptor.Descriptor(
  name='block_irreversible',
  full_name='koinos.broadcast.block_irreversible',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topology', full_name='koinos.broadcast.block_irreversible.topology', index=0,
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
  serialized_start=440,
  serialized_end=502,
)


_FORK_HEADS = _descriptor.Descriptor(
  name='fork_heads',
  full_name='koinos.broadcast.fork_heads',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_irreversible_block', full_name='koinos.broadcast.fork_heads.last_irreversible_block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heads', full_name='koinos.broadcast.fork_heads.heads', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=504,
  serialized_end=612,
)


_GOSSIP_STATUS = _descriptor.Descriptor(
  name='gossip_status',
  full_name='koinos.broadcast.gossip_status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='koinos.broadcast.gossip_status.enabled', index=0,
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
  serialized_start=614,
  serialized_end=646,
)


_EVENT_PARCEL = _descriptor.Descriptor(
  name='event_parcel',
  full_name='koinos.broadcast.event_parcel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='koinos.broadcast.event_parcel.block_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='koinos.broadcast.event_parcel.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='koinos.broadcast.event_parcel.transaction_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='koinos.broadcast.event_parcel.event', index=3,
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
    _descriptor.OneofDescriptor(
      name='_transaction_id', full_name='koinos.broadcast.event_parcel._transaction_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=649,
  serialized_end=801,
)

_TRANSACTION_ACCEPTED.fields_by_name['transaction'].message_type = koinos_dot_protocol_dot_protocol__pb2._TRANSACTION
_TRANSACTION_ACCEPTED.fields_by_name['receipt'].message_type = koinos_dot_protocol_dot_protocol__pb2._TRANSACTION_RECEIPT
_BLOCK_ACCEPTED.fields_by_name['block'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK
_BLOCK_ACCEPTED.fields_by_name['receipt'].message_type = koinos_dot_protocol_dot_protocol__pb2._BLOCK_RECEIPT
_BLOCK_IRREVERSIBLE.fields_by_name['topology'].message_type = koinos_dot_common__pb2._BLOCK_TOPOLOGY
_FORK_HEADS.fields_by_name['last_irreversible_block'].message_type = koinos_dot_common__pb2._BLOCK_TOPOLOGY
_FORK_HEADS.fields_by_name['heads'].message_type = koinos_dot_common__pb2._BLOCK_TOPOLOGY
_EVENT_PARCEL.fields_by_name['event'].message_type = koinos_dot_protocol_dot_protocol__pb2._EVENT_DATA
_EVENT_PARCEL.oneofs_by_name['_transaction_id'].fields.append(
  _EVENT_PARCEL.fields_by_name['transaction_id'])
_EVENT_PARCEL.fields_by_name['transaction_id'].containing_oneof = _EVENT_PARCEL.oneofs_by_name['_transaction_id']
DESCRIPTOR.message_types_by_name['transaction_accepted'] = _TRANSACTION_ACCEPTED
DESCRIPTOR.message_types_by_name['transaction_failed'] = _TRANSACTION_FAILED
DESCRIPTOR.message_types_by_name['block_accepted'] = _BLOCK_ACCEPTED
DESCRIPTOR.message_types_by_name['block_irreversible'] = _BLOCK_IRREVERSIBLE
DESCRIPTOR.message_types_by_name['fork_heads'] = _FORK_HEADS
DESCRIPTOR.message_types_by_name['gossip_status'] = _GOSSIP_STATUS
DESCRIPTOR.message_types_by_name['event_parcel'] = _EVENT_PARCEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

transaction_accepted = _reflection.GeneratedProtocolMessageType('transaction_accepted', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION_ACCEPTED,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.transaction_accepted)
  })
_sym_db.RegisterMessage(transaction_accepted)

transaction_failed = _reflection.GeneratedProtocolMessageType('transaction_failed', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION_FAILED,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.transaction_failed)
  })
_sym_db.RegisterMessage(transaction_failed)

block_accepted = _reflection.GeneratedProtocolMessageType('block_accepted', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK_ACCEPTED,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.block_accepted)
  })
_sym_db.RegisterMessage(block_accepted)

block_irreversible = _reflection.GeneratedProtocolMessageType('block_irreversible', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK_IRREVERSIBLE,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.block_irreversible)
  })
_sym_db.RegisterMessage(block_irreversible)

fork_heads = _reflection.GeneratedProtocolMessageType('fork_heads', (_message.Message,), {
  'DESCRIPTOR' : _FORK_HEADS,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.fork_heads)
  })
_sym_db.RegisterMessage(fork_heads)

gossip_status = _reflection.GeneratedProtocolMessageType('gossip_status', (_message.Message,), {
  'DESCRIPTOR' : _GOSSIP_STATUS,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.gossip_status)
  })
_sym_db.RegisterMessage(gossip_status)

event_parcel = _reflection.GeneratedProtocolMessageType('event_parcel', (_message.Message,), {
  'DESCRIPTOR' : _EVENT_PARCEL,
  '__module__' : 'koinos.broadcast.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:koinos.broadcast.event_parcel)
  })
_sym_db.RegisterMessage(event_parcel)


DESCRIPTOR._options = None
_TRANSACTION_ACCEPTED.fields_by_name['height']._options = None
_TRANSACTION_FAILED.fields_by_name['id']._options = None
_EVENT_PARCEL.fields_by_name['block_id']._options = None
_EVENT_PARCEL.fields_by_name['transaction_id']._options = None
# @@protoc_insertion_point(module_scope)
