// Node Redis client and basic operations

import { createClient, print } from 'redis';

const client = createClient();

async function nodeRedis() {
  try {
    await client.connect()
    console.log('Redis client connected to the server');
  } catch (error) {
    console.log('Redis client not connected to the server:', error);
  }
};


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
  const data = await client.get(schoolName);
  console.log(data);
};

nodeRedis()
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
