SELECT 
    *
FROM livro
WHERE strftime('%Y', publicacao) > '2014'
ORDER BY cod;