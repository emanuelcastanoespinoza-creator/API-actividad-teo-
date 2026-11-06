const express = require('express');
const app = express();

app.use(express.json());

const peliculasRouter = require('./routes/peliculas');
app.use('/peliculas', peliculasRouter);

app.listen(3000, () => console.log('Servidor corriendo en puerto 3000'));