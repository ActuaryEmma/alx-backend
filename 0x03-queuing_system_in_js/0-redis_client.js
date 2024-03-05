const redis = require("redis");
const client = redis.createClient();

(async () => {
	await client.connect();
})();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});
