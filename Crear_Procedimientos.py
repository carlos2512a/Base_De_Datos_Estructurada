1. Ejercicios Prácticos
--Crear un procedimiento insertar_departamento que valide duplicados
antes de insertar.

CREATE OR REPLACE PROCEDURE insertar_departamento (
 p_id_dpto     NUMBER,
 p_nom_dpto    VARCHAR2
)
IS
    v_existe_dpto NUMBER;
BEGIN
    
    SELECT COUNT(*) 
    INTO v_existe_dpto 
    FROM departamento 
    WHERE UPPER(nom_dpto) = UPPER(p_nom_dpto);

    IF v_existe_dpto > 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'El departamento ya existe.');
    ELSE
        
        INSERT INTO departamento (id_dpto, nom_dpto)
        VALUES (p_id_dpto, p_nom_dpto);

        DBMS_OUTPUT.PUT_LINE('Departamento insertado correctamente.');
    END IF;

EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        DBMS_OUTPUT.PUT_LINE('Error: ya existe un departamento con el mismo ID.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/

2. Crear un procedimiento eliminar_empleado que elimine por ID y
verifique su existencia.

CREATE OR REPLACE PROCEDURE eliminar_empleado (
    p_id_emp NUMBER
)
IS
    v_existe_emp NUMBER;
BEGIN
    
    SELECT COUNT(*) 
    INTO v_existe_emp 
    FROM empleado 
    WHERE id_emp = p_id_emp;

    IF v_existe_emp = 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'El empleado con el ID especificado no existe.');
    ELSE
        
        DELETE FROM empleado 
        WHERE id_emp = p_id_emp;

        DBMS_OUTPUT.PUT_LINE('Empleado eliminado correctamente.');
    END IF;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Error: No se encontró el empleado con ese ID.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/


3. Crear un procedimiento aumentar_sueldo_por_departamento que
incremente sueldos por porcentaje de un 3%

CREATE OR REPLACE PROCEDURE aumentar_sueldo_por_departamento (
    p_id_dpto NUMBER
)
IS
    v_existe_dpto NUMBER;
    v_existen_empleados NUMBER;
BEGIN
    
    SELECT COUNT(*) 
    INTO v_existe_dpto 
    FROM departamento 
    WHERE id_dpto = p_id_dpto;

    IF v_existe_dpto = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El departamento especificado no existe.');
    END IF;

    
    SELECT COUNT(*) 
    INTO v_existen_empleados 
    FROM empleado 
    WHERE departamento_id_dpto = p_id_dpto;

    IF v_existen_empleados = 0 THEN
        DBMS_OUTPUT.PUT_LINE('No hay empleados en este departamento. No se realizó ningún cambio.');
        RETURN;
    END IF;

    
    UPDATE empleado
    SET sueld_emp = sueld_emp * 1.03
    WHERE departamento_id_dpto = p_id_dpto;

    DBMS_OUTPUT.PUT_LINE('Se ha incrementado el sueldo de los empleados en un 3% para el departamento ID: ' || p_id_dpto);

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/



4. Crear un procedimiento mostrar_empleados_comuna que liste
empleados de una comuna.

CREATE OR REPLACE PROCEDURE mostrar_empleados_comuna (
    p_nom_com VARCHAR2
)
IS
    v_existe_comuna NUMBER;
BEGIN
    
    SELECT COUNT(*) 
    INTO v_existe_comuna 
    FROM comuna 
    WHERE UPPER(nom_com) = UPPER(p_nom_com);

    IF v_existe_comuna = 0 THEN
        RAISE_APPLICATION_ERROR(-20005, 'La comuna especificada no existe.');
    END IF;

    
    DBMS_OUTPUT.PUT_LINE('Empleados que pertenecen a la comuna: ' || UPPER(p_nom_com));
    DBMS_OUTPUT.PUT_LINE('-------------------------------------------');

    FOR emp IN (
        SELECT e.id_emp, e.nom_emp, e.ape_emp, e.sueld_emp, c.nom_com
        FROM empleado e
        JOIN comuna c ON e.comuna_cod_com = c.cod_com
        WHERE UPPER(c.nom_com) = UPPER(p_nom_com)
    )
    LOOP
        DBMS_OUTPUT.PUT_LINE(
            'ID: ' || emp.id_emp || ' | ' ||
            'Nombre: ' || emp.nom_emp || ' ' || emp.ape_emp || ' | ' ||
            'Sueldo: ' || emp.sueld_emp || ' | ' ||
            'Comuna: ' || emp.nom_com
        );
    END LOOP;

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/






5. Crear un procedimiento contar_empleados_por_cargo que muestre el
total por cargo.


CREATE OR REPLACE PROCEDURE contar_empleados_por_cargo
IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('Cantidad de empleados por cargo:');
    DBMS_OUTPUT.PUT_LINE('--------------------------------');

    FOR reg IN (
        SELECT c.nom_cargo AS nom_cargo,
               COUNT(e.id_emp) AS total_empleados
        FROM cargo c
        LEFT JOIN empleado e ON c.id_cargo = e.cargo_id_cargo
        GROUP BY c.nom_cargo
        ORDER BY total_empleados DESC
    )
    LOOP
        DBMS_OUTPUT.PUT_LINE(
            'Cargo: ' || reg.nom_cargo || 
            ' | Total empleados: ' || reg.total_empleados
        );
    END LOOP;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
