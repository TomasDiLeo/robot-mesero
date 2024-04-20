# robot-mesero

## Descripción

Este proyecto se centra en el desarrollo de un robot mesero básico, diseñado para operar de manera autónoma transportando y entregando alimentos en un entorno de restaurante o cafetería simulado. El objetivo es combinar el diseño mecánico, la navegación autónoma, la interfaz de usuario y la entrega de pedidos para crear un robot funcional y eficiente.

## Autores

- Tomás Di Leo
- Tomás Funes
- Ignacio Deichmann

## Institución

- Universidad Tres de Febrero
- Laboratorio de Microcontroladores
- Profesores: Jorge Fossati - Joaquín Moreno

## Fecha

- Abril 2024

## Tabla de Contenidos

- [Alcance del Proyecto](#alcance-del-proyecto)
- [Especificaciones de Hardware Mínimas](#especificaciones-de-hardware-mínimas)
- [Prestaciones de Hardware](#prestaciones-de-hardware)
- [Prestaciones de Software](#prestaciones-de-software)
- [Esquemas de Propuesta de Funcionamiento del Sistema](#esquemas-de-propuesta-de-funcionamiento-del-sistema)

## Alcance del Proyecto

El proyecto tiene como meta principal el diseño, construcción y programación de un robot mesero autónomo capaz de transportar y entregar alimentos dentro de un entorno controlado. Este robot contará con un diseño mecánico práctico, navegación autónoma, una interfaz de usuario intuitiva y un sistema de entrega de pedidos manual.

### Objetivos del Proyecto

- **Diseño Mecánico:** Desarrollar un chasis robusto y ligero con un centro de masa bajo y ruedas anchas para facilitar el movimiento y la estabilidad.
- **Navegación Autónoma:** Implementar algoritmos de navegación para detectar obstáculos, calcular rutas seguras y evitar colisiones.
- **Interfaz de Usuario:** Crear una interfaz intuitiva para la interacción entre el personal del restaurante y el robot, así como una señal sonora para indicar a los comensales que pueden retirar su pedido.
- **Entrega de Pedidos:** Limitada a una carga y descarga manual, enfocándose en el transporte de pedidos.

## Especificaciones de Hardware Mínimas

El hardware necesario para el funcionamiento del robot mesero incluye componentes como motores DC, una cámara ESP32, controlador ESP32, driver para los motores, sensor ultrasónico, batería de litio, botón pulsador y buzzer. Se proporcionan los precios y fuentes de los componentes para referencia.

## Prestaciones de Hardware

El sistema se basa en un microcontrolador que se conecta a una aplicación de control y maneja los motores y la detección de proximidad. El controlador de motor, el sensor ultrasónico y el módulo de cámara son componentes clave para la navegación y funcionamiento del robot.

## Prestaciones de Software

El software del robot gestiona la navegación utilizando datos de la cámara para ubicarse y calcular rutas hacia los objetivos. Además, maneja cambios en el entorno y la interacción con el usuario a través de un botón pulsador.

## Librerias y requisitos

El software debera tener compatibilidad con todos los sensores y hacer uso de distintos recursos para comunicarse con los sistemas y calcular caminos:
* #include "esp_camera.h"
* #include <WiFi.h>
* #include <ESPAsyncWebServer.h>
