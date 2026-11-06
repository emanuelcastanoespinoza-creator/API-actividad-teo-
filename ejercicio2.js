const express = require('express');
const app = express();
app.use(express.json());

app.get('/productos', (req, res) => {
    res.json({ success: true, data: [] });
});

app.post('/productos', (req, res) => {
    const { nombre } = req.body;
    res.status(201).json({ success: true, data: { nombre } });
});

app.get('/productos/:id', (req, res) => {
    const id = req.params.id;
    res.json({ success: true, data: { id } });
});

app.listen(3000);

