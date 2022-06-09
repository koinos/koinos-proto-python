# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinos/contracts/governance/governance.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from koinos import options_pb2 as koinos_dot_options__pb2
from koinos.protocol import protocol_pb2 as koinos_dot_protocol_dot_protocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='koinos/contracts/governance/governance.proto',
  package='koinos.contracts.governance',
  syntax='proto3',
  serialized_options=b'ZAgithub.com/koinos/koinos-proto-golang/koinos/contracts/governance',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,koinos/contracts/governance/governance.proto\x12\x1bkoinos.contracts.governance\x1a\x14koinos/options.proto\x1a\x1ekoinos/protocol/protocol.proto\"\xa7\x02\n\x0fproposal_record\x12.\n\noperations\x18\x01 \x03(\x0b\x32\x1a.koinos.protocol.operation\x12\x1d\n\x15operation_merkle_root\x18\x02 \x01(\x0c\x12\x19\n\x11vote_start_height\x18\x03 \x01(\x04\x12\x12\n\nvote_tally\x18\x04 \x01(\x04\x12\x16\n\x0evote_threshold\x18\x05 \x01(\x04\x12\x17\n\x0fshall_authorize\x18\x06 \x01(\x08\x12\x1a\n\x12updates_governance\x18\x07 \x01(\x08\x12<\n\x06status\x18\x08 \x01(\x0e\x32,.koinos.contracts.governance.proposal_status\x12\x0b\n\x03\x66\x65\x65\x18\t \x01(\x04\"w\n\x19submit_proposal_arguments\x12.\n\noperations\x18\x01 \x03(\x0b\x32\x1a.koinos.protocol.operation\x12\x1d\n\x15operation_merkle_root\x18\x02 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x03 \x01(\x04\"\x18\n\x16submit_proposal_result\"9\n\x1cget_proposal_by_id_arguments\x12\x19\n\x0bproposal_id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\"X\n\x19get_proposal_by_id_result\x12;\n\x05value\x18\x01 \x01(\x0b\x32,.koinos.contracts.governance.proposal_record\"\x8e\x01\n!get_proposals_by_status_arguments\x12\x1c\n\x0estart_proposal\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\x12\r\n\x05limit\x18\x02 \x01(\x04\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.koinos.contracts.governance.proposal_status\"]\n\x1eget_proposals_by_status_result\x12;\n\x05value\x18\x01 \x03(\x0b\x32,.koinos.contracts.governance.proposal_record\"F\n\x17get_proposals_arguments\x12\x1c\n\x0estart_proposal\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\x12\r\n\x05limit\x18\x02 \x01(\x04\"S\n\x14get_proposals_result\x12;\n\x05value\x18\x01 \x03(\x0b\x32,.koinos.contracts.governance.proposal_record\"[\n\x19proposal_submission_event\x12>\n\x08proposal\x18\x01 \x01(\x0b\x32,.koinos.contracts.governance.proposal_record\"g\n\x15proposal_status_event\x12\x10\n\x02id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\x12<\n\x06status\x18\x02 \x01(\x0e\x32,.koinos.contracts.governance.proposal_status\"S\n\x13proposal_vote_event\x12\x10\n\x02id\x18\x01 \x01(\x0c\x42\x04\x80\xb5\x18\x04\x12\x12\n\nvote_tally\x18\x02 \x01(\x04\x12\x16\n\x0evote_threshold\x18\x03 \x01(\x04*l\n\x0fproposal_status\x12\x0b\n\x07pending\x10\x00\x12\n\n\x06\x61\x63tive\x10\x01\x12\x0c\n\x08\x61pproved\x10\x02\x12\x0b\n\x07\x65xpired\x10\x03\x12\x0b\n\x07\x61pplied\x10\x04\x12\n\n\x06\x66\x61iled\x10\x05\x12\x0c\n\x08reverted\x10\x06\x42\x43ZAgithub.com/koinos/koinos-proto-golang/koinos/contracts/governanceb\x06proto3'
  ,
  dependencies=[koinos_dot_options__pb2.DESCRIPTOR,koinos_dot_protocol_dot_protocol__pb2.DESCRIPTOR,])

