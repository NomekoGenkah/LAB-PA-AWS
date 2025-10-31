-- Connect to transparencia database
\c transparencia

-- Create the spending table
CREATE TABLE IF NOT EXISTS spending (
    id SERIAL PRIMARY KEY,
    anio VARCHAR(10),
    mes VARCHAR(50),
    estamento VARCHAR(100),
    nombre_completo VARCHAR(255),
    cargo VARCHAR(255),
    grado VARCHAR(50),
    calificacion VARCHAR(255),
    region VARCHAR(100),
    asignaciones_especiales TEXT,
    remuneracion_bruta VARCHAR(50),
    remuneracion_liquida VARCHAR(50),
    rem_adicionales VARCHAR(50),
    rem_bonos VARCHAR(50),
    derecho_horas_extra VARCHAR(10),
    horas_extra_diurnas VARCHAR(100),
    horas_extra_nocturnas VARCHAR(100),
    horas_extra_festivas VARCHAR(100),
    fecha_inicio VARCHAR(20),
    fecha_termino VARCHAR(50),
    observaciones TEXT,
    viaticos VARCHAR(50)
);

-- Create temporary table with all 22 columns (including the empty one from trailing semicolon)
CREATE TEMP TABLE temp_spending (
    anio TEXT,
    mes TEXT,
    estamento TEXT,
    nombre_completo TEXT,
    cargo TEXT,
    grado TEXT,
    calificacion TEXT,
    region TEXT,
    asignaciones_especiales TEXT,
    remuneracion_bruta TEXT,
    remuneracion_liquida TEXT,
    rem_adicionales TEXT,
    rem_bonos TEXT,
    derecho_horas_extra TEXT,
    horas_extra_diurnas TEXT,
    horas_extra_nocturnas TEXT,
    horas_extra_festivas TEXT,
    fecha_inicio TEXT,
    fecha_termino TEXT,
    observaciones TEXT,
    viaticos TEXT,
    empty_column TEXT
);

-- Import CSV data into temp table
\copy temp_spending FROM 'c:/Users/pedro/Desktop/LAB-PA-AWS/backend/Data.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'LATIN1', QUOTE '"');

-- Copy from temp table to spending table (excluding empty column)
INSERT INTO spending (anio, mes, estamento, nombre_completo, cargo, grado, calificacion, region, asignaciones_especiales, remuneracion_bruta, remuneracion_liquida, rem_adicionales, rem_bonos, derecho_horas_extra, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivas, fecha_inicio, fecha_termino, observaciones, viaticos)
SELECT anio, mes, estamento, nombre_completo, cargo, grado, calificacion, region, asignaciones_especiales, remuneracion_bruta, remuneracion_liquida, rem_adicionales, rem_bonos, derecho_horas_extra, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivas, fecha_inicio, fecha_termino, observaciones, viaticos
FROM temp_spending;

-- Show result
SELECT COUNT(*) as total_rows FROM spending;
