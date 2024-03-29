// source: network_model/static/proto/mobs.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.Mob', null, global);
goog.exportSymbol('proto.MobList', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Mob = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Mob, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.Mob.displayName = 'proto.Mob';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.MobList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.MobList.repeatedFields_, null);
};
goog.inherits(proto.MobList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.MobList.displayName = 'proto.MobList';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Mob.prototype.toObject = function(opt_includeInstance) {
  return proto.Mob.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Mob} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Mob.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, 0),
    health: jspb.Message.getFieldWithDefault(msg, 2, 0),
    positionX: jspb.Message.getFieldWithDefault(msg, 3, 0),
    positionY: jspb.Message.getFieldWithDefault(msg, 4, 0),
    inBattle: jspb.Message.getBooleanFieldWithDefault(msg, 5, false),
    parentId: jspb.Message.getFieldWithDefault(msg, 6, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Mob}
 */
proto.Mob.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Mob;
  return proto.Mob.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Mob} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Mob}
 */
proto.Mob.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setHealth(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setPositionX(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setPositionY(value);
      break;
    case 5:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setInBattle(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setParentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Mob.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Mob.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Mob} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Mob.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f !== 0) {
    writer.writeInt32(
      1,
      f
    );
  }
  f = message.getHealth();
  if (f !== 0) {
    writer.writeInt32(
      2,
      f
    );
  }
  f = message.getPositionX();
  if (f !== 0) {
    writer.writeInt32(
      3,
      f
    );
  }
  f = message.getPositionY();
  if (f !== 0) {
    writer.writeInt32(
      4,
      f
    );
  }
  f = message.getInBattle();
  if (f) {
    writer.writeBool(
      5,
      f
    );
  }
  f = message.getParentId();
  if (f !== 0) {
    writer.writeInt32(
      6,
      f
    );
  }
};


/**
 * optional int32 id = 1;
 * @return {number}
 */
proto.Mob.prototype.getId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setId = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional int32 health = 2;
 * @return {number}
 */
proto.Mob.prototype.getHealth = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setHealth = function(value) {
  return jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional int32 position_x = 3;
 * @return {number}
 */
proto.Mob.prototype.getPositionX = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/**
 * @param {number} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setPositionX = function(value) {
  return jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional int32 position_y = 4;
 * @return {number}
 */
proto.Mob.prototype.getPositionY = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/**
 * @param {number} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setPositionY = function(value) {
  return jspb.Message.setProto3IntField(this, 4, value);
};


/**
 * optional bool in_battle = 5;
 * @return {boolean}
 */
proto.Mob.prototype.getInBattle = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 5, false));
};


/**
 * @param {boolean} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setInBattle = function(value) {
  return jspb.Message.setProto3BooleanField(this, 5, value);
};


/**
 * optional int32 parent_id = 6;
 * @return {number}
 */
proto.Mob.prototype.getParentId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/**
 * @param {number} value
 * @return {!proto.Mob} returns this
 */
proto.Mob.prototype.setParentId = function(value) {
  return jspb.Message.setProto3IntField(this, 6, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.MobList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.MobList.prototype.toObject = function(opt_includeInstance) {
  return proto.MobList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.MobList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.MobList.toObject = function(includeInstance, msg) {
  var f, obj = {
    mobsList: jspb.Message.toObjectList(msg.getMobsList(),
    proto.Mob.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.MobList}
 */
proto.MobList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.MobList;
  return proto.MobList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.MobList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.MobList}
 */
proto.MobList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.Mob;
      reader.readMessage(value,proto.Mob.deserializeBinaryFromReader);
      msg.addMobs(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.MobList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.MobList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.MobList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.MobList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getMobsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.Mob.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Mob mobs = 1;
 * @return {!Array<!proto.Mob>}
 */
proto.MobList.prototype.getMobsList = function() {
  return /** @type{!Array<!proto.Mob>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.Mob, 1));
};


/**
 * @param {!Array<!proto.Mob>} value
 * @return {!proto.MobList} returns this
*/
proto.MobList.prototype.setMobsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.Mob=} opt_value
 * @param {number=} opt_index
 * @return {!proto.Mob}
 */
proto.MobList.prototype.addMobs = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.Mob, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.MobList} returns this
 */
proto.MobList.prototype.clearMobsList = function() {
  return this.setMobsList([]);
};


goog.object.extend(exports, proto);
