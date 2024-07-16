
package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10;
    
    //Métodos insertar es abstracto y sin cuerpo
    void insertat();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
    
}
