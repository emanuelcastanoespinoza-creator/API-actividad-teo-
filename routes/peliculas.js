 const express = require('express');
const router = express.Router();

let peliculas = [
  { id: 1, titulo: 'Inception',    director: 'Nolan', anio: 2010, genero: 'Ciencia Ficcion' },
  { id: 2, titulo: 'Interstellar', director: 'Nolan', anio: 2014, genero: 'Ciencia Ficcion' },
  { id: 3, titulo: 'Parasite',     director: 'Bong',  anio: 2019, genero: 'Drama' },
];

// GET todas
router.get('/', (req, res) => {
  const { genero } = req.query;
  if (genero) {
    const filtradas = peliculas.filter(p => p.genero === genero);
    return res.json({ success: true, data: filtradas });
  }
  res.json({ success: true, data: peliculas });
});

// GET por ID
router.get('/:id', (req, res) => {
  const pelicula = peliculas.find(p => p.id === parseInt(req.params.id));
  if (!pelicula) return res.status(404).json({ success: false, mensaje: 'No encontrada' });
  res.json({ success: true, data: pelicula });
});

// POST crear
router.post('/', (req, res) => {
  const { titulo, director, anio, genero } = req.body;
  if (!titulo || !director || !anio) {
    return res.status(400).json({ success: false, mensaje: 'titulo, director y anio son obligatorios' });
  }
  const nueva = { id: peliculas.length + 1, titulo, director, anio, genero };
  peliculas.push(nueva);
  res.status(201).json({ success: true, data: nueva });
});

// PUT actualizar
router.put('/:id', (req, res) => {
  const index = peliculas.findIndex(p => p.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ success: false, mensaje: 'No encontrada' });
  peliculas[index] = { ...peliculas[index], ...req.body };
  res.json({ success: true, data: peliculas[index] });
});

// DELETE eliminar
router.delete('/:id', (req, res) => {
  const index = peliculas.findIndex(p => p.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ success: false, mensaje: 'No encontrada' });
  peliculas.splice(index, 1);
  res.json({ success: true, mensaje: 'Eliminada correctamente' });
});

module.exports = router;
