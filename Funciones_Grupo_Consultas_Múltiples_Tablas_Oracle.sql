1.#Mostrar el sueldo promedio por comuna.
SELECT COMUNA_COD_COM,ROUND(AVG(SUELD_EMP),2)AS SUELDO_PROMEDIO_TOTAL
FROM EMPLEADO
GROUP BY COMUNA_COD_COM
ORDER BY COMUNA_COD_COM;


2.# Listar la cantidad de empleados por cargo y el sueldo máximo dentro de
cada cargo.

SELECT CARGO_ID_CARGO, COUNT(EMPLEADO.ID_EMP) AS cantidad_empleados,MAX(SUELD_EMP) AS SUELDO_MAXIMO
FROM CARGO
JOIN EMPLEADO
ON CARGO_ID_CARGO = CARGO.ID_CARGO
GROUP BY CARGO_ID_CARGO
order by CARGO_ID_CARGO;

3.#Usar UNION para mostrar todos los nombres (empleados y
departamentos) en una sola lista.

SELECT NOM_EMP AS NOMBRE_COMPLETO
FROM EMPLEADO 
UNION
SELECT NOM_COM AS NOMBRE_COMPLETO
FROM COMUNA;

4#Obtener el total de sueldos por departamento y ordenarlos de mayor a
menor.

SELECT d.NOM_DPTO,SUM(e.SUELD_EMP) AS total_sueldos
FROM   DEPARTAMENTO d
JOIN   EMPLEADO e
ON e.DEPARTAMENTO_ID_DPTO = d.ID_DPTO
GROUP BY d.NOM_DPTO
ORDER BY total_sueldos DESC;

5#Listar a todos los empleados que fueron contratados después del día 10
de marzo.

SELECT e.NOM_EMP,e.APE_EMP,e.FECHACONT_EMP
FROM   EMPLEADO e
WHERE  e.FECHACONT_EMP > DATE '1993-03-10'   
ORDER BY e.FECHACONT_EMP;

6#Listar a todos los empleados, nombre, apellido con su fecha de
contratación usando el siguiente formato 'DD "de" Month, YYYY'

SELECT e.NOM_EMP,e.APE_EMP,
TO_CHAR(e.FECHACONT_EMP, 'DD "de" Month, YYYY') AS FECHA_CONTRATACION
FROM EMPLEADO e
ORDER BY e.NOM_EMP, e.APE_EMP;



