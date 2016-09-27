# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha.proto',
  package='voltha',
  syntax='proto3',
  serialized_pb=_b('\n\x0cvoltha.proto\x12\x06voltha\x1a\x1cgoogle/api/annotations.proto\"\r\n\x0bNullMessage\"v\n\x0cHealthStatus\x12/\n\x05state\x18\x01 \x01(\x0e\x32 .voltha.HealthStatus.HealthState\"5\n\x0bHealthState\x12\x0b\n\x07HEALTHY\x10\x00\x12\x0e\n\nOVERLOADED\x10\x01\x12\t\n\x05\x44YING\x10\x02\"q\n\x07\x41\x64\x64ress\x12\n\n\x02id\x18\x07 \x01(\t\x12\x0e\n\x06street\x18\x01 \x01(\t\x12\x0f\n\x07street2\x18\x02 \x01(\t\x12\x0f\n\x07street3\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0b\n\x03zip\x18\x06 \x01(\r\"/\n\tAddresses\x12\"\n\taddresses\x18\x01 \x03(\x0b\x32\x0f.voltha.Address\"\x9f\x01\n\x0bMoreComplex\x12$\n\x06health\x18\x01 \x01(\x0b\x32\x14.voltha.HealthStatus\x12\x13\n\x0b\x66oo_counter\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12%\n\x08\x63hildren\x18\x04 \x03(\x0b\x32\x13.voltha.MoreComplex\x12 \n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32\x0f.voltha.Address\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\t2a\n\rHealthService\x12P\n\x0fGetHealthStatus\x12\x13.voltha.NullMessage\x1a\x14.voltha.HealthStatus\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\x07/health:\x01*2\xb6\x02\n\x0e\x45xampleService\x12K\n\rListAddresses\x12\x13.voltha.NullMessage\x1a\x11.voltha.Addresses\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/addresses\x12\x42\n\nGetAddress\x12\n.voltha.ID\x1a\x0f.voltha.Address\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/addresses/{id}\x12H\n\rCreateAddress\x12\x0f.voltha.Address\x1a\x0f.voltha.Address\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/addresses:\x01*\x12I\n\rDeleteAddress\x12\n.voltha.ID\x1a\x13.voltha.NullMessage\"\x17\x82\xd3\xe4\x93\x02\x11*\x0f/addresses/{id}B<\n\x13org.opencord.volthaB\x0cVolthaProtos\xaa\x02\x16Opencord.Voltha.Volthab\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HEALTHSTATUS_HEALTHSTATE = _descriptor.EnumDescriptor(
  name='HealthState',
  full_name='voltha.HealthStatus.HealthState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTHY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLOADED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=187,
)
_sym_db.RegisterEnumDescriptor(_HEALTHSTATUS_HEALTHSTATE)


_NULLMESSAGE = _descriptor.Descriptor(
  name='NullMessage',
  full_name='voltha.NullMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=67,
)


_HEALTHSTATUS = _descriptor.Descriptor(
  name='HealthStatus',
  full_name='voltha.HealthStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='voltha.HealthStatus.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEALTHSTATUS_HEALTHSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=187,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='voltha.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='voltha.Address.id', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='street', full_name='voltha.Address.street', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='street2', full_name='voltha.Address.street2', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='street3', full_name='voltha.Address.street3', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='voltha.Address.city', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='voltha.Address.state', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zip', full_name='voltha.Address.zip', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=302,
)


_ADDRESSES = _descriptor.Descriptor(
  name='Addresses',
  full_name='voltha.Addresses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='voltha.Addresses.addresses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=351,
)


_MORECOMPLEX = _descriptor.Descriptor(
  name='MoreComplex',
  full_name='voltha.MoreComplex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health', full_name='voltha.MoreComplex.health', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='foo_counter', full_name='voltha.MoreComplex.foo_counter', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='voltha.MoreComplex.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='children', full_name='voltha.MoreComplex.children', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='voltha.MoreComplex.address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=513,
)


_ID = _descriptor.Descriptor(
  name='ID',
  full_name='voltha.ID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='voltha.ID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=531,
)

