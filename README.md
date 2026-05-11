# Has_guard
# HashGuard - File Integrity Monitor (FIM)

Protege tus archivos críticos contra modificaciones no autorizadas mediante criptografía SHA-256.

### 🛡️ Conceptos de Seguridad
- **Integridad:** Garantiza que los datos no han sido alterados.
- **SHA-256:** Algoritmo criptográfico utilizado para generar "huellas digitales" de archivos.
- **Hardenización:** Ideal para proteger scripts de producción y archivos de configuración.

### 🛠️ Flujo de Trabajo
1. **Inicialización:** Crea una base de datos del estado "limpio" del sistema.
2. **Verificación:** Detecta cualquier cambio bit a bit en los archivos monitorizados.
