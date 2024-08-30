// Node Redis Client

import { createClient } from 'redis';

client = createClient();

async function nodeRedis() {
  try {
    await client.connect()
    console.log('Redis client connected to the server');
  } catch (error) {
    console.log('Redis client not connected to the server:', error);
  }
};

nodeRedis()