_PROPOSAL_STATUS = _descriptor.EnumDescriptor(
  name='proposal_status',
  full_name='koinos.contracts.governance.proposal_status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='pending', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='active', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='approved', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='expired', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='applied', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='failed', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='reverted', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1405,
  serialized_end=1513,
)
_sym_db.RegisterEnumDescriptor(_PROPOSAL_STATUS)

proposal_status = enum_type_wrapper.EnumTypeWrapper(_PROPOSAL_STATUS)
pending = 0
active = 1
approved = 2
expired = 3
applied = 4
failed = 5
reverted = 6



_PROPOSAL_RECORD = _descriptor.Descriptor(
  name='proposal_record',
  full_name='koinos.contracts.governance.proposal_record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='koinos.contracts.governance.proposal_record.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_merkle_root', full_name='koinos.contracts.governance.proposal_record.operation_merkle_root', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_start_height', full_name='koinos.contracts.governance.proposal_record.vote_start_height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_tally', full_name='koinos.contracts.governance.proposal_record.vote_tally', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_threshold', full_name='koinos.contracts.governance.proposal_record.vote_threshold', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shall_authorize', full_name='koinos.contracts.governance.proposal_record.shall_authorize', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updates_governance', full_name='koinos.contracts.governance.proposal_record.updates_governance', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='koinos.contracts.governance.proposal_record.status', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee', full_name='koinos.contracts.governance.proposal_record.fee', index=8,
      number=9, type=4, cpp_type=4, label=1,
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
  serialized_start=132,
  serialized_end=427,
)


_SUBMIT_PROPOSAL_ARGUMENTS = _descriptor.Descriptor(
  name='submit_proposal_arguments',
  full_name='koinos.contracts.governance.submit_proposal_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='koinos.contracts.governance.submit_proposal_arguments.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_merkle_root', full_name='koinos.contracts.governance.submit_proposal_arguments.operation_merkle_root', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee', full_name='koinos.contracts.governance.submit_proposal_arguments.fee', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=429,
  serialized_end=548,
)


_SUBMIT_PROPOSAL_RESULT = _descriptor.Descriptor(
  name='submit_proposal_result',
  full_name='koinos.contracts.governance.submit_proposal_result',
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
  serialized_start=550,
  serialized_end=574,
)


_GET_PROPOSAL_BY_ID_ARGUMENTS = _descriptor.Descriptor(
  name='get_proposal_by_id_arguments',
  full_name='koinos.contracts.governance.get_proposal_by_id_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='koinos.contracts.governance.get_proposal_by_id_arguments.proposal_id', index=0,
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
  serialized_start=576,
  serialized_end=633,
)


_GET_PROPOSAL_BY_ID_RESULT = _descriptor.Descriptor(
  name='get_proposal_by_id_result',
  full_name='koinos.contracts.governance.get_proposal_by_id_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.governance.get_proposal_by_id_result.value', index=0,
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
  serialized_start=635,
  serialized_end=723,
)


_GET_PROPOSALS_BY_STATUS_ARGUMENTS = _descriptor.Descriptor(
  name='get_proposals_by_status_arguments',
  full_name='koinos.contracts.governance.get_proposals_by_status_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_proposal', full_name='koinos.contracts.governance.get_proposals_by_status_arguments.start_proposal', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='koinos.contracts.governance.get_proposals_by_status_arguments.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='koinos.contracts.governance.get_proposals_by_status_arguments.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=726,
  serialized_end=868,
)


_GET_PROPOSALS_BY_STATUS_RESULT = _descriptor.Descriptor(
  name='get_proposals_by_status_result',
  full_name='koinos.contracts.governance.get_proposals_by_status_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.governance.get_proposals_by_status_result.value', index=0,
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
  serialized_start=870,
  serialized_end=963,
)


_GET_PROPOSALS_ARGUMENTS = _descriptor.Descriptor(
  name='get_proposals_arguments',
  full_name='koinos.contracts.governance.get_proposals_arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_proposal', full_name='koinos.contracts.governance.get_proposals_arguments.start_proposal', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='koinos.contracts.governance.get_proposals_arguments.limit', index=1,
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
  serialized_start=965,
  serialized_end=1035,
)


