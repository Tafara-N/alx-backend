// Node Redis client and advanced operations

import { createClient, redis } from 'redis';

async function runRedis() {
  const client = createClient();
  client.on('connect', () => console.log(`Redis client connected to the server`))
  client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
  await client.connect();

  client.hSet('HolbertonSchools',{
    'portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  });

  const allHolberton = await client.hGetAll('HolbertonSchools');
  console.log(allHolberton);
}

runRedis()
