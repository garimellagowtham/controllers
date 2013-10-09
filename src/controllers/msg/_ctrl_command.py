"""autogenerated by genpy from controllers/ctrl_command.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ctrl_command(genpy.Message):
  _md5sum = "565f48a2a630e6ab6b4fb72196ae65ee"
  _type = "controllers/ctrl_command"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Roll in radians
float64 roll 
# Pitch in radians 
float64 pitch
# yaw rate in rad/s
float64 rateyaw
# Thrust normalized between thrustmin to thrustmax 
float64 thrust

"""
  __slots__ = ['roll','pitch','rateyaw','thrust']
  _slot_types = ['float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       roll,pitch,rateyaw,thrust

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ctrl_command, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.rateyaw is None:
        self.rateyaw = 0.
      if self.thrust is None:
        self.thrust = 0.
    else:
      self.roll = 0.
      self.pitch = 0.
      self.rateyaw = 0.
      self.thrust = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.roll, _x.pitch, _x.rateyaw, _x.thrust))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.roll, _x.pitch, _x.rateyaw, _x.thrust,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.roll, _x.pitch, _x.rateyaw, _x.thrust))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.roll, _x.pitch, _x.rateyaw, _x.thrust,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