_GET_PROPOSALS_RESULT = _descriptor.Descriptor(
  name='get_proposals_result',
  full_name='koinos.contracts.governance.get_proposals_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='koinos.contracts.governance.get_proposals_result.value', index=0,
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
  serialized_start=1037,
  serialized_end=1120,
)


_PROPOSAL_SUBMISSION_EVENT = _descriptor.Descriptor(
  name='proposal_submission_event',
  full_name='koinos.contracts.governance.proposal_submission_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='koinos.contracts.governance.proposal_submission_event.proposal', index=0,
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
  serialized_start=1122,
  serialized_end=1213,
)


_PROPOSAL_STATUS_EVENT = _descriptor.Descriptor(
  name='proposal_status_event',
  full_name='koinos.contracts.governance.proposal_status_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='koinos.contracts.governance.proposal_status_event.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='koinos.contracts.governance.proposal_status_event.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1215,
  serialized_end=1318,
)


_PROPOSAL_VOTE_EVENT = _descriptor.Descriptor(
  name='proposal_vote_event',
  full_name='koinos.contracts.governance.proposal_vote_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='koinos.contracts.governance.proposal_vote_event.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_tally', full_name='koinos.contracts.governance.proposal_vote_event.vote_tally', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_threshold', full_name='koinos.contracts.governance.proposal_vote_event.vote_threshold', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=1320,
  serialized_end=1403,
)

_PROPOSAL_RECORD.fields_by_name['operations'].message_type = koinos_dot_protocol_dot_protocol__pb2._OPERATION
_PROPOSAL_RECORD.fields_by_name['status'].enum_type = _PROPOSAL_STATUS
_SUBMIT_PROPOSAL_ARGUMENTS.fields_by_name['operations'].message_type = koinos_dot_protocol_dot_protocol__pb2._OPERATION
_GET_PROPOSAL_BY_ID_RESULT.fields_by_name['value'].message_type = _PROPOSAL_RECORD
_GET_PROPOSALS_BY_STATUS_ARGUMENTS.fields_by_name['status'].enum_type = _PROPOSAL_STATUS
_GET_PROPOSALS_BY_STATUS_RESULT.fields_by_name['value'].message_type = _PROPOSAL_RECORD
_GET_PROPOSALS_RESULT.fields_by_name['value'].message_type = _PROPOSAL_RECORD
_PROPOSAL_SUBMISSION_EVENT.fields_by_name['proposal'].message_type = _PROPOSAL_RECORD
_PROPOSAL_STATUS_EVENT.fields_by_name['status'].enum_type = _PROPOSAL_STATUS
DESCRIPTOR.message_types_by_name['proposal_record'] = _PROPOSAL_RECORD
DESCRIPTOR.message_types_by_name['submit_proposal_arguments'] = _SUBMIT_PROPOSAL_ARGUMENTS
DESCRIPTOR.message_types_by_name['submit_proposal_result'] = _SUBMIT_PROPOSAL_RESULT
DESCRIPTOR.message_types_by_name['get_proposal_by_id_arguments'] = _GET_PROPOSAL_BY_ID_ARGUMENTS
DESCRIPTOR.message_types_by_name['get_proposal_by_id_result'] = _GET_PROPOSAL_BY_ID_RESULT
DESCRIPTOR.message_types_by_name['get_proposals_by_status_arguments'] = _GET_PROPOSALS_BY_STATUS_ARGUMENTS
DESCRIPTOR.message_types_by_name['get_proposals_by_status_result'] = _GET_PROPOSALS_BY_STATUS_RESULT
DESCRIPTOR.message_types_by_name['get_proposals_arguments'] = _GET_PROPOSALS_ARGUMENTS
DESCRIPTOR.message_types_by_name['get_proposals_result'] = _GET_PROPOSALS_RESULT
DESCRIPTOR.message_types_by_name['proposal_submission_event'] = _PROPOSAL_SUBMISSION_EVENT
DESCRIPTOR.message_types_by_name['proposal_status_event'] = _PROPOSAL_STATUS_EVENT
DESCRIPTOR.message_types_by_name['proposal_vote_event'] = _PROPOSAL_VOTE_EVENT
DESCRIPTOR.enum_types_by_name['proposal_status'] = _PROPOSAL_STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