_HEALTHSTATUS.fields_by_name['state'].enum_type = _HEALTHSTATUS_HEALTHSTATE
_HEALTHSTATUS_HEALTHSTATE.containing_type = _HEALTHSTATUS
_ADDRESSES.fields_by_name['addresses'].message_type = _ADDRESS
_MORECOMPLEX.fields_by_name['health'].message_type = _HEALTHSTATUS
_MORECOMPLEX.fields_by_name['children'].message_type = _MORECOMPLEX
_MORECOMPLEX.fields_by_name['address'].message_type = _ADDRESS
DESCRIPTOR.message_types_by_name['NullMessage'] = _NULLMESSAGE
DESCRIPTOR.message_types_by_name['HealthStatus'] = _HEALTHSTATUS
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['Addresses'] = _ADDRESSES
DESCRIPTOR.message_types_by_name['MoreComplex'] = _MORECOMPLEX
DESCRIPTOR.message_types_by_name['ID'] = _ID

NullMessage = _reflection.GeneratedProtocolMessageType('NullMessage', (_message.Message,), dict(
  DESCRIPTOR = _NULLMESSAGE,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.NullMessage)
  ))
_sym_db.RegisterMessage(NullMessage)

HealthStatus = _reflection.GeneratedProtocolMessageType('HealthStatus', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHSTATUS,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.HealthStatus)
  ))
_sym_db.RegisterMessage(HealthStatus)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.Address)
  ))
_sym_db.RegisterMessage(Address)

Addresses = _reflection.GeneratedProtocolMessageType('Addresses', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSES,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.Addresses)
  ))
_sym_db.RegisterMessage(Addresses)

MoreComplex = _reflection.GeneratedProtocolMessageType('MoreComplex', (_message.Message,), dict(
  DESCRIPTOR = _MORECOMPLEX,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.MoreComplex)
  ))
_sym_db.RegisterMessage(MoreComplex)

ID = _reflection.GeneratedProtocolMessageType('ID', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'voltha_pb2'
  # @@protoc_insertion_point(class_scope:voltha.ID)
  ))
_sym_db.RegisterMessage(ID)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023org.opencord.volthaB\014VolthaProtos\252\002\026Opencord.Voltha.Voltha'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class HealthServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetHealthStatus = channel.unary_unary(
        '/voltha.HealthService/GetHealthStatus',
        request_serializer=NullMessage.SerializeToString,
        response_deserializer=HealthStatus.FromString,
        )


class HealthServiceServicer(object):

  def GetHealthStatus(self, request, context):
    """Return current health status of a Voltha instance
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HealthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetHealthStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetHealthStatus,
          request_deserializer=NullMessage.FromString,
          response_serializer=HealthStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'voltha.HealthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaHealthServiceServicer(object):
  def GetHealthStatus(self, request, context):
    """Return current health status of a Voltha instance
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaHealthServiceStub(object):
  def GetHealthStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Return current health status of a Voltha instance
    """
    raise NotImplementedError()
  GetHealthStatus.future = None


def beta_create_HealthService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('voltha.HealthService', 'GetHealthStatus'): NullMessage.FromString,
  }
  response_serializers = {
    ('voltha.HealthService', 'GetHealthStatus'): HealthStatus.SerializeToString,
  }
  method_implementations = {
    ('voltha.HealthService', 'GetHealthStatus'): face_utilities.unary_unary_inline(servicer.GetHealthStatus),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_HealthService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('voltha.HealthService', 'GetHealthStatus'): NullMessage.SerializeToString,
  }
  response_deserializers = {
    ('voltha.HealthService', 'GetHealthStatus'): HealthStatus.FromString,
  }
  cardinalities = {
    'GetHealthStatus': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'voltha.HealthService', cardinalities, options=stub_options)


class ExampleServiceStub(object):
  """(placeholder) This is an example service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAddresses = channel.unary_unary(
        '/voltha.ExampleService/ListAddresses',
        request_serializer=NullMessage.SerializeToString,
        response_deserializer=Addresses.FromString,
        )
    self.GetAddress = channel.unary_unary(
        '/voltha.ExampleService/GetAddress',
        request_serializer=ID.SerializeToString,
        response_deserializer=Address.FromString,
        )
    self.CreateAddress = channel.unary_unary(
        '/voltha.ExampleService/CreateAddress',
        request_serializer=Address.SerializeToString,
        response_deserializer=Address.FromString,
        )
    self.DeleteAddress = channel.unary_unary(
        '/voltha.ExampleService/DeleteAddress',
        request_serializer=ID.SerializeToString,
        response_deserializer=NullMessage.FromString,
        )


