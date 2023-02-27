# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openapiv3/annotations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openapiv3 import OpenAPIv3_pb2 as openapiv3_dot_OpenAPIv3__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='openapiv3/annotations.proto',
  package='openapi.v3',
  syntax='proto3',
  serialized_options=b'\n\016org.openapi_v3B\020AnnotationsProtoP\001Z.github.com/google/gnostic/openapiv3;openapi_v3\242\002\003OAS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bopenapiv3/annotations.proto\x12\nopenapi.v3\x1a\x19openapiv3/OpenAPIv3.proto\x1a google/protobuf/descriptor.proto:E\n\x08\x64ocument\x12\x1c.google.protobuf.FileOptions\x18\xf7\x08 \x01(\x0b\x32\x14.openapi.v3.Document:I\n\toperation\x12\x1e.google.protobuf.MethodOptions\x18\xf7\x08 \x01(\x0b\x32\x15.openapi.v3.Operation:D\n\x06schema\x12\x1f.google.protobuf.MessageOptions\x18\xf7\x08 \x01(\x0b\x32\x12.openapi.v3.Schema:D\n\x08property\x12\x1d.google.protobuf.FieldOptions\x18\xf7\x08 \x01(\x0b\x32\x12.openapi.v3.SchemaBZ\n\x0eorg.openapi_v3B\x10\x41nnotationsProtoP\x01Z.github.com/google/gnostic/openapiv3;openapi_v3\xa2\x02\x03OASb\x06proto3'
  ,
  dependencies=[openapiv3_dot_OpenAPIv3__pb2.DESCRIPTOR,google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


DOCUMENT_FIELD_NUMBER = 1143
document = _descriptor.FieldDescriptor(
  name='document', full_name='openapi.v3.document', index=0,
  number=1143, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
OPERATION_FIELD_NUMBER = 1143
operation = _descriptor.FieldDescriptor(
  name='operation', full_name='openapi.v3.operation', index=1,
  number=1143, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SCHEMA_FIELD_NUMBER = 1143
schema = _descriptor.FieldDescriptor(
  name='schema', full_name='openapi.v3.schema', index=2,
  number=1143, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
PROPERTY_FIELD_NUMBER = 1143
property = _descriptor.FieldDescriptor(
  name='property', full_name='openapi.v3.property', index=3,
  number=1143, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['document'] = document
DESCRIPTOR.extensions_by_name['operation'] = operation
DESCRIPTOR.extensions_by_name['schema'] = schema
DESCRIPTOR.extensions_by_name['property'] = property
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

document.message_type = openapiv3_dot_OpenAPIv3__pb2._DOCUMENT
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(document)
operation.message_type = openapiv3_dot_OpenAPIv3__pb2._OPERATION
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(operation)
schema.message_type = openapiv3_dot_OpenAPIv3__pb2._SCHEMA
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(schema)
property.message_type = openapiv3_dot_OpenAPIv3__pb2._SCHEMA
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(property)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)