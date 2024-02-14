const express = require('express');
require('dotenv').config()

const os = require('os');

const mysql = require('mysql2');

const pool = mysql.createPool({
  host: process.env.MYSQL_HOST || '172.20.112.1',
  user: process.env.MYSQL_USER || 'root',
  password: process.env.MYSQL_PASSWORD || 'root',
  database: process.env.MYSQL_DATABASE || 'seta',
  waitForConnections: true,
  connectionLimit: 10,
  maxIdle: 10,
  idleTimeout: 60000,
  queueLimit: 0,
  enableKeepAlive: true,
  keepAliveInitialDelay: 0,
});

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  const hostname = os.hostname();
  const date = new Date().toDateString();
  const ip = os.networkInterfaces().eth0[0].address;

  res.send({
    hostname,
    date,
    ip,
    env: process.env.NODE_ENV,
    MYSQL_HOST: process.env.MYSQL_HOST,
    MYSQL_USER: process.env.MYSQL_USER,
    MYSQL_PASSWORD: process.env.MYSQL_PASSWORD,
    MYSQL_DATABASE: process.env.MYSQL_DATABASE,
  });
});

app.get('/user', (req, res) => {
  pool.query('SELECT * FROM USER', (err, rows) => {
    if (err) throw err;
    res.send(rows);
  });
});

app.listen(process.env.PORT || 3000, () => {
  console.log('Listening on port 3000');
});