class ExampleServiceServicer(object):
  """(placeholder) This is an example service
  """

  def ListAddresses(self, request, context):
    """Return a bit more complex objects
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddress(self, request, context):
    """Return an address by ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateAddress(self, request, context):
    """Create an address record
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAddress(self, request, context):
    """Delete an address record by ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExampleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAddresses': grpc.unary_unary_rpc_method_handler(
          servicer.ListAddresses,
          request_deserializer=NullMessage.FromString,
          response_serializer=Addresses.SerializeToString,
      ),
      'GetAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddress,
          request_deserializer=ID.FromString,
          response_serializer=Address.SerializeToString,
      ),
      'CreateAddress': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAddress,
          request_deserializer=Address.FromString,
          response_serializer=Address.SerializeToString,
      ),
      'DeleteAddress': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAddress,
          request_deserializer=ID.FromString,
          response_serializer=NullMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'voltha.ExampleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaExampleServiceServicer(object):
  """(placeholder) This is an example service
  """
  def ListAddresses(self, request, context):
    """Return a bit more complex objects
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetAddress(self, request, context):
    """Return an address by ID
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def CreateAddress(self, request, context):
    """Create an address record
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def DeleteAddress(self, request, context):
    """Delete an address record by ID
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaExampleServiceStub(object):
  """(placeholder) This is an example service
  """
  def ListAddresses(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Return a bit more complex objects
    """
    raise NotImplementedError()
  ListAddresses.future = None
  def GetAddress(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Return an address by ID
    """
    raise NotImplementedError()
  GetAddress.future = None
  def CreateAddress(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Create an address record
    """
    raise NotImplementedError()
  CreateAddress.future = None
  def DeleteAddress(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Delete an address record by ID
    """
    raise NotImplementedError()
  DeleteAddress.future = None


def beta_create_ExampleService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('voltha.ExampleService', 'CreateAddress'): Address.FromString,
    ('voltha.ExampleService', 'DeleteAddress'): ID.FromString,
    ('voltha.ExampleService', 'GetAddress'): ID.FromString,
    ('voltha.ExampleService', 'ListAddresses'): NullMessage.FromString,
  }
  response_serializers = {
    ('voltha.ExampleService', 'CreateAddress'): Address.SerializeToString,
    ('voltha.ExampleService', 'DeleteAddress'): NullMessage.SerializeToString,
    ('voltha.ExampleService', 'GetAddress'): Address.SerializeToString,
    ('voltha.ExampleService', 'ListAddresses'): Addresses.SerializeToString,
  }
  method_implementations = {
    ('voltha.ExampleService', 'CreateAddress'): face_utilities.unary_unary_inline(servicer.CreateAddress),
    ('voltha.ExampleService', 'DeleteAddress'): face_utilities.unary_unary_inline(servicer.DeleteAddress),
    ('voltha.ExampleService', 'GetAddress'): face_utilities.unary_unary_inline(servicer.GetAddress),
    ('voltha.ExampleService', 'ListAddresses'): face_utilities.unary_unary_inline(servicer.ListAddresses),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ExampleService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('voltha.ExampleService', 'CreateAddress'): Address.SerializeToString,
    ('voltha.ExampleService', 'DeleteAddress'): ID.SerializeToString,
    ('voltha.ExampleService', 'GetAddress'): ID.SerializeToString,
    ('voltha.ExampleService', 'ListAddresses'): NullMessage.SerializeToString,
  }
  response_deserializers = {
    ('voltha.ExampleService', 'CreateAddress'): Address.FromString,
    ('voltha.ExampleService', 'DeleteAddress'): NullMessage.FromString,
    ('voltha.ExampleService', 'GetAddress'): Address.FromString,
    ('voltha.ExampleService', 'ListAddresses'): Addresses.FromString,
  }
  cardinalities = {
    'CreateAddress': cardinality.Cardinality.UNARY_UNARY,
    'DeleteAddress': cardinality.Cardinality.UNARY_UNARY,
    'GetAddress': cardinality.Cardinality.UNARY_UNARY,
    'ListAddresses': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'voltha.ExampleService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
