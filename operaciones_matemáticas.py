Taller final II unidad


Ejercicios de Subconsultas de una sola fila


1. Listar los empleados cuyo sueldo es menor o igual al sueldo promedio de todos los empleados. Use mascaras 

SELECT sueld_emp AS salario, ape_emp as apellido,
nom_emp as nombre
FROM empleado
WHERE sueld_emp < = (SELECT AVG(sueld_emp) FROM
empleado)
order by apellido asc;



2. Mostrar los empleados que ganan menos que el empleado 'DOROTEA LOPEZ'. Use mascaras


SELECT nom_emp AS nombre, ape_emp as apellido,
sueld_emp as salario
FROM empleado
WHERE sueld_emp > (
SELECT sueld_emp
FROM empleado
WHERE nom_emp = 'DOROTEA' AND ape_emp = 'LOPEZ'
)
order by apellido desc;

Ejercicios de Subconsultas de varias filas

3. Mostrar los empleados que tienen el mismo departamento que algún empleado del cargo operador.

SELECT nom_emp, ape_emp, nom_dpto,NOM_CARGO
FROM empleado
JOIN DEPARTAMENTO
ON empleado.DEPARTAMENTO_ID_DPTO=DEPARTAMENTO.ID_DPTO
join CARGO
on empleado.CARGO_ID_CARGO=CARGO.ID_CARGO
WHERE empleado.CARGO_ID_CARGO =1;

4. Listar empleados cuyo sueldo es mayor que todos los de la comuna el bosque

SELECT nom_emp, ape_emp, sueld_emp, nom_com
FROM empleado
join COMUNA
on empleado.COMUNA_COD_COM= COMUNA.COD_COM
WHERE sueld_emp > ALL (
SELECT  sueld_emp
FROM empleado
WHERE comuna_cod_com = '2'
);

Ejercicios con agrupamientos y operaciones matemáticas

5. Calcular el sueldo promedio de los empleados por comuna, cual comuna consume más?


SELECT comuna.nom_com,
ROUND(AVG(empleado.sueld_emp),2) AS promedio_sueldo
FROM empleado
JOIN comuna ON empleado.comuna_cod_com =
comuna.COD_COM
GROUP BY comuna.NOM_COM
ORDER BY promedio_sueldo DESC



6. Contar la cantidad de empleados por comuna, que comuna tiene más empleados 

SELECT comuna.nom_com, COUNT(empleado.id_emp) AS
cantidad_empleados
FROM empleado
JOIN COMUNA
ON empleado.COMUNA_COD_COM = COMUNA.COD_COM
GROUP BY comuna.nom_com
ORDER BY cantidad_empleados ASC;



7. Calcular el gasto total en sueldos por cargo. ¿Qué cargo consume más recursos?



SELECT cargo.nom_cargo, SUM(empleado.sueld_emp) AS
gasto_total
FROM empleado
JOIN CARGO ON empleado.cargo_id_cargo =cargo_id_cargo
GROUP BY cargo.nom_cargo
ORDER BY gasto_total ASC;



8. Mostrar el promedio de sueldos por departamento, solo si es inferior a $710.500

SELECT  departamento.nom_dpto, AVG(empleado.sueld_emp) AS
promedio_sueldo
FROM empleado
JOIN DEPARTAMENTO ON  empleado.departamento_id_dpto = departamento.id_dpto
GROUP BY  departamento.nom_dpto
HAVING AVG(empleado.sueld_emp) < 711500
ORDER BY promedio_sueldo DESC;



