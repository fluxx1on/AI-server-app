const { Mob, MobList, jspb } = require('./protojs/mobs_pb');

const mobMap = {}; // Локальная переменная для хранения мобов
const socket = new WebSocket('ws://127.0.0.1:8000/ws/updates/1');

socket.onopen = function() {
  console.log('WebSocket connection established.');
};

socket.onclose = function(event) {
  console.log('WebSocket connection closed with code:', event.code);
};

socket.onmessage = function(event) {
  const message = event.data;
  const bytes = new jspb.ByteSource(message);
  const mobList = MobList.deserializeBinary(bytes);


  mobList.getMobsList().forEach(function(mobMessage) {
    const id = mobMessage.getId();
    console.log(id);
    let existingMob = null;
    mobMap.forEach(function(mob) {
      if (mob.getId() == id) {
        existingMob = mob;
      }
    });

    if (existingMob != null) {
      existingMob.setHealth(mobMessage.getHealth());
      existingMob.setPositionX(mobMessage.getPositionX());
      existingMob.setPositionY(mobMessage.getPositionY());
      existingMob.setInBattle(mobMessage.getInBattle());
      existingMob.setParentId(mobMessage.getParentId());
    } else {
      mobMap.push(mobMessage);
    }
  });
};

socket.onerror = function(error) {
  console.error('WebSocket error:', error);
};