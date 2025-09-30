1. Evaluación final (3 ejercicios) - 
-De la tabla EMPLEADOS, mostrar el nombre completo (nombre + apellido 
en minúsculas).

SELECT LOWER(NOM_EMP), LOWER(APE_EMP) FROM EMPLEADO 
ORDER BY APE_EMP ASC;
 
-Obtener el número de meses transcurridos desde la fecha de 
contratación hasta hoy para cada empleado.
 
SELECT NOM_EMP,APE_EMP,FECHACONT_EMP,
FLOOR(MONTHS_BETWEEN(SYSDATE, FECHACONT_EMP)) AS meses_transcurridos
FROM EMPLEADO;



-Mostrar la fecha actual (SYSDATE), la fecha del próximo viernes
SELECT SYSDATE AS fecha_hoy,
       NEXT_DAY(SYSDATE, 'VIERNES') AS proximo_viernes,
       FROM dual;
-Mostrar el último día del mes actual. 

SELECT LAST_DAY(SYSDATE) AS fin_mes FROM dual; 


2. Mostrar el nombre de cada empleado en mayúsculas de la tabla EMPLEADO.
SELECT UPPER(NOM_EMP) AS NOMBRE, UPPER(APE_EMP) AS APELLIDO  
FROM EMPLEADO 
ORDER BY APE_EMP ASC; 

 
Divida le sueldo por 7 y redondéelo con 2 decimales de la tabla EMPLEADO,
muestre el sueldo divido en 7 y en redondeado con 2 decimales.

SELECT NOM_EMP,(SUELD_EMP/0.7) AS SUELDO_dividido, 
ROUND((SUELD_EMP/0.7),2) AS SUELDO_redondeado 
FROM EMPLEADO; 


 
Convertir la fecha de contratación (FECHACONT_EMP) al formato YYYY/MM/DD
SELECT NOM_EMP, 
       TO_CHAR(FECHACONT_EMP, 'YYYY/MM/DD') AS fecha_contratacion
FROM EMPLEADO;