proposal_record = _reflection.GeneratedProtocolMessageType('proposal_record', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL_RECORD,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.proposal_record)
  })
_sym_db.RegisterMessage(proposal_record)

submit_proposal_arguments = _reflection.GeneratedProtocolMessageType('submit_proposal_arguments', (_message.Message,), {
  'DESCRIPTOR' : _SUBMIT_PROPOSAL_ARGUMENTS,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.submit_proposal_arguments)
  })
_sym_db.RegisterMessage(submit_proposal_arguments)

submit_proposal_result = _reflection.GeneratedProtocolMessageType('submit_proposal_result', (_message.Message,), {
  'DESCRIPTOR' : _SUBMIT_PROPOSAL_RESULT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.submit_proposal_result)
  })
_sym_db.RegisterMessage(submit_proposal_result)

get_proposal_by_id_arguments = _reflection.GeneratedProtocolMessageType('get_proposal_by_id_arguments', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSAL_BY_ID_ARGUMENTS,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposal_by_id_arguments)
  })
_sym_db.RegisterMessage(get_proposal_by_id_arguments)

get_proposal_by_id_result = _reflection.GeneratedProtocolMessageType('get_proposal_by_id_result', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSAL_BY_ID_RESULT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposal_by_id_result)
  })
_sym_db.RegisterMessage(get_proposal_by_id_result)

get_proposals_by_status_arguments = _reflection.GeneratedProtocolMessageType('get_proposals_by_status_arguments', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSALS_BY_STATUS_ARGUMENTS,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposals_by_status_arguments)
  })
_sym_db.RegisterMessage(get_proposals_by_status_arguments)

get_proposals_by_status_result = _reflection.GeneratedProtocolMessageType('get_proposals_by_status_result', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSALS_BY_STATUS_RESULT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposals_by_status_result)
  })
_sym_db.RegisterMessage(get_proposals_by_status_result)

get_proposals_arguments = _reflection.GeneratedProtocolMessageType('get_proposals_arguments', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSALS_ARGUMENTS,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposals_arguments)
  })
_sym_db.RegisterMessage(get_proposals_arguments)

get_proposals_result = _reflection.GeneratedProtocolMessageType('get_proposals_result', (_message.Message,), {
  'DESCRIPTOR' : _GET_PROPOSALS_RESULT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.get_proposals_result)
  })
_sym_db.RegisterMessage(get_proposals_result)

proposal_submission_event = _reflection.GeneratedProtocolMessageType('proposal_submission_event', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL_SUBMISSION_EVENT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.proposal_submission_event)
  })
_sym_db.RegisterMessage(proposal_submission_event)

proposal_status_event = _reflection.GeneratedProtocolMessageType('proposal_status_event', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL_STATUS_EVENT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.proposal_status_event)
  })
_sym_db.RegisterMessage(proposal_status_event)

proposal_vote_event = _reflection.GeneratedProtocolMessageType('proposal_vote_event', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL_VOTE_EVENT,
  '__module__' : 'koinos.contracts.governance.governance_pb2'
  # @@protoc_insertion_point(class_scope:koinos.contracts.governance.proposal_vote_event)
  })
_sym_db.RegisterMessage(proposal_vote_event)


DESCRIPTOR._options = None
_GET_PROPOSAL_BY_ID_ARGUMENTS.fields_by_name['proposal_id']._options = None
_GET_PROPOSALS_BY_STATUS_ARGUMENTS.fields_by_name['start_proposal']._options = None
_GET_PROPOSALS_ARGUMENTS.fields_by_name['start_proposal']._options = None
_PROPOSAL_STATUS_EVENT.fields_by_name['id']._options = None
_PROPOSAL_VOTE_EVENT.fields_by_name['id']._options = None
# @@protoc_insertion_point(module_scope)
